# Exercise 1
import numpy as np 

x,y = np.ones((22,10)) , np.ones((22,10)) # Task1
print(x[-20: , 2:6]) # Task 2
xf = x.flatten() # Task 3
print(xf)

def reshapetofour(arr): # Task 4
    print("Before reshaping the array: ")
    print(arr)
    print("After reshaping the array: ")
    return arr.reshape((-1,4)) 

print(reshapetofour(y))

# Exercise 2
filters = []
labels = list()
for g in movies.Genre.cat.categories :
    labels.append(g)
    elem = movies[movies.Genre == g].Budget
    filters.append(elem)
plt.hist(np.array(filters, dtype='object'), bins = 30, stacked = True, label = labels)
plt.legend()
plt.show()

