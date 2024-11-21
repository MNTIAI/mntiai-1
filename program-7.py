import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv(r'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',header=None)
data.columns=['sepal length ', 'sepal width',
'petal length', 'petal width','class']
print(data.head())

from pandas.api.types import is_numeric_dtype
for col in data.columns:
    if is_numeric_dtype(data[col]):
        print('%s'%(col))
        print('\t Mean=%.2f'%data[col].mean())
        print('\t StandardDeviation=%.2f'%data[col].std())
        print('\t Minimum=%.2f'%data[col].min())
        print('\t Maximum=%.2f'%data[col].max())
        numeric_columns =data.select_dtypes(include='number').columns
        covariance_series =data[numeric_columns].cov()[col]
        print('\tCovariance:')
        for covariate, value in covariance_series.items():
            print(f'\t\t {covariate}: {value:.2f}')
#matplotlib inline
data['sepal length '].hist(bins=8)
data.boxplot()
plt.show()