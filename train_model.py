
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pickle

# Sample data
data = pd.DataFrame({
    'brand': ['Dell', 'HP', 'Lenovo', 'Dell', 'HP'],
    'processor': ['i5', 'i7', 'i3', 'i5', 'i7'],
    'ram': [8, 16, 4, 8, 16],
    'storage': [512, 1024, 256, 512, 1024],
    'gpu': ['Intel', 'Nvidia', 'Intel', 'Intel', 'Nvidia'],
    'os': ['Windows', 'Windows', 'Linux', 'Windows', 'Windows'],
    'price': [50000, 75000, 30000, 52000, 77000]
})

X = data.drop('price', axis=1)
y = data['price']

categorical_features = ['brand', 'processor', 'gpu', 'os']
numeric_features = ['ram', 'storage']

preprocessor = ColumnTransformer([
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
], remainder='passthrough')

model = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

model.fit(X, y)

with open("laptop_price_model.pkl", "wb") as f:
    pickle.dump(model, f)
