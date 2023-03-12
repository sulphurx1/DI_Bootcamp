# Question 1
# Write a function to create a numpy array using only the input: start, length, and stop. Use the function to create an numpy array of length 100, starting from 6 and has a step of 4 between consecutive numbers
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

arr = np.arange(6,((100 * 4) + 6) , 4)
# print(arr)

# Question 2
# Drop all nan values from the following numpy array.
a = np.array([1,2,3,np.nan,5,6,7,np.nan])
a = a[~np.isnan(a)]
# print(a)

# Question 3
# create a random numpy array that has a shape of (5, 6) filled with integers between 1 and 100.
arr1 = np.random.randint(1, 101, size=(5,6))
# print(arr1)

# Then compute the maximum int for each row in the array
max_per_row = np.amax(arr1, axis=1)
# print(max_per_row)

# Question 4
# use a pandas Series function to find the unique values and their frequencies of the following Series:
# series = pd.Series(np.take(list('abcdefghijklmnop'), np.random.randint(16, size=500)))
# x = series.unique()
# print(x)

# Question 5
# Get the day of month, week number, day of year and day of week from this pandas series
series = pd.Series(['01 Jan 2020', '10-19-2020', '20150303', '2013/04/04', '2012-05-05', '2013-06-06T12:20'])
index_date = pd.to_datetime(series)

# day of the month
day_of_month = index_date.dt.day
print(day_of_month)

# week number
week_number = index_date.dt.week
print(week_number)

# day of year
day_of_year = index_date.dt.dayofyear
print(day_of_year)

# day of week
day_of_week = index_date.dt.day_of_week
print(day_of_week)


# Question 6
# Read the data
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

# print how many columns are of each datatype.
print(df.shape)

# Change the column name “Type” to “TypeOfCar” and print the head of the dataframe
df = df.rename(columns={'Type': 'TypeOfCar'})
print(df.info)

# How many values are missing from each of the columns?
missing_values = df.isnull().sum()
print(missing_values)

# Which columns has the most missing values? (answer with code, without sorting)
max_missing_values = missing_values.max()
column_max_missing_values = missing_values[missing_values == max_missing_values].index
print(column_max_missing_values)

# Delete the columns: “EngineSize” and “Length” in 2 different ways. Check (with code) that these columns are indeed gone.
df.drop('EngineSize', axis=1, inplace=True)

del df['Length']

# Question 8
# Join the following two dataframes by two columns, so they have only the common rows.

df1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                    'weight': ['high', 'medium', 'low'] * 3,
                    'price': np.random.randint(0, 15, 9)})

df2 = pd.DataFrame({'pazham': ['apple', 'orange', 'pine'] * 2,
                    'kilo': ['high', 'low'] * 3,
                    'price': np.random.randint(0, 15, 6)}) 
merged_df = pd.merge(df1, df2, left_on=['fruit', 'weight'], right_on=['pazham', 'kilo'])
print(merged_df)

# Remove duplicate columns (meaning that all values are the same) to keep only one.

duplicate_columns = merged_df.columns[merged_df.T.duplicated()].tolist()
print(duplicate_columns)
merged_df = merged_df.drop(columns=duplicate_columns)
print(merged_df)

# Question 9

# Split this dataframe with a string column to form a dataframe with 3 columns named “STD”, “City”, and “State.”

df3 = pd.DataFrame(["STD,City\tState",
"33,Kolkata\tWest Bengal",
"44,Chennai\tTamil Nadu",
"40,Hyderabad\tTelengana",
"80,Bangalore\tKarnataka"], columns=['row'])

df3 = df3['row'].str.split(',', expand=True)

df3[['STD', 'City']] = df3[1].str.split('\t', expand=True)
print(df3)
df3 = df3.drop(columns=1)
print(df3)
df3 = df3.rename(columns={0: 'STD'})
print(df3)

# Question 10
# Create a function called scatter_plot that takes the dataframe df and plots the relationship between the following two features: displacement over x-axis, acceleration over y-axis
filename = "auto-mpg.data"
filepath = "./" + filename
names = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin", "car_name"]
df_mpg = pd.read_csv(filepath, header=None, names=names, delim_whitespace=True)

x = df_mpg['displacement']
y = df_mpg['acceleration']

# plt.scatter(x, y)
# plt.xlabel('Displacement')
# plt.ylabel('Acceleration')
# plt.title('Scatter Plot of Displacement vs. Acceleration')
# plt.show()

# Question 11
# Create a function bar_plot that takes the dataframe df and compares the cylinders of all the cars from 1978 model_year and toyota company
# filtered_df = df_mpg[(df_mpg['model_year'] == 78)]
# filtered_df = filtered_df[filtered_df['car_name'].str.contains('toyota')]
# cylinder_count = filtered_df.groupby('cylinders').size()
# print(cylinder_count)

# fig, ax = plt.subplots()
# ax.bar(cylinder_count.index, cylinder_count.values, width=0.5, edgecolor='black', linewidth=0.5)
# ax.set_xlabel('Cylinders')
# ax.set_ylabel('Count')
# ax.set_title('Cylinder Count for 1978 Toyota Cars')
# plt.show()

# Question 12
# Create a function line_plot that takes the dataframe df and plots the change in weight throughout the years for the cars of toyota company.
df_toyota = df_mpg[df_mpg['car_name'].str.contains('toyota')]

grouped = df_toyota.groupby('model_year')['weight'].mean()
# ax = plt.subplot()
# ax.plot(grouped.index, grouped.values)
# ax.set_xlabel('Year')
# ax.set_ylabel('Weight')
# ax.set_title('Change in Weight of Toyota Cars over Time')
# plt.show()
# print(grouped)

# Question 13
fig, ax = plt.subplots(figsize=(8, 6))
colors = df_mpg['cylinders']
scatter = ax.scatter(df_mpg['displacement'], df_mpg['mpg'], c=colors, cmap='viridis')
ax.set_xlabel('Engine Displacement (L)')
ax.set_ylabel('Miles per Gallon (mpg)')
ax.set_title('Engine Displacement vs. Fuel Efficiency (1970-1982)')
ax.grid(True)
plt.colorbar(scatter)
plt.show()