import pandas as pd

# Reference: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.replace.html#pandas.DataFrame.replace
df['col_name'].replace('ori_val', 'new_val', inplace=True)
df['col_name'].replace(['ori_val_1', 'ori_val_2'], 'new_val', inplace=True)
df['col_name'].replace(['ori_val_1', 'ori_val_2'], ['new_val_1', 'new_val_2'], inplace=True) # Replace original value 1 with new value 1, and original value 2 with new value 2
