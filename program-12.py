import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from matplotlib.colors import ListedColormap
# Load dataset and prepare features and labels
data = pd.read_csv(r"C:\Users\TEMP\Desktop\Dataset\User_Data.csv")
X, y = data.iloc[:, [2, 3]].values, data.iloc[:, 4].values

# Split and scale the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
X_train = StandardScaler().fit_transform(X_train)
X_test = StandardScaler().fit_transform(X_test)
# Train Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, criterion='entropy', random_state=0)
clf.fit(X_train, y_train)
# Predict and evaluate
y_pred = clf.predict(X_test)
print(confusion_matrix(y_test, y_pred))
# Visualize results
x1, x2 = np.meshgrid(np.arange(X_train[:, 0].min() - 1, X_train[:, 0].max() + 1,0.01),np.arange(X_train[:, 1].min() - 1, X_train[:, 1].max() + 1, 0.01))
Z = clf.predict(np.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape)
plt.contourf(x1, x2, Z, alpha=0.75, cmap=ListedColormap(('purple', 'green')))
plt.xlim(x1.min(), x1.max())
plt.ylim(x2.min(), x2.max())
# Plot training set results
for i, j in enumerate(np.unique(y_train)):
    plt.scatter(X_train[y_train == j, 0], X_train[y_train == j, 1],c=ListedColormap(('purple', 'green'))(i), label=j)
    plt.title('Random Forest Algorithm (Training set)')
    plt.xlabel('Age')
    plt.ylabel('Estimated Salary')
    plt.legend()
    plt.show()