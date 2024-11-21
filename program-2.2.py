import pandas as p
d=p.DataFrame([[2,5,6],[4,6,3],[5,7,8]],columns=["maths","java","python"])
print(d)
c=d.agg(['sum','min','max','count','mean','median','std','size'])
print(c)
print(d.describe())
a=d.groupby("maths")
print(a.first())