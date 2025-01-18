import pandas as pd
import numpy as np

dates = pd.date_range('20250118', periods=6)

dataframe = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])

dataframe.iloc[0, 1] = np.nan
dataframe.iloc[1, 2] = np.nan

print_newline = lambda data: print(data, '\n')

print_newline(dataframe)

print_newline(dataframe.dropna(axis=0, how='any'))

print_newline(dataframe.dropna(axis=1, how='any'))

print_newline(dataframe.fillna(value=0))

print_newline(dataframe.isna())

if np.any(dataframe.isna()):
    print_newline("There is at least a missing data in the dataframe")
else:
    print_newline("There isn't a missing data in the dataframe")