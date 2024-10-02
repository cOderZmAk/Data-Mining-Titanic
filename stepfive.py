#step 4 - adding statistics and graphs about the dataset.

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('titanic.csv')

#Basic Statistics
mean = data['fare'].mean()
std = data['fare'].std()

lower_bound = mean - 2 * std
upper_bound = mean + 2 * std

#IQR for FARE
Q1_fare = data['fare'].quantile(0.25)
Q3_fare = data['fare'].quantile(0.75)

IQR_fare = Q3_fare - Q1_fare

#IQR for AGE
Q1_age = data['age'].quantile(0.25)
Q3_age = data['age'].quantile(0.75)

IQR_age = Q3_age - Q1_age

#Outliers for age and fare
fare_lower_bound = Q1_fare - 1.5 * IQR_fare
fare_upper_bound = Q3_fare + 1.5 * IQR_fare

age_lower_bound = Q1_age - 1.5 * IQR_age
age_upper_bound = Q3_age + 1.5 * IQR_age

#Filtering fare values
filtered_data = data.loc[
    (data['fare'] >= lower_bound) & (data['fare'] <= upper_bound) &
    (data['age'] >= age_lower_bound) & (data['age'] <= age_upper_bound)
]
#Histogram Before 'fare' feature 
plt.subplot(1, 2, 1)
plt.hist(data['fare'], bins=30, density=True)
plt.title('Histogram without Fare')
plt.xlabel('Fare')
plt.ylabel('Probability')

#Boxplot Before 'fare' feature
plt.subplot(1, 2, 2)
data.boxplot(column=['fare'])
plt.title('Boxplot without fare')
plt.show()

#Histogram after 'fare' feature
plt.subplot(1, 2, 1)
plt.hist(filtered_data['fare'],  bins=30, density=True)
plt.title('Histogram with Fare')
plt.xlabel('Fare')
plt.ylabel('Probability')

#Boxplot after 'fare' feature
plt.subplot(1, 2, 2)
filtered_data.boxplot(column=['fare'])
plt.title('Boxplot with fare')
plt.show()

#Histogram Before 'age' feature 
plt.subplot(1, 2, 1)
plt.hist(data['age'], bins=30, density=True)
plt.title('Histogram without age')
plt.xlabel('age')
plt.ylabel('Probability')

#Boxplot Before 'age' feature
plt.subplot(1, 2, 2)
data.boxplot(column=['age'])
plt.title('Boxplot without age')
plt.show()

#Histogram after 'age' feature
plt.subplot(1, 2, 1)
plt.hist(filtered_data['age'],  bins=30, density=True)
plt.title('Histogram with age')
plt.xlabel('age')
plt.ylabel('Probability')

#Boxplot after 'age' feature
plt.subplot(1, 2, 2)
filtered_data.boxplot(column=['age'])
plt.title('Boxplot with age')
plt.show()


print(f'Mean: {mean}')
print(f'Standard Deviation: {std}')
print(f'Lower Bound: {lower_bound}')
print(f'Upper Bound: {upper_bound}')

print(f'IQR for fare: {IQR_fare}')
print(f'Fare Lower Bound: {fare_lower_bound}')
print(f'Fare Upper Bound: {fare_upper_bound}')
print(f'IQR for age: {IQR_age}')
print(f'Age Lower Bound: {age_lower_bound}')
print(f'Age Upper Bound: {age_upper_bound}')