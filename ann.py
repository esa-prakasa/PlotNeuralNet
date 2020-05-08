import pandas as pd
import os

os.system("cls")

# Location of dataset
url = "C:\\Users\\INKOM06\\Documents\\a1OpenCVcodes\\neural\\iris.data"

# Assign colum names to the dataset
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']

# Read dataset to pandas dataframe
irisdata = pd.read_csv(url, names=names)

print(irisdata.head())

# Assign data from first four columns to X variable
X = irisdata.iloc[:, 0:4]

# Assign data from first fifth columns to y variable
y = irisdata.select_dtypes(include=[object])


print(y.head())

print(y.Class.unique())

from sklearn import preprocessing
le = preprocessing.LabelEncoder()

y = y.apply(le.fit_transform)

print(y.Class.unique())


# Create Training and testing dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)


### Training and Predictions

from sklearn.neural_network import MLPClassifier
#mlp = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=1000)
mlp = MLPClassifier(hidden_layer_sizes=(5, 8, 15, 10, 8), max_iter=1000)
mlp.fit(X_train, y_train.values.ravel())

 
predictions = mlp.predict(X_test)
print(predictions)

# Final prediction
from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))






print("Done!")