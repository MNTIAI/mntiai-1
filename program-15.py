import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
iris=pd.read_csv(r"C:\Users\TEMP\Desktop\Dataset\Iris1.csv")
print(iris)

#Plot scatter by comparing
fig=iris[iris.variety=='Setosa'].plot.scatter(x='petal.length',y='petal.width',color='orange',
label='Setosa')
iris[iris.variety=='Versicolor'].plot.scatter(x='petal.length',y='petal.width',color='blue',label='Versicolor',ax=fig)
iris[iris.variety=='Virginica'].plot.scatter(x='petal.length',y='petal.width',color='green',
label='Virginica',ax=fig)
fig.set_xlabel("petal.length")
fig.set_ylabel("petal.width")
fig.set_title("petal length and width")
fig=plt.gcf()
fig.set_size_inches(8,8)
plt.show()
#To display all data whose values -1.4
petal_width=iris[iris['petal.length']==1.4]
print(petal_width)
#To known the how many times each value inpetal length is given
count=iris.groupby('petal.length')['petal.length'].count()

print(count)
#To find the sum of petal length column
sum=iris['petal.length'].sum()
print(sum)
#To known the max size of sepal widthcolumn
max=iris['sepal.width'].max()
print(max)
#To add 1.0 to all the inputs in sepal lengthcolumn
add=iris['sepal.length']+1.0
print(add)