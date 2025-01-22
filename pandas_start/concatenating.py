import pandas as pd
import numpy as np

dataframe_1 = pd.DataFrame(np.zeros((3, 4)), columns=['A', 'B', 'C', 'D'])
dataframe_2 = pd.DataFrame(np.ones((3, 4)), columns=['A', 'B', 'C', 'D'])
dataframe_3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['A', 'B', 'C', 'D'])

print_newline = lambda data: print(data, '\n')

print_newline(dataframe_1)
print_newline(dataframe_2)
print_newline(dataframe_3)

vertical_concatenating_dataframe = pd.concat([dataframe_1, dataframe_2, dataframe_3], axis=0, ignore_index=True)

print_newline(vertical_concatenating_dataframe)

dataframe_2.index = [2, 3, 4]
dataframe_2.columns = ['B', 'C', 'D', 'E']

print_newline(dataframe_2)

inner_joining_dataframe = pd.concat([dataframe_1, dataframe_2], join='inner', ignore_index=True)
outer_joining_dataframe = pd.concat([dataframe_1, dataframe_2], join='outer', ignore_index=True)

print_newline(inner_joining_dataframe)
print_newline(outer_joining_dataframe)

series = pd.Series([1, 2, 3, 4], index=['A', 'B', 'C', 'D'])
concat_series_dataframe = pd.concat([dataframe_1, series.to_frame().T], axis=0, ignore_index=True)

print_newline(concat_series_dataframe)