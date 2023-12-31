# -*- coding: utf-8 -*-
"""spaceship titatnic.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZHQYot_6kYdl9_JV14wvtwBOrawgkpSJ
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv('/content/train.csv')

df.head()

df.info()

df.describe()

sns.heatmap(df.corr())

cr = df.corr()

cr_df = cr['Transported'].sort_values(ascending=False)
cr_df

plot_df =df.Transported.value_counts()
plot_df.plot(kind="bar")

fig, ax = plt.subplots(5,1,  figsize=(10, 10))
plt.subplots_adjust(top = 2)

sns.histplot(df['Age'], color='g', bins=50, ax=ax[0]);
sns.histplot(df['FoodCourt'], color='g', bins=50, ax=ax[1]);
sns.histplot(df['ShoppingMall'], color='g', bins=50, ax=ax[2]);
sns.histplot(df['Spa'], color='g', bins=50, ax=ax[3]);
sns.histplot(df['VRDeck'], color='g', bins=50, ax=ax[4]);

df.isnull().sum()

df[['VIP', 'CryoSleep', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck']] = df[['VIP', 'CryoSleep', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck']].fillna(value=0)
df.isnull().sum().sort_values(ascending=False)

# df['Age'].fillna(df['Age'].mean().round(0),inplace=True)
# df['RoomService'].fillna(df['RoomService'].mean().round(0),inplace=True)
# df['FoodCourt'].fillna(df['FoodCourt'].mean().round(0),inplace=True)
# df['ShoppingMall'].fillna(df['ShoppingMall'].mean().round(0),inplace=True)
# df['Spa'].fillna(df['Spa'].mean().round(0),inplace=True)
# df['VRDeck'].fillna(df['VRDeck'].mean().round(0),inplace=True)

df['VIP'] = df['VIP'].astype(int)
df['CryoSleep'] =df['CryoSleep'].astype(int)

label = "Transported"
df[label] = df[label].astype(int)

df=df.drop('Name', axis=1)

df.drop(columns=['HomePlanet','Cabin','Destination'],axis=1,inplace=True)

df.head()



df.head()

df.isnull().sum()

df['Age'].fillna(df['Age'].mean().round(0),inplace=True)
df['RoomService'].fillna(df['RoomService'].mean().round(0),inplace=True)

df.isnull().sum()

from sklearn.model_selection import train_test_split

X= df.drop(columns=['Transported'])
y= df['Transported']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 42)

from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import accuracy_score

lr= LinearRegression()
lr.fit(X_train, y_train)

y_pred= lr.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2_square = r2_score(y_test,y_pred)
print(f" R-squared: {r2_square}")
print(f'Mean Squared Error: {mse}')

knn= KNeighborsClassifier(n_neighbors=2)
knn.fit(X_train, y_train)

y_pred1=knn.predict(X_test)

accuracy= accuracy_score(y_test, y_pred1)
accuracy

rf= RandomForestClassifier()
rf.fit(X_train, y_train)

y_pred2= rf.predict(X_test)

accuracy= accuracy_score(y_test, y_pred2)
accuracy

dtc= DecisionTreeClassifier()
dtc.fit(X_train, y_train)

y_pred3= dtc.predict(X_test)

accuracy= accuracy_score(y_test, y_pred3)
accuracy

lr_1= LogisticRegression()
lr_1.fit(X_train, y_train)

y_pred4= lr_1.predict(X_test)

accuracy= accuracy_score(y_test, y_pred4)
accuracy

