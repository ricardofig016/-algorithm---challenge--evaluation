try:
    from sklearn.model_selection import train_test_split
except ImportError:
    from sklearn.cross_validation import train_test_split
from sklearn.datasets import make_classification
from sklearn.datasets import make_regression
from scipy.spatial import distance
import glob
import pandas as pd
import os

from mla import knn
from mla.metrics.metrics import mean_squared_error, accuracy


def regression():
    # Generate a random regression problem
    #X, y = make_regression(
     #   n_samples=500, n_features=5, n_informative=5, n_targets=1, noise=0.05, random_state=1111, bias=0.5
    #)
    files1 = glob.glob("noise_outliers/*.csv")
    files2 = glob.glob("class_imbalance/*.csv")
    files3 = glob.glob("multiclass_classification/*.csv")
    for file1 in files1:
        df = pd.read_csv(file1)
        X = df.drop(df.columns[-1], axis=1)
        y = df.iloc[ :, -1:]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
        model = knn.KNNRegressor(k=5, distance_func=distance.euclidean)
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        print("regression mse", mean_squared_error(y_test, predictions))
    for file2 in files2:
        df = pd.read_csv(file2)
        X = df.drop(df.columns[-1], axis=1)
        y = df.iloc[ :, -1:]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
        model = knn.KNNRegressor(k=5, distance_func=distance.euclidean)
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        print("regression mse", mean_squared_error(y_test, predictions))
    for file3 in files3:
        df = pd.read_csv(file3)
        X = df.drop(df.columns[-1], axis=1)
        y = df.iloc[ :, -1:]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
        model = knn.KNNRegressor(k=5, distance_func=distance.euclidean)
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        print("regression mse", mean_squared_error(y_test, predictions))


def classification():
   # X, y = make_classification(
    #    n_samples=500,
     #   n_features=5,
      #  n_informative=5,
       # n_redundant=0,
        #n_repeated=0,
        #n_classes=3,
        #random_state=1111,
        #class_sep=1.5,
    #)
    files1 = glob.glob('noise_outliers/*.csv')
    files2 = glob.glob('class_imbalance/*.csv')
    files3 = glob.glob('multiclass_classification/*.csv')
    for file1 in files1:
        df = pd.read_csv(file1)
        X = df.drop(df.columns[-1], axis=1)
        y = df.iloc[ :, -1:]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
        model = knn.KNNClassifier(k=5, distance_func=distance.euclidean)
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        print("regression mse", mean_squared_error(y_test, predictions))
    for file2 in files2:
        df = pd.read_csv(file2)
        X = df.drop(df.columns[-1], axis=1)
        y = df.iloc[ :, -1:]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
        model = knn.KNNClassifier(k=5, distance_func=distance.euclidean)
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        print("regression mse", mean_squared_error(y_test, predictions))
    for file3 in files3:
        df = pd.read_csv(file3)
        X = df.drop(df.columns[-1], axis=1)
        y = df.iloc[ :, -1:]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
        model = knn.KNNClassifier(k=5, distance_func=distance.euclidean)
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        print("regression mse", mean_squared_error(y_test, predictions))


if __name__ == "__main__":
    regression()
    #classification()
