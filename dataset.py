import pandas as pd

data=pd.read_csv("C:/Users/SPTINT-25/Desktop/dataset2/Iris.csv")
print(data)
print(data.head(5))
print(data.tail(10))
print(data["SepalLengthCm"])
print(data.info())
print(data.dtypes)
print(data.count())

