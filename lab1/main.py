import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r'Data1.csv',index_col=0, parse_dates=True)
#df.set_index(df.columns[0])
#print(df)
df.head()
df.plot()
#print (df)