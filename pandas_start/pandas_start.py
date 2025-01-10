import pandas as pd
import numpy as np

series = pd.Series([1, 2, 3, np.nan, 5])

print(series)

dates = pd.date_range('20250101', periods=6)
print(dates)

data_frame = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])
print(data_frame)

numbers = pd.DataFrame(np.arange(20).reshape((4, 5)))
print(numbers)

dict_frame = pd.DataFrame({
        'A': 1,
        'B': pd.Timestamp('20250101'),
        'C': pd.Series(np.arange(4), index=list(range(4)), dtype='float32'),
        'D': np.array([3] * 4, dtype='int32'),
        'E': pd.Categorical(['test', 'train', 'test', 'train']),
        'F': 'foo'})

print(dict_frame)

print(dict_frame.dtypes)

print(dict_frame.index)
print(dict_frame.columns)

print(dict_frame.values)

print(dict_frame.describe())

# dict_frame.T
print(dict_frame.transpose())

print(dict_frame.sort_index(axis=1, ascending=False))
print(dict_frame.sort_index(axis=0, ascending=False))

print(dict_frame.sort_values(by='E'))