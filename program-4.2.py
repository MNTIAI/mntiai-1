import pandas as pd
from datetime import datetime
import numpy as np
range_date = pd.date_range(start
='1/10/2023', end ='31//10/2023',freq
='Min')
df = pd.DataFrame(range_date, columns
=['date'])
df['data'] = np.random.randint(0, 100, size
=(len(range_date)))
string_data = [str(x) for x in range_date]
print(string_data[1:11])