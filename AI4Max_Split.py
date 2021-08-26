import pandas as pd
import numpy as np 
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

## Importing the data files 
df = pd.read_excel("df.xlsx") 

# Setting up multiple linear regression model
#y = df['Suicide rate (deaths per 100,000 individuals)']
y = df['Suicide rate (deaths per 100,000 individuals)'].values.reshape(-1,1)
age_20_24 = df['20-24 years old (%)'].values.reshape(-1,1)
age_10_14 = df['10-14 years old (%)'].values.reshape(-1,1)
age_15_19 = df['15-19 years old (%)'].values.reshape(-1,1)
age_30_34 = df['30-34 years old (%)'].values.reshape(-1,1)
age_25_29 = df['25-29 years old (%)'].values.reshape(-1,1)
age_50_69 = df['50-69 years old (%)'].values.reshape(-1,1)
age_15_49 = df['15-49 years old (%)'].values.reshape(-1,1)
age_70_up = df['70+ years old (%)'].values.reshape(-1,1)
males = df['Prevalence in males (%)'].values.reshape(-1,1)
females = df['Prevalence in females (%)'].values.reshape(-1,1)

# Creating Model 
#linear_regression = LinearRegression()
age_10_14_model = LinearRegression()
age_15_19_model = LinearRegression()
age_20_24_model = LinearRegression()
age_25_29_model = LinearRegression()
age_30_34_model = LinearRegression()
age_50_69_model = LinearRegression()
age_15_49_model = LinearRegression()
age_70_up_model = LinearRegression()
males_model = LinearRegression()
females_model = LinearRegression()

# fitting data to model
#linear_regression.fit(x,y)
age_10_14_model.fit(age_10_14, y)
age_15_19_model.fit(age_15_19, y)
age_20_24_model.fit(age_20_24, y)
age_25_29_model.fit(age_25_29, y)
age_30_34_model.fit(age_30_34, y)
age_50_69_model.fit(age_50_69, y)
age_15_49_model.fit(age_15_49, y)
age_70_up_model.fit(age_70_up, y)
males_model.fit(males, y)
females_model.fit(females, y)

# Predicting from model 
#y_pred = linear_regression.predict(x) 
age_10_14_pred = age_10_14_model.predict(age_10_14)
age_15_19_pred = age_15_19_model.predict(age_15_19)
age_20_24_pred = age_20_24_model.predict(age_20_24)
age_25_29_pred = age_25_29_model.predict(age_25_29)
age_30_34_pred = age_30_34_model.predict(age_30_34)
age_50_69_pred = age_50_69_model.predict(age_50_69)
age_15_49_pred = age_15_49_model.predict(age_15_49)
age_70_up_pred = age_70_up_model.predict(age_70_up)
males_pred = males_model.predict(males)
females_pred = females_model.predict(females)

# Getting Intercept
age_10_14_intercept = age_10_14_model.intercept_
age_15_19_intercept = age_15_19_model.intercept_
age_20_24_intercept = age_20_24_model.intercept_
age_25_29_intercept = age_25_29_model.intercept_
age_30_34_intercept = age_30_34_model.intercept_
age_50_69_intercept = age_50_69_model.intercept_
age_15_49_intercept = age_15_49_model.intercept_
age_70_up_intercept = age_70_up_model.intercept_
males_intercept = males_model.intercept_
females_intercept = females_model.intercept_

# Getting Coefficient 
age_10_14_coefficient= age_10_14_model.coef_
age_15_19_coefficient = age_15_19_model.coef_
age_20_24_coefficient = age_20_24_model.coef_
age_25_29_coefficient = age_25_29_model.coef_
age_30_34_coefficient = age_30_34_model.coef_
age_50_69_coefficient = age_50_69_model.coef_
age_15_49_coefficient = age_15_49_model.coef_
age_70_up_coefficient = age_70_up_model.coef_
males_coefficient = males_model.coef_
females_coefficient = females_model.coef_

# Plotting the models
#figure, axis = plt.subplots(2, 2)
figure, axis = plt.subplots(2,5, constrained_layout=True)

