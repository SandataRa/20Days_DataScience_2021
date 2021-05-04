#Copyright: These datasets were prepared using publicly available data.
#           However, theses scripts are subject to Copyright Laws. 
#           If you wish to use these Python scripts outside of the Python Programming Course
#           by Kirill Eremenko, you may do so by referencing www.superdatascience.com in your work.

import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 
import seaborn as sns # pip install seaborn here 
get_ipython().run_line_magic('matplotlib', 'inline')


dataset = pd.read_csv("C:\\Users\\Sandratra\\Downloads\\Homework6-Dataset.csv")
dataset

dataset.info()

movies = dataset[['Movie Title','Genre','Studio','Profit ($mill)','Budget ($mill)','Release Date','Gross % US']]
movies.columns = ['Movie','Genre','Studio','Profit','Budget','ReleaseDate','GrossUS']
movies

# Transform categorical data
movies.Movie = movies.Movie.astype('category')
movies.Genre = movies.Genre.astype('category')
movies.Studio = movies.Studio.astype('category')
movies.ReleaseDate = movies.ReleaseDate.astype('category')

movies.info()

f1 = (movies.Genre.isin(['action', 'comedy', 'adventure', 'animation', 'drama'])) &  (movies.Studio.isin(['Buena Vista Studios', 'Sony', 'Universal', 'WB', 'Paramount Pictures', 'Fox']))
movies = movies[f1]
movies.tail(50)

# Building the box plot
plt.rcParams['figure.figsize'] = 12,6
sns.set_style("dark")


bplot = sns.boxplot(data = movies, x="Genre" , y = "GrossUS", order=["action", "comedy","adventure","animation","drama"],
                   color = "LightGray", showfliers = False)
bplot = sns.swarmplot(data= movies , x="Genre", y="GrossUS", order=["action", "comedy","adventure","animation","drama"], 
                     hue = 'Studio', hue_order = ['Buena Vista Studios', 'Sony', 'Universal', 'WB', 'Paramount Pictures', 'Fox'],
                     palette = "husl")

plt.legend(prop={'size':10} , loc='upper left', bbox_to_anchor=(1,1), frameon = False, framealpha = 0)
plt.ylabel("Gross % US", fontsize = 20, color = "Black")
plt.xlabel("Genre", fontsize = 20, color = "Black")
plt.yticks(fontsize = 15)
plt.xticks(fontsize = 15)
plt.title("Domestic Gross % by Genre", fontsize = 30, color="Black", fontname = "Arial")
plt.show()

movies.Studio.unique()
movies.Genre.unique()

bplot = sns.boxplot(data = movies, x="Genre" , y = "GrossUS", order=["action", "comedy","adventure","animation","drama"],
                   color = "LightGray", showfliers = False)
bplot = sns.stripplot(data= movies , x="Genre", y="GrossUS", order=["action", "comedy","adventure","animation","drama"], jitter = True,
                     hue = 'Studio', hue_order = ['Buena Vista Studios', 'Sony', 'Universal', 'WB', 'Paramount Pictures', 'Fox'],
                     palette = "husl")

plt.legend(prop={'size':10} , loc='upper left', bbox_to_anchor=(1,1), frameon = False, framealpha = 0)
plt.ylabel("Gross % US", fontsize = 20, color = "Black")
plt.xlabel("Genre", fontsize = 20, color = "Black")
plt.yticks(fontsize = 15)
plt.xticks(fontsize = 15)
plt.title("Domestic Gross % by Genre", fontsize = 30, color="Black", fontname = "Arial")
plt.show()

