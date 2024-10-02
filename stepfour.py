#step 4 - adding statistics and graphs about the dataset.

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('titanic.csv')

#Basic Statistics
mean = data['fare'].mean()
std = data['fare'].std()

lower_bound = mean - 2 * std

upper_bound = mean + 2 * std


#Filtering fare values
filtered_data = data.loc[(data['fare'] >= lower_bound) & (data['fare'] <= upper_bound)]

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


print(f'Mean: {mean}')
print(f'Standard Deviation: {std}')
print(f'Lower Bound: {lower_bound}')
print(f'Upper Bound: {upper_bound}')