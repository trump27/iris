
#%%
from sklearn.datasets import load_iris
import pandas as pd

#%%
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target_names[iris.target]
df.to_csv('./iris.csv', index=False)

#%%
print(iris)
print(iris.DESCR)


#%%
iris = load_iris()
df = pd.DataFrame(iris.data)
df['target'] = iris.target
df.columns = ["sepal-length", "sepal-width", "petal-length", "petal-width", "target"]
df.to_csv('./iris_data.csv', index=False)


#%%
