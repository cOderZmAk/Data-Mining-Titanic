#Step 2: Drop rows with missing values and displaying how many rows were dropped

import pandas as pd

data = pd.read_csv('titanic.csv')

original_column_length = len(data)

data_cleaned = data.dropna()

new_column_length = len(data_cleaned)

rows_dropped = original_column_length - new_column_length

print(f'Original length: {original_column_length}')
print(f'Rows dropped: {rows_dropped}')