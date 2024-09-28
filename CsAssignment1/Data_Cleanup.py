import pandas as pd
from scipy import stats
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import numpy as np

def clean_data():
    #Data was gathered from assignment 1 box, stored in this folder under the file name 'StudentsPerformanceAssignment1Dataset.csv'
    StudentPerformanceData = pd.read_csv('CsAssignment1/StudentsPerformanceAssignment1Dataset.csv')

    # Checking the data
    print("Showing Data Head\n--------------------")
    print(StudentPerformanceData.head())

    # Overview
    print("\nData Info\n--------------------")
    print(StudentPerformanceData.info())

    # Data Stats
    print("\nShowing Data statistics:\n--------------------")
    print(StudentPerformanceData.describe())

    #Drop Unnecessary Columns:
    # Drop a single column
    StudentPerformanceData = StudentPerformanceData.drop('race/ethnicity', axis=1) #Irrelevant to problem

    # Find missing values in each column
    missing_values = StudentPerformanceData.isnull().sum()
    print(missing_values)

    # % of missing values
    missing_percentage = (StudentPerformanceData.isnull().sum() / len(StudentPerformanceData)) * 100
    print(missing_percentage)

    # Drop rows with any missing values
    StudentPerformanceData = StudentPerformanceData.dropna()

    # Drop columns with any missing values
    StudentPerformanceData = StudentPerformanceData.dropna(axis=1)


    # Find any duplicate rows
    duplicates = StudentPerformanceData.duplicated()
    print(f"Number of duplicate data: {duplicates.sum()}") 

    # Drop duplicate rows
    if len(duplicates) > 0:
        StudentPerformanceData = StudentPerformanceData.drop_duplicates() 

    # Convert categorical columns to numeric data
        
    #rename education column
    StudentPerformanceData = StudentPerformanceData.rename(columns={'parental level of education': 'parental_education', 'test preparation course': 'test_prep'})

    # Map categorical values manually
    gender_map = {'male': 1, 'female': 0}
    test_prep_map = {'none': 0, 'completed': 1}
    lunch_map = {'standard': 0, 'free/reduced': 1}
    StudentPerformanceData['gender'] = StudentPerformanceData['gender'].map(gender_map)
    StudentPerformanceData['test_prep'] = StudentPerformanceData['test_prep'].map(test_prep_map)
    StudentPerformanceData['lunch'] = StudentPerformanceData['lunch'].map(lunch_map)

    #rename education column
    StudentPerformanceData = StudentPerformanceData.rename(columns={'parental level of education': 'parental_education'})

    print(set(StudentPerformanceData['parental_education']))
    par_edu_map = {'some high school': 0, 'high school': 1, 'some college': 2, 'some college': 3, 'associate\'s degree': 4, 'bachelor\'s degree': 5, 'master\'s degree': 6}

    StudentPerformanceData['parental_education'] = StudentPerformanceData['parental_education'].map(par_edu_map)

    # Normalize dataframe
    scaler = MinMaxScaler()
    data_normalized = scaler.fit_transform(StudentPerformanceData)

    StudentPerformanceData = pd.DataFrame(data_normalized, columns=StudentPerformanceData.columns)

    print(StudentPerformanceData)

    StudentPerformanceData.to_csv('CsAssignment1/Normalized_Student_Performance_Data.csv', index=False)