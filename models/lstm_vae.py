from keras.layers import Input, LSTM, Lambda, RepeatVector, Dense, TimeDistributed
from keras.models import Model

from keras import backend
import tensorflow as tf
from tensorflow.keras import losses



class LSTM_VAE:
    def __init__(self, activation='relu', optimizer='adam', 
                 loss=losses.MeanSquaredError, hat_mean=0, hat_sigma=1):
        
        self.activation = activation
        self.optimizer = optimizer
        if isinstance(loss, losses.Loss):
            raise TypeError("Loss should be keras class")
        self.loss = loss()
        
        self.hat_mean = hat_mean
        self.hat_sigma = hat_sigma
        
    def fit(self, train_windows, batch_size=32, epochs=2):
        windows_count, time_steps, n_features = train_windows.shape
        
        encoder_input = Input(shape = (None, n_features))
        encoder_output = LSTM(units=128, return_state = False, 
                              return_sequences = False)(encoder_input)
        
        latent_dim = 64
        z_mean = Dense(units=latent_dim, name="z_mean")(encoder_output)
        z_sigma = Dense(units=latent_dim, name="z_sigma")(encoder_output)
        
        def sampling(args):
            z_mean, z_sigma = args
            epsilon = backend.random_normal(
                shape=(latent_dim, ), mean=self.hat_mean, stddev=self.hat_sigma)
            
            return z_mean + z_sigma * epsilon
            
        
        z = Lambda(sampling, output_shape=(latent_dim, ))([z_mean, z_sigma])
        z_repeat = RepeatVector(time_steps)(z)
        
        decoder_lstm = LSTM(units=128, return_state = False, 
                            return_sequences = True)(z_repeat)
        
        decoder_output = TimeDistributed(Dense(n_features))(decoder_lstm)
        
        self.model = Model(encoder_input, decoder_output)
        
        def loss_function(x, x_reconstructed):
            reconstructed_loss = self.loss(x, x_reconstructed)
            kl_loss = -0.5 * backend.mean(
                self.hat_sigma + z_sigma - backend.square(z_mean) - backend.exp(z_sigma))

            return reconstructed_loss + kl_loss
        
        self.model.add_loss(loss_function(encoder_input, decoder_output))
        
        self.model.compile(optimizer=self.optimizer, loss=None)
        history = self.model.fit(train_windows, train_windows, 
                                 epochs=epochs, batch_size=batch_size)
        return self
    
    def predict(self, test_windows):
        return self.model.predict(test_windows)