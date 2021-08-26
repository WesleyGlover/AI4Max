import pandas as pd

## Importing the data files 
#education = pd.read_excel("depression-by-level-of-educatio.xlsx", index_col="Entity") #----- Ready to be used -----
age = pd.read_excel("prevalence-of-depression-by-age.xlsx", index_col="Entity") #----- Ready to be used -----
gender = pd.read_excel("prevalence-of-depression-males-.xlsx", index_col='Entity') #----- Ready to be used -----
suicide = pd.read_excel("suicide-rates-vs-prevalence-of-.xlsx", index_col='Entity') #----- Ready to be used -----
depression_population = pd.read_excel("number-with-depression-by-count.xlsx", index_col='Entity') #----- Ready to be used -----
mental = pd.read_excel("prevalence-by-mental-and-substa.xlsx", index_col='Entity') #----- Ready to be used -----

## Checks to make sure everything is working
print("Manipulating Files")
# print(education)
# print(age)
# print(gender)
# print(suicide)
# print(depression_population)
# print(mental)

# Cleaning up education dataframe to be used
#education.drop(['Code'], axis=1, inplace=True)
#education = education.loc[['Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Malta', 'Moldova', 'Montenegro', 'Netherlands', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Ukraine', 'United Kingdom']] 
#print(education) # <-------------------- This is the Education Data ready to be used. Does not Have Years Accosiated with it

# Cleaning up Age dataframe to be used 
age.drop(['Code'], axis=1, inplace=True)
age = age.loc[['Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Malta', 'Moldova', 'Montenegro', 'Netherlands', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Ukraine', 'United Kingdom']]
#print(age) # <------------------- Age is Age Ready.

#Cleaning up Gender to be used
gender.drop(['Code', 'Population'], axis=1, inplace=True)
genderuk = gender.loc[['Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Malta', 'Moldova', 'Montenegro', 'Netherlands', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Ukraine', 'United Kingdom']]
gender = genderuk.loc[(genderuk['Year'] >= 1990) & (genderuk['Year'] < 2018)]
#print(gender) # < ---------------- Gender is Ready.

#Cleaning up Suicide 
suicide.drop(['Code', 'Population'], axis=1, inplace=True)
suicideuk = suicide.loc[['Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Malta', 'Moldova', 'Montenegro', 'Netherlands', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Ukraine', 'United Kingdom']]
suicide = suicideuk.loc[(suicideuk['Year'] >= 1990) & (suicideuk['Year'] < 2018)]
#print(suicide) # <--------------- Suicide is Ready.

#Cleaninig up depression_population
depression_population.drop(['Code'], axis=1, inplace=True)
depression_populationuk = depression_population.loc[['Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Malta', 'Moldova', 'Montenegro', 'Netherlands', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Ukraine', 'United Kingdom']]
depression_population = depression_populationuk.loc[(depression_populationuk['Year'] >= 1990) & (depression_populationuk['Year'] < 2018)]
#print(depression_population) # <-------------- depression_population is Ready.

#Cleaning up mental 
mental.drop(['Code'], axis=1, inplace=True)
mentaluk = mental.loc[['Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Malta', 'Moldova', 'Montenegro', 'Netherlands', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Ukraine', 'United Kingdom']]
mental = mentaluk.loc[(mentaluk['Year'] >= 1990) & (mentaluk['Year'] < 2018)]
#print(mental) # <----------------- Mental is Ready.

#Placing data into its own file to be used in the linear regression model 
#education.to_excel("UK_Education.xlsx")
#age.to_excel('UK_Age.xlsx')
#gender.to_excel('UK_Gender.xlsx')
#suicide.to_excel('EU_Suicide.xlsx')
#depression_population.to_excel('UK_Depression.xlsx')
#mental.to_excel('UK_Mental.xlsx')

df = pd.concat([mental, depression_population, suicide, gender, age], axis=1, sort=True)
df.to_excel('df.xlsx')

print('Files Saved Sucessfully')

