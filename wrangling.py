import numpy as np # Imports numpy into our project
import pandas as pd # Imports pandas into our project

data = pd.read_csv('data.csv') # reads our data file and saves it as a dataframe

"Part 1: Data Exploration"

def data_exploring():
    data.shape # Shows you the shape of your data, including the number of columns and rows
    data.info() # Shows us information about the data, including column names, data types, and the number of non null items
    data.head() # Shows us the first few items. Empty parameter shows the first five items
    data.tail(10) # Shows us the last 10 items based on the parameter we passed in

def statistical_exploration():   
    data.describe() # Shows us a high level statistical overlap of the data
    data.mean() # Shows us the average of all of the columns
    data['Longitude'].max() # Shows us the max value of a specific column that we passed in as a parameter

"Part 2: Select, Filter, Sort"

def indexing():
    data['FacilityType'][1] # Selects a specific column and row based off of the parameters that we have passed into the data
    data[['locationid', 'Applicant', 'FacilityType']] # Selects all the columns from a list of columns
    data.loc[4, "LocationDescription"] # Selects a specific row and column. Loc and Iloc are slightly more efficient

def filtering():
    data[data['Status'] == 'APPROVED'] # Uses booleans to filter in only the data that meets the condition of the parameter that we are passing in

def sorting():
    data.sort_index(inplace = True, axis = 1) # Sorts the data frame by the index. We sort by the column index and not the row index because the axis = 1 statement

"Part 3: Clean Data"

def missing_data():
    data.isnull().any() # Checks if a column has any nan values
    data.isnull().any(axis=1) # Checks if a row has any nan values using the axis parameter
    data[['dayshours', 'NOISent']].isnull().all(axis = 1) # Checks if a row has null values for both of these columns
    data.notnull().all() # Checks if every value in a column is not null
    data['Approved'].fillna('Not approved yet.', inplace=True) # Replaces the null values in the 'Approved' column with a string that we are passing in

def removing_data():
    data.drop(['NOISent', 'dayshours'], axis = 1, inplace=True) # Drops two columns per the parameters we are passing in
    data.duplicated().any() # Checks if we have any duplicate rows
    data.drop_duplicates() # Drops any duplicate rows

def fixing_indices():
    data.set_index('locationid', drop=True, inplace = True) # Changes our index to be the locationid column. 'Drop=true' drops the pre-existing locationid column

"Part 4: Transforming Data"

def grouping_data():
    g = data.groupby('Applicant') # Takes every value from our parameter column and makes a groupby object
    g.sum() # Does a mathmatic function on our groupby object
    # We can pass in multiple groupby parameters to create more in depth groupings.

def structural_transformations():
    data.stack() # This function moves all the data from the rows into a single column
    data.unstack() # Moves values from columns into rows
    data.pivot('index', 'column names', 'value') # This allows us to reshape our data structure into a pivot table based on the passed in parameters
    data.melt(id_vars = ['index']) # Combines data from rows into a single column, however it adds an additional column that shows where the data came from