import pandas as pd


# pass in the dictionary into the arg
def make_dataframe_from_sales_data(sales):
    # concatenate sales/file data ; in other word sums up all separate file data into one large summary of data
    # concatenating along the row axis=0 sorting keys in order
    df = pd.concat(sales, axis=0, keys=sorted(sales.keys()), names=['Year', 'Month'])
    # convert month strings to numbers

    lookup = {'Jan': '01', 'Feb': '02', 'Mar': '03',
              'Apr': '04', 'May': '05', 'Jun': '06',
              'Jul': '07', 'Aug': '08', 'Sep': '09',
              'Oct': '10', 'Nov': '11', 'Dec': '12'}
    df = df.rename(index=lookup)

    # convert the (year, month) MultiIndex to a 'year-month' index example ('2010-07')
    df.index = ["-".join(x) for x in df.index.ravel()]

    # convert the 'year-month' strings to datetime objects example ('2010-07')
    df.index = pd.to_datetime(df.index)

    return df

    # sales_df = make_dataframe_from_sales_data(add_directory)
