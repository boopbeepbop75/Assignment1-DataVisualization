import pandas as pd
import os
import Data_Cleanup
import matplotlib.pyplot as plt
import seaborn as sns

# Specify the file name or path
file_path = 'CsAssignment1/Normalized_Student_Performance_Data.csv'

# Check if the file exists
if os.path.exists(file_path):
    print(f"The file '{file_path}' exists already.")
else:
    print(f"Cleaning Data...")
    Data_Cleanup.clean_data()


#Data was gathered from assignment 1 box, stored in this folder under the file name 'StudentsPerformanceAssignment1Dataset.csv'
StudentPerformanceData = pd.read_csv('CsAssignment1/Normalized_Student_Performance_Data.csv')

# Checking the data
print("Showing Data Head\n--------------------")
print(StudentPerformanceData.head())

#########VISUALIZING THE DATA############
plt.figure(figsize=(10, 6))
plt.scatter(StudentPerformanceData['math score'], StudentPerformanceData['reading score'], alpha=0.5)
plt.title('Math Scores vs. Reading Scores')
plt.xlabel('Math Score')
plt.ylabel('Reading Score')
plt.show()
'''This plot helps us understand the data by showing the scores on math vs reading. 
In this plot it looks like a fairly linear improvement bar between the two, hinting at some correlation'''

par_edu_map = {'some high school': 0, 'high school': 1, 'some college': 2, 'some college': 3, 'associate\'s degree': 4, 'bachelor\'s degree': 5, 'master\'s degree': 6}
plt.figure(figsize=(12, 6))
StudentPerformanceData.groupby('parental_education')[['math score', 'reading score', 'writing score']].mean().plot(kind='bar')
plt.title('Average Scores by Parental Education Level')
plt.xlabel('Parental Education Level')
plt.ylabel('Average Score')
plt.legend(title='Subject')
plt.xticks(rotation=45)
plt.show()
'''This plot helps us visualize how the parents education might impact the students. 
I organized more education as higher numbers on the X-Plot
This shows some carrelation of better parent score = better student score'''

test_prep_map = {'none': 0, 'completed': 1}
plt.figure(figsize=(12, 6))
StudentPerformanceData.melt(id_vars=['test_prep'], value_vars=['math score', 'reading score', 'writing score'], var_name='Subject', value_name='Score').pipe(
    (sns.boxplot, 'data'), x='Subject', y='Score', hue='test_prep')
plt.title('Score Distribution by Test Preparation')
plt.show()
'''This plot helps us find a correlation between how taking a test prep course influences the scores
It seems to indicate that student that HAVE completed the test prep (labeled 1) tend to score better'''

plt.figure(figsize=(10, 8))
correlation_matrix = StudentPerformanceData[['math score', 'reading score', 'writing score', 'parental_education']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0)
plt.title('Correlation Heatmap of Scores and Parental Education')
plt.show()
'''This heatmap helps to show some correlation between how the students scored on the different tests, 
as well as how much the parent scores may have an effect on it.
It seems like the parent score doesn't have a high correlation to how the students score compared to
how they scored on each test. 
May indicate that the students scores depend more on their overall study habits rather than parent influence?'''

gender_map = {'male': 1, 'female': 0}
lunch_map = {'standard': 0, 'free/reduced': 1}
# Create the grouped bar plot

# Assuming df is your DataFrame
melted_df = StudentPerformanceData.melt(id_vars=['lunch'], 
                    value_vars=['math score', 'reading score', 'writing score'], 
                    var_name='Subject', value_name='Score')

# Create the box plot
plt.figure(figsize=(12, 6))
ax = sns.boxplot(x='Subject', y='Score', hue='lunch', data=melted_df, palette='Set3')

plt.title('Score Distribution by Subject and Lunch Type', fontsize=16)
plt.xlabel('Subject', fontsize=12)
plt.ylabel('Score', fontsize=12)

# Correct the legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, ['Standard', 'Free/Reduced'], title='Lunch Type')

plt.tight_layout()
plt.show()
'''This plot helps show the correlation between the type of lunch the students got and how they scored
The plot seems to indicate that students who got the standard lunch scored better than those who 
got the free or reduced lunch.'''