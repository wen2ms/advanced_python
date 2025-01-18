import pandas as pd

dataframe = pd.read_csv('pandas_start/studens.csv')

print(dataframe)

dataframe.index = dataframe.index + 1
print(dataframe)

dataframe.to_pickle('pandas_start/new_studens.pickle')