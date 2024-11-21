#Bar chart
from matplotlib import pyplot as p
pro_na=["intel","amd","snapdragon","tensor"]
use=[200,180,250,56]
p.bar(pro_na,use,color="black",width=0.2)
p.xlabel("processors")
p.ylabel("number of users")
p.title("processor users in a community")
p.show()

#histogram
from matplotlib import pyplot as p
import numpy as n
x=n.random.normal(180,5,200)
p.hist(x,color='red')
p.xlabel("height in cm"),p.ylabel("people")
p.title("height of 200 people")
p.show()

#pie chart
import matplotlib.pyplot as plt
cars=['AUDI', 'BMW', 'FORD', 'TESLA',
'JAGUAR']
data=[23,13,35,15,12]
explode=[0.1,0.5,0,0,0]
colors=("orange", "cyan", "yellow", "grey",
"green")
plt.pie(data, labels=cars, explode=explode,
autopct='%1.2f%%', colors=colors,
shadow=True)
plt.show()

#line graph
from matplotlib import pyplot as p
Q=["Q1","Q2","Q3","Q4"]
ssd=[200,230,350,400]
hdd=[250,240,320,250]
p.plot(Q,ssd,'^-',color='green')
p.plot(Q,hdd,'o-.b')
p.xlabel("quarters in 2022"),p.ylabel("salesunits")
p.title("sdd & hdd sales in store")
p.legend(['sdd','hdd'])
p.show()

#scatter plot
from matplotlib import pyplot as p
x=[2,6,8,7,3,2,5]
y=[6,7,8,9,7,5,3]
c=['k','b']
p.scatter(x,y,label="value of xy",color='green')
p.xlabel('x')
p.ylabel('y')
p.legend()
p.show()