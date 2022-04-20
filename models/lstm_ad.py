import pandas as pd
import numpy as np

from keras.models import Sequential, Model
from keras.layers import TimeDistributed, Input, Dense, LSTM, RepeatVector

class LSTM_AD:
    
    def __init__(self, activation='relu', optimizer='adam', loss='mse'):
        self.activation = activation
        self.optimizer = optimizer
        self.loss = loss
        
        self.encoder_model_inf = None
        self.decoder_model_inf = None
    
    def fit(self, train_windows, units=128, batch_size=32, epochs=2):
        windows_count, time_steps, n_features = train_windows.shape
        window_shape = (time_steps, n_features)

        encoder_input = Input(shape = (None, n_features))
        encoder_LSTM = LSTM(128, return_state = True)
        _, encoder_h, encoder_c = encoder_LSTM(encoder_input)
        encoder_states = [encoder_h, encoder_c]

        decoder_input = Input(shape = (None, n_features))
        decoder_LSTM = LSTM(128, return_sequences = True, return_state = True)
        decoder_out, _, _ = decoder_LSTM(decoder_input, initial_state = encoder_states)
        decoder_dense = TimeDistributed(Dense(n_features, activation = self.activation))
        decoder_out = decoder_dense(decoder_out)

        model = Model(inputs=[encoder_input, decoder_input], outputs=[decoder_out])
        model.compile(optimizer=self.optimizer, loss=self.loss)

        model.fit(x=[train_windows, train_windows], y=train_windows, 
                  batch_size=batch_size , epochs=epochs)
        
        # Determine inference models
        self.encoder_model_inf = Model(encoder_input, encoder_states)
        decoder_state_input_h = Input(shape = (128, ))
        decoder_state_input_c = Input(shape = (128, ))
        decoder_input_states = [decoder_state_input_h, decoder_state_input_c]

        decoder_out, decoder_h, decoder_c = decoder_LSTM(decoder_input, 
                                                         initial_state = decoder_input_states)
        decoder_states = [decoder_h, decoder_c]
        decoder_out = decoder_dense(decoder_out)

        self.decoder_model_inf = Model(inputs = [decoder_input] + decoder_input_states,
                                       outputs = [decoder_out] + decoder_states)
        
        return self
    
    def predict(self, test_windows):
        windows_count, time_steps, n_features = test_windows.shape
        start_symbol = -1 * np.ones(n_features) # Sequence start symbol for decoder
        
        encoded_windows = self.encoder_model_inf.predict(test_windows)
        encoded_windows = np.array(encoded_windows)
        
        predictions = []

        for win_no, window in enumerate(test_windows):
            h, c = encoded_windows[:, win_no, :]
            h = np.reshape(h, (1,len(h)))
            c = np.reshape(c, (1,len(c)))

            window[0] = start_symbol    
            window = np.reshape(window, (1, time_steps, n_features))

            decoder_out, decoder_h, decoder_c = self.decoder_model_inf.predict([window,h,c])
            predictions.append(decoder_out[0])
            
        return predictions
