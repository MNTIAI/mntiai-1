students = [
{"name": "John Doe",
"father name": "Robert Doe",
"Address": "123 Hall street"
},
{
"name": "Rahul Garg",
"father name": "Kamal Garg",
"Address": "3-Upper-Street corner"
},
{
"name": "Angela Steven",
"father name": "Jabob steven",
"Address": "Unknown"

}
]
print(list(map(lambda student:student['name'], students)))
print(list(map(lambda student:student['Address'], students)))


import numpy as np
import pandas as pd
tech={'Fees':[20000,25000,23000,26000],
'Duration':['30 Days','50 Days','30 Days','35Dys']}
df=pd.DataFrame(tech)
print(df)
# lambda function
df['Fees']= df['Fees'].map(lambda x:x==(x*10/100))
print(df)


import numpy as np
import pandas as pd
df=pd.DataFrame(np.array([[2,3,4],[5,6,7]]),
index=['tiger','lion'],columns=['one','two','three'])
print(df)
print(df.filter(items=['one','three']))
print(df.filter(regex='e$',axis=1))


#Using Reduce functions:
from functools import reduce
lst = [2,4,6,8]
#find largest element
max=reduce(lambda x, y: x if x>y else y, lst)
print(max)
#find smallest element
min=reduce(lambda x, y: x if x<y else y, lst)
print(min)