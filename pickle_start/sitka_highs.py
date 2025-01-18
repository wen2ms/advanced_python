import pandas as pd
import pickle
import matplotlib.pyplot as plt

class SitkaWeather:
    def __init__(self, dataframe):
        self.dates = pd.to_datetime(dataframe.DATE)
        self.highs = dataframe.TMAX
        self.lows = dataframe.TMIN

    def plot(self):
        plt.style.use('seaborn-v0_8')

        fig, ax = plt.subplots()
        ax.plot(self.dates, self.highs, color='r', alpha=0.7)
        ax.plot(self.dates, self.lows, color='b', alpha=0.7)
        ax.fill_between(self.dates, self.lows, self.highs, facecolor='b', alpha=0.15)

        ax.set_title('Daily High Temperatures, 2021', fontsize=14)

        ax.set_xlabel('', fontsize=10)
        fig.autofmt_xdate()

        ax.set_ylabel('Temperature (F)', fontsize=10)

        ax.tick_params(labelsize=10)

        plt.show()

dataframe = pd.read_csv('pickle_start/sitka_weather_2021_simple.csv')

data = SitkaWeather(dataframe)

with open('pickle_start/sitka_weather_2021_simple.pkl', 'wb') as outfile:
    pickle.dump(data, outfile)

with open('pickle_start/sitka_weather_2021_simple.pkl', 'rb') as infile:
    sitka_weather = pickle.load(infile)

sitka_weather.plot()

