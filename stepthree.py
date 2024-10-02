import pandas as pd

data = pd.read_csv('titanic.csv')

dropped_deck = data.drop(columns=['deck'])

original_column_length = len(dropped_deck)

data_cleaned = dropped_deck.dropna()

new_column_length = len(data_cleaned)

rows_dropped = original_column_length - new_column_length

print(f'Original length: {original_column_length}')
print(f'Number of rows dropped after removing the column deck: {rows_dropped}')