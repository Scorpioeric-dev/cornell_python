import pandas as pd

df = pd.read_csv('sales.txt')

print(df.index)
df.set_index('day', inplace=True)
print(df)

df.sum(axis=0)
# sums up the entire table values by column
# investigate allows one to drop values from a df in the event it is nan
df.dropna()
# process for dropping data syntax
df['A'].dropna()

# specify the threshold of values
df.dropna(thresh=20)

# drop data based on axis (example of row) and the how key implies the count
df.dropna(axis=1, how=any)

# pandas has the ability to fill in any missing values using the fillna method with generic data
df.fillna(0.5)
# or you can use the average if dealing with int
df.fillna(df.mean())
