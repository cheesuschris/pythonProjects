import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#features, test, and train are all included in the path directory under a folder called SIFQuantAnalysis
features_path = 'features.xlsx'
test_path = 'test.xlsx'
train_path = 'train.xlsx'

# Since the files are named features and test, let's load them into pandas dataframes.
features_df = pd.read_excel(features_path)
test_df = pd.read_excel(test_path)
train_df = pd.read_excel(train_path)

#What we're looking for
#Data quality: Missing data, duplicates, and data types.
#Distributions: The spread of the data (e.g., mean, median, variance, skewness).
#Relationships: Correlations and interactions between variables.
#Outliers and anomalies: Unusual data points.
#Patterns and trends: Especially in time series or continuous data.
#Hypotheses: Generate questions for further analysis or modeling.
#Feature selection: Identify which variables are important for downstream analysis.

# Display the first few rows of both dataframes to understand their structure.
print("-----------------------------------------------------------------------------------------------------------------\nHead\n-----------------------------------------------------------------------------------------------------------------\n")
print("\nFeatures Head\n")
print(features_df.head())
print("\nTest Head\n")
print(test_df.head())
print("\nTrain Head\n")
print(train_df.head())
#Display the data types, non-null counts
print("-----------------------------------------------------------------------------------------------------------------\nInfo\n-----------------------------------------------------------------------------------------------------------------\n")
print("\nFeatures Info\n")
print(features_df.info())
print("\nTest Info\n")
print(test_df.info())
print("\nTrain Info\n")
print(train_df.info())
#Display the summary statistics
print("-----------------------------------------------------------------------------------------------------------------\nSummary Statistics\n-----------------------------------------------------------------------------------------------------------------\n")
print("\nFeatures Summary Statistics\n")
print(features_df.describe())
print("\nTest Summary Statistics\n")
print(test_df.describe())
print("\nTrain Summary Statistics\n")
print(train_df.describe())
#Check for missing values
print("-----------------------------------------------------------------------------------------------------------------\nMissing Values\n-----------------------------------------------------------------------------------------------------------------\n");
print("\nFeatures Missing Values\n")
print(features_df.isnull().sum())
print("\nTest Missing Values\n")
print(test_df.isnull().sum())
print("\nTrain Missing Values\n")
print(train_df.isnull().sum())

#Changed for every plot I did, and every variable I tested
plt.plot(features_df['IsHoliday'], features_df['CPI'])
plt.xlabel('IsHoliday')
plt.ylabel('CPI')
plt.title('Line Plot of IsHoliday vs CPI')
plt.show()

