import pandas as pd

df= pd.read_csv("Batting_2019.csv")

df= pd.DataFrame(df)

df.info()