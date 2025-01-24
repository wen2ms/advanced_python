import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_series = pd.Series(np.random.randn(1000))

print_line = lambda data: print(data, '\n')

data_cumulative_sum =  data_series.cumsum()

data_cumulative_sum.plot()

dataframe = pd.DataFrame(np.random.randn(1000, 4), columns=list('ABCD'))

dataframe_cumulative_sum = dataframe.cumsum()

dataframe_cumulative_sum.plot()

ax = dataframe_cumulative_sum.plot.scatter(x='A', y='B', color='tomato', label='AB')
dataframe_cumulative_sum.plot.scatter(x='A', y='C', color='skyblue', label='AC', ax=ax)

plt.show()