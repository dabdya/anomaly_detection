from keras.models import Sequential
from keras.layers import TimeDistributed, Dense, LSTM, RepeatVector

class LSTM_AE:
    def __init__(self, activation="relu", optimizer="adam", loss="mse"):
        self.activation = activation
        self.optimizer = optimizer
        self.loss = loss
        
    def fit(self, x_train, epochs, batch_size, TIME_STEPS):
        n_features = x_train.shape[2]
        self.model = Sequential()
        self.model.add(LSTM(units=128, activation=self.activation, return_sequences=True, 
                       input_shape=(x_train.shape[1], x_train.shape[2])))
        self.model.add(LSTM(units=64, activation=self.activation, return_sequences=False))
        # Encoding is done
        self.model.add(RepeatVector(TIME_STEPS))
        self.model.add(LSTM(units=64, activation=self.activation, return_sequences=True))
        self.model.add(LSTM(units=128, activation=self.activation, return_sequences=True))
        self.model.add(TimeDistributed(Dense(n_features)))
        self.model.compile(optimizer=self.optimizer, loss=self.loss)   
        history = self.model.fit(x_train, x_train, epochs=epochs, batch_size=batch_size)
        return self
    
    def predict(self, x_test):
        return self.model.predict(x_test)