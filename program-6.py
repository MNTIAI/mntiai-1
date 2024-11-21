import pandas as pd
import numpy as np
dict = {
'First Score':[100, 90, np.nan, 95],
'Second Score': [30, 45, 56, np.nan],
'Third Score':[np.nan, 40, 80, 98]
}
df = pd.DataFrame(dict)
print(df.isnull ())


import pandas as pd
import numpy as np
dict = {
'First Score':[100, 90, np.nan, 95],
'Second Score': [30, 45, 56, np.nan],
'Third Score':[np.nan, 40, 80, 98]}
df = pd.DataFrame(dict)
print(df.notnull())


import pandas as pd
import numpy as np
dict = {
'First Score':[100, 90, np.nan, 95],
'Second Score': [30, 45, 56, np.nan],
'Third Score':[np.nan, 40, 80, 98]
}
df = pd.DataFrame(dict)
print(df.fillna (5))


import pandas as pd
import numpy as np
dict = {
'First Score':[100, 90, np.nan, 95],
'Second Score': [30, 45, 56, np.nan],
'Third Score':[np.nan, 40, 80, 98]
}
df = pd.DataFrame(dict)
print(df.fillna(method='pad'))# method=’pad sameas ffilll()


import pandas as pd
import numpy as np
dict = {
'First Score':[100, 90, np.nan, 95],
'Second Score': [30, 45, 56, np.nan],
'Third Score':[np.nan, 40, 80, 98]
}
df = pd.DataFrame(dict)
print(df.fillna(method='bfill'))


import pandas as pd
import numpy as np
dict = {
'First Score':[100, 90, np.nan, 95],
'Second Score': [30, 45, 56, np.nan],
'Third Score':[np.nan, 40, 80, 98]
}
df = pd.DataFrame(dict)
print(df.interpolate ())


import pandas as pd
import numpy as np
dict = {
'First Score':[100, 90, np.nan, 95],
'Second Score': [30, 45, 56, np.nan],
'Third Score':[np.nan, 40, 80, 98]
}
df = pd.DataFrame(dict)
df['Second Score']=df['Second Score'].fillna(df['Second Score'].mean())
print(df)
df['Second Score']=df['Second Score'].fillna(df['Second Score'].median())
print(df)


import pandas as pd
import numpy as np
dict = { 'First Score':[100, 90, np.nan, 95],
'Second Score': [30, np.nan,45, 56,],
'Third Score':[np.nan, 40, 80, 98],
'Fourth Score':[np.nan, np.nan, np.nan, 65]
}
df = pd.DataFrame(dict)
print(df)
df.dropna ()
print (df)
print(df.dropna(axis=0))


import pandas as pd
import numpy as np
dict = { 'First Score':[100, 90, np.nan, 95],
'Second Score': [30, np.nan,45, 56,],
'Third Score':[np.nan, 40, 80, 98],
'Fourth Score':[np.nan, np.nan, np.nan, 65]
}
df = pd.DataFrame(dict)
print(df)
print(df.dropna(axis=1))