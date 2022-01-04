import pandas as pd


df = pd.read_csv('sales.txt')

print(df.index)
df.set_index('day', inplace=True)
print(df)