from math import sqrt
from numpy import concatenate
from matplotlib import pyplot
from pandas import read_csv
from pandas import DataFrame
from pandas import concat
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import numpy as np

file = open("test3.txt", "r")

data = file.read().splitlines()

all_series = []
for i in range(0, round(len(data)/485)):
    series = data[i*485:(i+1)*485]
    float_series = [ float(elem) for elem in series ]
    all_series.append(float_series)


pyplot.plot(all_series[0], label="actual")
pyplot.plot(all_series[1], label='predicted with no sentiment')
pyplot.plot(all_series[2], label='predicted with linear sentiment')
pyplot.plot(all_series[3], label='predicted with log sentiment')
pyplot.title("Stock prediction for 5 days from now using past 10 days' data")
pyplot.ylabel("Stock Price ($US)")
pyplot.xlabel("Day")
pyplot.legend()
pyplot.show()
