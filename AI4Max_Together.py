import pandas as pd
import numpy as np 
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns

## Importing the data files 
df = pd.read_excel("df.xlsx") 

# Setting up multiple linear regression model
y = np.array(df['Suicide rate (deaths per 100,000 individuals)'].values)
x = np.array(df[['20-24 years old (%)', '10-14 years old (%)', '15-19 years old (%)', '30-34 years old (%)', '25-29 years old (%)', '50-69 years old (%)', '15-49 years old (%)', '70+ years old (%)', 'Prevalence in males (%)', 'Prevalence in females (%)']].values)

# Creating Model 
x_model = LinearRegression()

# fitting data to model
x_model.fit(x,y)

# Predicting from model 
x_model_pred = x_model.predict(x)

# Getting Intercept
x_intercept = x_model.intercept_

# Getting Coefficient 
x_coefficient = x_model.coef_

# Plotting the models
fig = plt.figure(figsize=(16,9))
sns.regplot(x=df['20-24 years old (%)'], y=df['Suicide rate (deaths per 100,000 individuals)'], color='blue', marker='+')
sns.regplot(x=df['10-14 years old (%)'], y=df['Suicide rate (deaths per 100,000 individuals)'], color='red', marker='+')
sns.regplot(x=df['15-19 years old (%)'], y=df['Suicide rate (deaths per 100,000 individuals)'], color='yellow', marker='+')
sns.regplot(x=df['30-34 years old (%)'], y=df['Suicide rate (deaths per 100,000 individuals)'], color='green', marker='+')
sns.regplot(x=df['25-29 years old (%)'], y=df['Suicide rate (deaths per 100,000 individuals)'], color='purple', marker='+')
sns.regplot(x=df['50-69 years old (%)'], y=df['Suicide rate (deaths per 100,000 individuals)'], color='orange', marker='+')
sns.regplot(x=df['15-49 years old (%)'], y=df['Suicide rate (deaths per 100,000 individuals)'], color='brown', marker='+')
sns.regplot(x=df['70+ years old (%)'], y=df['Suicide rate (deaths per 100,000 individuals)'], color='cyan', marker='+')
sns.regplot(x=df['Prevalence in males (%)'], y=df['Suicide rate (deaths per 100,000 individuals)'], color='olive', marker='+')
sns.regplot(x=df['Prevalence in females (%)'], y=df['Suicide rate (deaths per 100,000 individuals)'], color='magenta', marker='+')

plt.legend(labels=['20-24 years old (%)', '10-14 years old (%)', '15-19 years old (%)', '30-34 years old (%)', '25-29 years old (%)', '50-69 years old (%)', '15-49 years old (%)', '70+ years old (%)', 'Prevalence in males (%)', 'Prevalence in females (%)'], title='Legend', bbox_to_anchor=(1.05, 1), fontsize='xx-small')
plt.title('Factors in Relation to Suicide')
plt.xlabel('Percentage of Population')
plt.ylabel('Suicide Rates (% of population with depressive symptoms)')

#Saving figure
fig.savefig('Model.png')

# Printing Intercept
print('Printing Intercepts')
print('x Factor: ', x_intercept)

# Printing Coefficient 
print('\nPrinting Coefficients')
print('x Factor: ', x_coefficient)
