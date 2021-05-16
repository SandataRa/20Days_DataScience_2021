#Day 14

#Compare average monthly income by education and attrition
education_income_means = dataset_subset.groupby('EducationField').MonthlyIncome.mean()
mean_dict = education_income_means.to_dict()

dataset_subset['FieldMonthlyIncomeMean'] = dataset_subset['EducationField'].map(mean_dict)
dataset_subset['FieldMonthlyIncomeMean'] = pd.to_numeric(dataset_subset['FieldMonthlyIncomeMean'])
dataset_subset.info()

plt.rcParams['figure.figsize'] = 20,8

income_educationField = sns.boxplot(data = dataset_subset, x="EducationField", y="FieldMonthlyIncomeMean", palette = "Accent")
income_educationField = sns.stripplot(data= dataset_subset , x="EducationField", y="MonthlyIncome", jitter = True,
                     hue = 'Attrition', palette = 'inferno')
# Styling the plot
sns.set_style("dark", {"axes.facecolor": "lightgrey"})
plt.ylabel("MonthlyIncome", fontsize = 20, color = "Black")
plt.xlabel("Education Field", fontsize = 20, color = "Black")
plt.yticks(fontsize = 15)
plt.xticks(fontsize = 15)
plt.title("Scatterplot of Monthly Income by Education Field's mean", fontsize = 26, color="Black", fontname = "Arial")
plt.show() 

"""
Most of the employees who left the company were paid under the average monthly income of their Education Field. So we can suppose that Monthly
Income can be a cause of attrition among the employees who have a Life Sciences, Medical or Technical Degree.
"""
# Is the number of years since the last promotion a reason for attrition? 
sns.set_style("darkgrid")
yearsAtCompany_promotion = sns.lmplot(data = dataset_subset, x = 'YearsAtCompany', y = 'YearsSinceLastPromotion', \
               fit_reg = False, hue = 'Attrition',height = 5, aspect = 1, markers=["x", "o"])
# Styling the plot
plt.ylabel("Years since last promotion", fontsize = 15, color = "Black")
plt.xlabel("Years at company", fontsize = 15, color = "Black")
plt.yticks(fontsize = 10)
plt.xticks(fontsize = 10)
plt.title("Relation between Promotion and Years at company", fontsize = 20, color="Black", fontname = "Arial")

plt.show() 
"""
The promotion doesn't seem to be a reason for attrition because we can observe that the cluster of attrition concerns employees
who recently received a promotion as well as employees who joined the company for less than 5 years. Therefore, we can conclude
that recent employees tend to leave the company. 
"""
# Confirming the relation between Promotion and Years at company with a KDE 
attrition_on = (dataset_subset.Attrition == 'Yes')

# Dashboard about the Promotion vs Years at the company 
sns.set_style("darkgrid")
f, axes = plt.subplots(1,2, figsize = (15,6), sharex = True, sharey = True)

kde_yp_at = sns.kdeplot(x = dataset_subset[attrition_on].YearsAtCompany, y = dataset_subset[attrition_on].YearsSinceLastPromotion, \
                 shade = True, cmap = 'flare', ax = axes[0])
kde_yp_at_shape = sns.kdeplot(x = dataset_subset[attrition_on].YearsAtCompany, y = dataset_subset[attrition_on].YearsSinceLastPromotion, \
                  cmap = 'hot', ax = axes[0]) 
axes[0].set_title('KDE of Promotion and Years at the company (filtered on attrition)')

kde_yp = sns.kdeplot(x = dataset_subset.YearsAtCompany, y = dataset_subset.YearsSinceLastPromotion, \
                 shade = True, cmap = 'GnBu', ax = axes[1])
kde_yp_shape = sns.kdeplot(x = dataset_subset.YearsAtCompany, y = dataset_subset.YearsSinceLastPromotion, \
                  cmap = 'cool', ax = axes[1]) 
axes[1].set_title('KDE of Promotion and Years at the company (not filtered)')
plt.show() 
