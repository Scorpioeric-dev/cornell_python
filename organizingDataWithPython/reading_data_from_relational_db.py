import pandas as pd
# from google.cloud import bigquery
# client = bigquery.Client()
#
# query = """
#     SELECT name, SUM(number) as total_people
#     FROM `bigquery-public-data.usa_names.usa_1910_2013`
#     WHERE state = 'TX'
#     GROUP BY name, state
#     ORDER BY total_people DESC
#     LIMIT 20
# """
# query_job = client.query(query)  # Make an API request.
#
# print("The query data:")
# for row in query_job:
#     # Row values can be accessed by field name or index.
#     print("name={}, count={}".format(row[0], row["total_people"]))

# create a database
from sqlalchemy import create_engine

db = create_engine('sqlite:///product_data.sqlite')
sales = ([1,2,3,4,5],[1234,4567,789,1010,0000],['mon','tues','wed','thur','friday'])

sales = pd.read_sql('select * from sales', db)


