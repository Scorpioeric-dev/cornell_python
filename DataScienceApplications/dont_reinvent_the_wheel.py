import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# How to create a dataframe from a dictionary
d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)
print(df)

x = np.arange(0, 5, 0.1)
y = np.sin(x)
print(x)
print(y)