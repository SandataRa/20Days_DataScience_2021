# First EDA Project Day12
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set_theme()

dataset = pd.read_csv("C:\\Users\\Sandratra\\Desktop\\Udemy Resources\\Employee Attrition and Performance\\dataset.csv")

dataset # nb lines = 1470 nb columns = 35 
dataset_subset = dataset[['EmployeeNumber', 'Age','Gender', 'Attrition','Department','DistanceFromHome','Education','EducationField',
                                 'StockOptionLevel', 'TotalWorkingYears', 'MonthlyIncome', 'NumCompaniesWorked',
                                 'PerformanceRating', 'TrainingTimesLastYear','WorkLifeBalance','YearsAtCompany',
                                 'YearsSinceLastPromotion', 'YearsWithCurrManager']]

dataset_subset.info()
# Transformation columns 
dataset_subset.Gender = dataset_subset.Gender.astype('category')
dataset_subset.Attrition = dataset_subset.Attrition.astype('category')
dataset_subset.Department = dataset_subset.Department.astype('category')
dataset_subset.Education = dataset_subset.Education.astype('category')
dataset_subset.EducationField = dataset_subset.EducationField.astype('category')
dataset_subset.StockOptionLevel = dataset_subset.StockOptionLevel.astype('category')
dataset_subset.PerformanceRating = dataset_subset.PerformanceRating.astype('category')
dataset_subset.WorkLifeBalance = dataset_subset.WorkLifeBalance.astype('category')

dataset_subset

# Uncover the factors that lead to employee attrition and explore important questions 
# Question 1: show me a breakdown of distance from home by job role and attrition 
# Question 2: compare average monthly income by education and attrition


# Filter only on the attrition part  
f1 = (dataset_subset.Attrition == 'Yes')

sns.set_style("darkgrid")
# Observing attrition for each slice of age comparing gender group for each departments 
ageFG1 = sns.FacetGrid(dataset_subset[f1] , row = 'Gender', col='Department', hue = 'Gender', height=3, aspect=1.5)
ageFG1 = ageFG1.map(plt.hist, 'Age')

plt.show()
# Observation1: The peak of attrition concerns mainly male employees between [25 - 35] years old working 
# in Research & Development department 

# Observing potential correlation between DistanceFromHome and YearsAtCompany 
density1 = sns.jointplot(data = dataset_subset, x='YearsAtCompany',y = 'DistanceFromHome', hue='Attrition', kind="hist",  height = 10)
plt.show()
# Observation2: The peak of attrition concerns recent employees (less than 10 years at the company) 
# living near the office, under 10 km but it also matches the number of observations of the dataset 


# Observing potential correlation between DistanceFromHome and YearsAtCompany on our subset of male employee from R&D
f2 = (dataset_subset.Attrition == 'Yes') & (dataset_subset.Gender == 'Male') & (dataset_subset.Department == 'Research & Development')

density2 = sns.jointplot(data = dataset_subset[f2], x='YearsAtCompany',y = 'DistanceFromHome', kind="hist",  height = 10, color = '#DD8452' )
plt.show()
# Observation 3: We confirm that employee under 10 years at the company tend to leave but the distance doesn't seem to be an
# explanation factor as we have attrition between 10 - 25 km as well as under 10 