#axis[0, 0].plot(X, Y1)
axis[0, 0].scatter(age_10_14, y)
axis[0, 1].scatter(age_15_19, y)
axis[0, 2].scatter(age_20_24, y)
axis[0, 3].scatter(age_25_29, y)
axis[0, 4].scatter(age_30_34, y)
axis[1, 0].scatter(age_50_69, y)
axis[1, 1].scatter(age_15_49, y)
axis[1, 2].scatter(age_70_up, y)
axis[1, 3].scatter(males, y)
axis[1, 4].scatter(females, y)

#plt.plot(X, Y_pred, color='red')
axis[0, 0].plot(age_10_14, age_10_14_pred, color='red')
axis[0, 1].plot(age_15_19, age_15_19_pred, color='red')
axis[0, 2].plot(age_20_24, age_20_24_pred, color='red')
axis[0, 3].plot(age_25_29, age_25_29_pred, color='red')
axis[0, 4].plot(age_30_34, age_30_34_pred, color='red')
axis[1, 0].plot(age_50_69, age_50_69_pred, color='red')
axis[1, 1].plot(age_15_49, age_15_49_pred, color='red')
axis[1, 2].plot(age_70_up, age_70_up_pred, color='red')
axis[1, 3].plot(males, males_pred, color='red')
axis[1, 4].plot(females, females_pred, color='red')

#axis[0, 0].set_title("Sine Function")
axis[0, 0].set_title('Age 10-14')
axis[0, 1].set_title('Age 15-19')
axis[0, 2].set_title('Age 20-24')
axis[0, 3].set_title('Age 25-29')
axis[0, 4].set_title('Age 30-34')
axis[1, 0].set_title('Age 50-69')
axis[1, 1].set_title('Age 15-49')
axis[1, 2].set_title('Age 70+')
axis[1, 3].set_title('Males')
axis[1, 4].set_title('Females')

#Setting x axis labels
axis[0, 0].set_xlabel('Age 10-14 (%)')
axis[0, 1].set_xlabel('Age 15-19 (%)')
axis[0, 2].set_xlabel('Age 20-24 (%)')
axis[0, 3].set_xlabel('Age 25-29 (%)')
axis[0, 4].set_xlabel('Age 30-34 (%)')
axis[1, 0].set_xlabel('Age 50-69 (%)')
axis[1, 1].set_xlabel('Age 15-49 (%)')
axis[1, 2].set_xlabel('Age 70+ (%)')
axis[1, 3].set_xlabel('Males (%)')
axis[1, 4].set_xlabel('Females (%)')

# Setting y axis labels
axis[0, 0].set_ylabel('Suicide Rates (%)')
axis[0, 1].set_ylabel('Suicide Rates (%)')
axis[0, 2].set_ylabel('Suicide Rates (%)')
axis[0, 3].set_ylabel('Suicide Rates (%)')
axis[0, 4].set_ylabel('Suicide Rates (%)')
axis[1, 0].set_ylabel('Suicide Rates (%)')
axis[1, 1].set_ylabel('Suicide Rates (%)')
axis[1, 2].set_ylabel('Suicide Rates (%)')
axis[1, 3].set_ylabel('Suicide Rates (%)')
axis[1, 4].set_ylabel('Suicide Rates (%)')

#plt.show()
plt.show() 
figure.savefig('Plots.png')

# Printing Intercept
print('Printing Intercepts')
print('Age 10-14: ', age_10_14_intercept)
print('Age 15-19: ', age_15_19_intercept)
print('Age 20-24: ', age_20_24_intercept)
print('Age 25-29: ', age_25_29_intercept)
print('Age 30-34: ', age_30_34_intercept)
print('Age 50-69: ', age_50_69_intercept)
print('Age 15-49: ', age_15_49_intercept)
print('Age 70+: ', age_70_up_intercept)
print('males: ', males_intercept)
print('females: ', females_intercept)

# Printing Coefficient 
print('\nPrinting Coefficients')
print('Age 10-14: ', age_10_14_coefficient)
print('Age 15-19: ', age_15_19_coefficient)
print('Age 20-24: ', age_20_24_coefficient)
print('Age 25-29: ', age_25_29_coefficient)
print('Age 30-34: ', age_30_34_coefficient)
print('Age 50-69: ', age_50_69_coefficient)
print('Age 15-49: ', age_15_49_coefficient)
print('Age 70+: ', age_70_up_coefficient)
print('males: ', males_coefficient)
print('females: ', females_coefficient)

