#!/usr/bin/env python
# coding: utf-8

# # *FOR ITEM A*
# # Converting the Dataset .txt to .csv:
# 
# There are several methods to convert a text file (.txt) to Comma Seperated Values (.csv):
# 
# 1. The easiest method is to manually rename the extension of the target text file from .txt to .csv - providing the data are already formatted in the CSV format.
# 
# 2. Secondly, on Macs with the application 'Numbers' (the MacOS native spreadsheet app), the dataset file can be opened directly from Finder using 'Open With...'. This method is slightly lengthier than simply renaming the file extension, but the .txt file (if correctly formatted) will automatically be arranged in tabular form with columns delienated by commas. The file can then be 'Save As...' and change the extension from .txt to .csv
# 
# 3. Thirdly, by using Microsoft Excel on any platforms supporting it natively. We do this by opening the Excel application and start by creating a new spreadsheet. On the 'Data' tab, the .txt file is opened by selecting 'Get External Data' and 'From Text' options. An Import Wizard screen will be shown where detailed options with regards to handling the data can be selected. Once applicable options have been modified, clicking 'Finish' will terminate the Import Wizard and open the .txt file according to set parameters. The spreadsheet can then be saved as a .csv file from the main menu.
# 
# 4. Finally, there are many free online tools available that could automatically convert .txt files to .csv, although using this method is not recommended in most cases as their authenticity could not always be determined.

# In[4]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# *FOR ITEM B*
## Opening .csv dataset in Jupyter Notebook:
df = pd.read_csv('Data Files/horse-colic.csv', header=None)

# *FOR ITEM C AND D*
## Replacing missing values with NaN, then saving as new .csv file:
df.replace('?', np.nan, inplace=True)
df.to_csv('Data Files/horse-colic-with-NaN.csv', header=None, index=False)

# *FOR ITEM E ANG F*
## Rename the column headers, then saving the edited Dataframe as new .csv file:
column_names = ['Surgery','Age','Hosp No','Rect Temp','Heart Rate','Respi Rate','Ext Temp','Peri Pulse',
                'Mucosa','CRT','Pain','Peristalsis','Abdo Dist','NG Tube','NG Ref Vol','NG Ref pH','Feces Amt',
                'Int Feces','PCV','Proteins','Ab_cen App','Ab_cen Prt','Outcome','Les_Exist','Les_Site',
                'Les_Type','Les_Sub','Les_Code','Path_Data']

df = pd.read_csv('Data Files/horse-colic-with-NaN.csv', header=None, names=column_names)
df.to_csv('Data Files/horse-colic-with-title.csv', index=False)

# *FOR ITEM G*
## Loading the .csv file and displaying the NaN values:
dfnan = df.isnull().sum()
print('Number of NaN values of each column:\n')
print(dfnan,'\n')

# *FOR ITEM H*
## Plotting the NaN values of each column on a bar chart. Matplotlib Pyplot is imported:
dfnan.plot(kind='bar', color='blue')
plt.title('Missing Values for Each Column')
plt.ylabel('Number of Missing Values')

# *FOR ITEM I*
## Displaying data types for column values in the Dataset:
print('Data types of each column:\n')
print(df.dtypes,'\n')

# *TESTING EXTRAS*
dfnan2 = df.drop(df.columns[-1:],axis=1)
print('Total Number of NaN in Dataset:')
print(dfnan2.isnull().sum().sum())
df.shape


# # *FOR ITEM J*
# # Dropping NaN values?
# 
# With regards to the NaN values found in the DataFrame, the decision to delete/remove NaN rows will depend on several factors:
# 
# 1. If the intention is to delete ALL rows containing NaN values, this will result in deletion of the whole dataset, considering the column 'Pathology Data' consists of rows which are entirely NaN. Even excluding Pathology Data (since it was mentioned that none were actually collected and hence the column is not significant), some columns (e.g. Nasogastric Tube Reflux pH' and Abdominocentesis Protein') have majority of their rows consisting of NaN values. Removing all rows with NaN significantly shrinks the sample size of the dataset.
# 
# 2. However, if the intention is to remove only the NaN rows of each column individually

# 

# In[5]:


from numpy import isnan
from pandas import read_csv
from sklearn.impute import SimpleImputer

# Import the original dataset in the CSV format into Pandas DataFrame, defined as df
# Specify argument 'header=None' to prevent the first row from being converted to the Header during import
df = pd.read_csv('Data Files/horse-colic.csv', header=None)

# Replace the missing values represented with '?' in the DataFrame to 'NaN' (np.nan)
# Save the updated DataFrame to a new CSV file, with argument 'index=False' to remove the Index column
df.replace('?', np.nan, inplace=True)
df.to_csv('Data Files/horse-colic-project.csv', index=False)

# Assign meaningful and identifiable names to column to the list 'column_names'
# Import the updated CVS file and append the column names using argument 'names=column_names'
# Drop the column 'Path_Data' as it does not contain any value (all NaN)
column_names = ['Surgery','Age','Hosp No','Rect Temp','Heart Rate','Respi Rate','Ext Temp','Peri Pulse',
                'Mucosa','CRT','Pain','Peristalsis','Abdo Dist','NG Tube','NG Ref Vol','NG Ref pH','Feces Amt',
                'Int Feces','PCV','Proteins','Ab_cen App','Ab_cen Prt','Outcome','Les_Exist','Les_Site',
                'Les_Type','Les_Sub','Les_Code']

dataframe = pd.read_csv('Data Files/horse-colic-project.csv', header=None, names=column_names)

# Create an array where each column is represented by a set, and its row values as contents of the sets
data = dataframe.values

# Get the total number of columns in the DataFrame, by specifiying data.shape[1] (columns) instead of
# data.shape[0], which will list rows.
# Declare 'ix' variable as the list of all column except Column 23 which is 'Outcome'
# Declare 'X' as all the values in the DataFrame except for Column 23
# Declare 'y' as all the values in Column 23
totalCol = data.shape[1]
ix = [i for i in range(totalCol) if i != 23]
X = data[:, ix]
y = data[:, 23]

# Print the number of the missing values in the DataFrame. First, the data is flattened into one-dimension
# using flatten(), then the NaN values within the data is identified with isnan(X).
# Then, the sum of NaN values is obtained with sum()
# The result is subsequently printed
print('Missing: %d' % sum(isnan(X).flatten()))

# Use an imputer as a 
# With SimpleImputer using the strategy='mean', the NaN values are replace with the mean value of each column
# the NaN exists in
imputer = SimpleImputer(strategy='mean')
# <to code>
imputer.fit(X)
Xtrans = imputer.transform(X)

# <to code>
print('Missing: %d' % sum(isnan(Xtrans).flatten()))


# In[ ]:





# In[ ]:




