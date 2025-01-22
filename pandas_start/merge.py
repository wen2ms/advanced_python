import pandas as pd
import numpy as np

dataframe_1 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                            'A': ['A0', 'A1', 'A2', 'A3'],
                            'B': ['B0', 'B1', 'B2', 'B3']})

dataframe_2 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                            'C': ['C0', 'C1', 'C2', 'C3'],
                            'D': ['D0', 'D1', 'D2', 'D3']})

print_newline = lambda data: print(data, '\n')

print_newline(dataframe_1)
print_newline(dataframe_2)

merged_dataframe = pd.merge(dataframe_1, dataframe_2, on='key')

print_newline(merged_dataframe)

dataframe_1 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                            'key2': ['K0', 'K1', 'K0', 'K1'],
                            'A': ['A0', 'A1', 'A2', 'A3'],
                            'B': ['B0', 'B1', 'B2', 'B3']})

dataframe_2 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                            'key2': ['K0', 'K0', 'K0', 'K0'],
                            'C': ['C0', 'C1', 'C2', 'C3'],
                            'D': ['D0', 'D1', 'D2', 'D3']})

print_newline(dataframe_1)
print_newline(dataframe_2)

outer_merged_dataframe = pd.merge(dataframe_1, dataframe_2, on=['key1', 'key2'], how='outer')
left_merged_dataframe = pd.merge(dataframe_1, dataframe_2, on=['key1', 'key2'], how='left')

print_newline(outer_merged_dataframe)
print_newline(left_merged_dataframe)

dataframe_1 = pd.DataFrame({'col1': [0, 1], 'col2': ['a', 'b']})
dataframe_2 = pd.DataFrame({'col1': [1, 1, 2], 'col3': [2, 2, 2]})

print_newline(dataframe_1)
print_newline(dataframe_2)

given_indicator_dataframe = pd.merge(dataframe_1, dataframe_2, how='outer', indicator='indicator_column')

print_newline(given_indicator_dataframe)

dataframe_1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                            'B': ['B0', 'B1', 'B2']},
                            index=['K0', 'K1', 'K2'])

dataframe_2 = pd.DataFrame({'C': ['C0', 'C1', 'C2'],
                            'D': ['D0', 'D1', 'D2']},
                            index=['K0', 'K2', 'K3'])

print_newline(dataframe_1)
print_newline(dataframe_2)

index_merge_dataframe = pd.merge(dataframe_1, dataframe_2, left_index=True, right_index=True)

print_newline(index_merge_dataframe)

dataframe_1 = pd.DataFrame({'key': ['K0', 'K1', 'K2'],
                            'age': np.random.randint(15, 23, size=3)})

dataframe_2 = pd.DataFrame({'key': ['K0', 'K0', 'K3'],
                            'age': np.random.randint(15, 23, size=3)})

print_newline(dataframe_1)
print_newline(dataframe_2)

suffixes_dataframe = pd.merge(dataframe_1, dataframe_2, on='key', suffixes=['_1', '_2'], how='outer')

print_newline(suffixes_dataframe)