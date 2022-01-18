import pandas as pd

file = 'WHR2018Chapter2OnlineData.xls'
dfraw = pd.read_excel(file, sheet_name='Table2.1')
print(dfraw)

# grabbing columns using dot notation
print(dfraw.Generosity)
# if receive a type error when looking for columns then
print(dfraw['Life ladder'])

# we can remap the columnn name sin bulk

# creating the list of columns we want to change
cols_to_include = ['Life Ladder']
# creating a dictionary key pair with original column name as key and new column as value
renaming = {'Life Ladder': 'Happiness', }

# create a new df
df = dfraw[cols_to_include].rename(renaming, axis=1)

# changing a column type example
# dfsummary['N'] = dfsummary['N'].astype(int)
