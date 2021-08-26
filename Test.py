import pandas as pd
import numpy as np 
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

## Importing the data files 
df = pd.read_excel("df.xlsx") 

# Setting up multiple linear regression model
y = np.array(df['Suicide rate (deaths per 100,000 individuals)'].values)
x = np.array(df[['20-24 years old (%)', '10-14 years old (%)', '15-19 years old (%)', '30-34 years old (%)', '25-29 years old (%)', '50-69 years old (%)', '15-49 years old (%)', '70+ years old (%)', 'Prevalence in males (%)', 'Prevalence in females (%)']].values)

# Creating train and test variables
x_train, x_test, y_train, y_test=train_test_split(x, y, test_size=0.2, random_state=10)

# Creating Model 
x_model = LinearRegression()

# fitting data to model
x_model.fit(x_train, y_train)

#accuracy
accuracy = x_model.score(x_test, y_test)

# Predicting from model 
x_model_pred = x_model.predict(x_test)

# Getting Intercept
x_intercept = x_model.intercept_

# Getting Coefficient 
x_coefficient = x_model.coef_

# Printing Intercept
print('Printing Intercepts')
print('x Factor: ', x_intercept)

# Printing Coefficient 
print('\nPrinting Coefficients')
print('x Factor: ', x_coefficient)

#Printing accuracy
print("Accuracy: ", format(int(round(accuracy * 10))), "%")
