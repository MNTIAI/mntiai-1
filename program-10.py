import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data_set=pd.read_csv(r"C:\Users\TEMP\Desktop\Dataset\Salary_Data.csv")
x=data_set.iloc[:,:-1].values
y=data_set.iloc[:, 1].values
from sklearn.linear_model import LinearRegression
lin_regs=LinearRegression()
lin_regs.fit(x,y)

from sklearn.preprocessing import PolynomialFeatures
poly_regs=PolynomialFeatures (degree=2)
x_poly=poly_regs.fit_transform(x)
lin_reg_2=LinearRegression()
lin_reg_2.fit(x_poly,y)
plt.scatter(x,y,color="blue")
plt.plot(x,lin_regs.predict(x),color="red")
plt.title("Bluff detection model(LinearRegression)")
plt.xlabel("Position Levels")
plt.ylabel("Salary")
plt.show()
plt.scatter(x,y,color="blue")
plt.plot(x,lin_reg_2.predict(poly_regs.fit_transform(x)), color="red")
plt.title("Bluff detection model (PolynomialRegression)")
plt.xlabel("Position Levels")
plt.ylabel("Salary")
plt.show()