# Import necessary libraries
from sklearn import datasets # to retrieve the iris Dataset
import pandas as pd # to load the dataframe
from sklearn.preprocessing import StandardScaler # to standardize the features
from sklearn.decomposition import PCA # toapply PCA
import seaborn as sns # to plot the heatmaps
import matplotlib.pyplot as plt
#Load the Dataset
iris = datasets.load_iris ()
#convert the dataset into a pandas dataframe
df = pd.DataFrame(iris['data'], columns = iris['feature_names'])
#display the head (first 5 rows) of thedataset
print(df.head ())
#Standardize the features
#Create an object of StandardScaler which ispresent in sklearn.preprocessing
scalar = StandardScaler()
scaled_data = pd.DataFrame(scalar.fit_transform (df))
#scaling the data
print(scaled_data)
#Check the Co-relation between featureswithout PCA
sns.heatmap(scaled_data.corr())
# Applying PCA Taking no. of PrincipalComponents as 3
plt.show()
pca = PCA(n_components = 3)
pca.fit(scaled_data)
data_pca = pca.transform(scaled_data)
data_pca =pd.DataFrame(data_pca,columns=['PC1','PC2','PC3'])
print(data_pca.head())
sns.heatmap(data_pca.corr())
plt.show()