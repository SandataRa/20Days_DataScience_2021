# Day 13

# Breakdown of distance from home by job role and attrition
plt.rcParams['figure.figsize'] = 20,8

distance_role_breakdown = sns.boxplot(data = dataset_subset, x="JobRole", y="DistanceFromHome", palette = "Accent")
distance_role_breakdown = sns.stripplot(data= dataset_subset , x="JobRole", y="DistanceFromHome", jitter = True,
                     hue = 'Attrition', palette = 'inferno')
# Styling the plot
sns.set_style("white")
plt.legend(prop={'size':15} , loc='upper left', bbox_to_anchor=(1,1), frameon = True)
plt.ylabel("Distance from home", fontsize = 20, color = "Black")
plt.xlabel("Job Role", fontsize = 20, color = "Black")
plt.yticks(fontsize = 15)
plt.xticks(range(9), ["Sales \n Executive","Research \n Scientist","Laboratory \n Technician", "Manufacturing \n Director",
                     "Healthcare \n Representative", "Manager","Sales \n Representative", "Research \n Director",
                      "Human \n Resources"], fontsize = 15)
plt.title("Breakdown of distance from home by job role and attrition", fontsize = 26, color="Black", fontname = "Arial")
plt.show()

# Why male employee from R&D are more susceptible to leave the company? 
# Let's analyze in further details the male employees of the Research & Development department 

males_rd_subset = dataset[['EmployeeNumber', 'Age','Gender', 'Attrition', 'Department', 'DistanceFromHome',
                           'EnvironmentSatisfaction', 'JobInvolvement', 'JobRole','JobSatisfaction', 'MonthlyIncome',
                           'MonthlyRate', 'OverTime', 'PerformanceRating', 'RelationshipSatisfaction', 'TrainingTimesLastYear',
                           'WorkLifeBalance']]

f3 = (dataset_subset.Gender == 'Male') & (dataset_subset.Department == 'Research & Development')

# Columns transformations
males_rd_subset[f3].Gender = males_rd_subset[f3].Gender.astype('category')
males_rd_subset[f3].Attrition = males_rd_subset[f3].Attrition.astype('category')
males_rd_subset[f3].Department = males_rd_subset[f3].Department.astype('category')
males_rd_subset[f3].EnvironmentSatisfaction = males_rd_subset[f3].EnvironmentSatisfaction.astype('category')
males_rd_subset[f3].JobInvolvement = males_rd_subset[f3].JobInvolvement.astype('category')
males_rd_subset[f3].JobRole = males_rd_subset[f3].JobRole.astype('category')
males_rd_subset[f3].JobSatisfaction = males_rd_subset[f3].JobSatisfaction.astype('category')
males_rd_subset[f3].OverTime = males_rd_subset[f3].OverTime.astype('category')
males_rd_subset[f3].PerformanceRating = males_rd_subset[f3].PerformanceRating.astype('category')
males_rd_subset[f3].RelationshipSatisfaction = males_rd_subset[f3].RelationshipSatisfaction.astype('category')
males_rd_subset[f3].WorkLifeBalance = males_rd_subset[f3].WorkLifeBalance.astype('category')

# Distribution of Monthly income by Job Role among men of Research & Development department
income_job = sns.violinplot(data = males_rd_subset[f3], x = 'JobRole', y = 'MonthlyIncome')

# Styling the plot
sns.set_style("white")
plt.ylabel("Distance from home", fontsize = 20, color = "Black")
plt.xlabel("Job Role", fontsize = 20, color = "Black")
plt.yticks(fontsize = 15)
plt.xticks(fontsize = 15)
plt.title("Monthly income by Role among men of Research & Development department", fontsize = 20, color="Black", fontname = "Arial")
plt.show()