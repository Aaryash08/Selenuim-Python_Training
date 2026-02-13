import numpy as np
import pandas as pd
arr=np.array([1,2,3])
print("array",arr)
print("sum",np.sum(arr))
print("mean",np.mean(arr))
print("median",np.median(arr))
print("multiply",arr*2)
print("max",np.max(arr))

data={
    "Name":["Kiran","Anita","Ravi"],
    "Age":[21,22,23],
    "City":["Bangalore","Chennai","Hydrabad"]
}

df=pd.DataFrame(data)
print(df)
print(df[df["Age"]>22])
df["Salary"]=[50000,60000,70000]
print(df)
