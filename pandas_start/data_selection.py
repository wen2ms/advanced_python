import pandas as pd
import numpy as np

dates = pd.date_range('20250117', periods=6)

dataframe = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])

print(dataframe, '\n')

print(dataframe['A'], '\n')
print(dataframe.A, '\n')

print(dataframe[:3], '\n')
print(dataframe['20250117':'20250120'], '\n')

# select by labels
print(dataframe.loc['20250117'], '\n')
print(dataframe.loc['20250117', ['A', 'C']], '\n')
print(dataframe.loc['20250117', ['A']], '\n')

# select by position
print(dataframe.iloc[3], '\n')
print(dataframe.iloc[[0, 3], [0, 3]], '\n')

print(dataframe[dataframe.A > 8])