from sklearn.datasets import load_iris
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib
import numpy as np

# use Iris dataset
data = load_iris()
x = data.data
y = data.target
# x, y = data.data, data.target
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=1)

clf = svm.SVC(gamma="scale", probability=True)
clf.fit(x, y)

# save the model as pickle
joblib.dump(clf, './iris_model.pkl', compress=True)

# load the model
SVC = joblib.load('./iris_model.pkl')

# # predict
t = np.array([5.1,  3.5,  1.4,  0.2])
t = t.reshape(1, -1)
print(SVC.predict(X=t))

# # predict_proba
t = np.array([2.1,  1.5,  3.4,  1.2])
t = t.reshape(1, -1)
proba = SVC.predict_proba(t).flatten()
print('proba: ', proba)
print('index', np.argmax(proba))
print('class', SVC.classes_)

print(proba[np.argmax(proba)])
# print(proba.reshape(1))
