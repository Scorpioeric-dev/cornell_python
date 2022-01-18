import inline as inline
import matplotlib
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline
# pd.options.display.float_format = '{:.2f}'.format

dfraw = pd.read_excel('WHR2018Chapter2OnlineData.xls', sheet_name='Table2.1')

cols_to_include = ['country', 'year', 'Life Ladder',
                   'Positive affect','Negative affect',
                   'Log GDP per capita', 'Social support',
                   'Healthy life expectancy at birth',
                   'Freedom to make life choices',
                   'Generosity', 'Perceptions of corruption']

df = dfraw[cols_to_include]


def produce_summary_table(df):
    column_renaming = {'count': 'N', 'mean': 'Mean', 'std': 'Std. Dev.', 'min': 'Min.', 'max': 'Max.'}
    column_order = ['Mean', 'Std. Dev.', 'Min.', 'Max.', 'N']
    df1 = df.describe()
    #     print(df1)
    df = df1.T
    #     print(df)
    df1 = df.drop(['year'], axis=0).drop(columns=['25%', '50%', '75%'], axis=1).rename(column_renaming, axis=1)
    #     print(df1)
    dfsummary = df1[column_order]
    #     print(dfsummary)
    dfsummary['N'] = dfsummary['N'].astype(int)
    #     print(dfsummary)
    return dfsummary


print(produce_summary_table(df))



