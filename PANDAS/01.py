# print("Hello")
import pandas as pd
# s = pd.Series([142,45,23,21,54],name="count")
# s=pd.Series([142,45,23,21,54], name= "count",index=["0","1","2","3","4"])
# print(s)


s = pd.read_csv("stores.csv")
print(s.head)
# print(s.tail)

# nan_ex = pd.Series([2,None,3,None])
# print(nan_ex.count())


data = [33,34,40,41,36]
year = [2002, 2002, 2003, 2010, 2001]
s= pd.Series(data, index=year,name='data')
print(s)

for item in s.items():
  print(item)