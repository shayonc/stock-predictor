from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential
import lstm, time #helper libraries


#Step 1 Load Data
X_train, y_train, X_test, y_test = lstm.load_data('TSLA_1.csv', 50, True)


#Step 2 Build Model
model = Sequential()
model.add(LSTM(50, input_shape=(X_train.shape[1], X_train.shape[2])))
# model.add(Dropout(0.2))

# model.add(LSTM(
#     100,
#     return_sequences=False))
# model.add(Dropout(0.2))

model.add(Dense(1))
# model.add(Activation('linear'))

start = time.time()
model.compile(loss='mae', optimizer='adam')
print('compilation time : %d' % (time.time() - start))


#Step 3 Train the model
# model.fit(
#     X_train,
#     y_train,
#     batch_size=512,
#     nb_epoch=5,
#     validation_split=0.05)
history = model.fit(X_train, y_train, epochs=50, batch_size=72, validation_data=(X_test, y_test), verbose=2, shuffle=False)


#Step 4 - Plot the predictions!
# predictions = lstm.predict_sequences_multiple(model, X_test, 50, 50)
# lstm.plot_results_multiple(predictions, y_test, 50)
