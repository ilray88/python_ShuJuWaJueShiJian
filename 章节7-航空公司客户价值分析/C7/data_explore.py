import pandas as pd
datafile = "air_data.csv"
data = pd.read_csv(datafile, encoding="utf-8")
print(data.shape)
print(data.info())