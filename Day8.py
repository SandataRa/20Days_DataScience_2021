# Practice 1
import numpy as np 
 
mydata = np.arange(0,20)
m1 = np.reshape(mydata, (5,4), order = 'C') # OR mydata.reshape((5,4), order = 'C')
print(m1)
print("Get to the number ten: " ,m1[2,2])
 
m2 = np.reshape(mydata, (5,4), order = 'F')
print(m2)
print("Get to the number ten: ", m2[0,2])
 
r1 = ["I", "AM", "HAPPY"]
r2 = ["WHAT","A", "DAY"]
r3 = [1,2,3]
 
r4 = [r1,r2,r3]
print(r4)
r5 = np.array(r4)
print(r5)
 
# Practice 2
import matplotlib.pyplot as plt
 
ShotAccuracy = np.matrix.round(FieldGoals / FieldGoalAttempts, 2)*100
print(ShotAccuracy)
 
plt.plot(ShotAccuracy[0], c= 'black', ls = '--',marker='s', ms = 3, label=Players[0])
plt.plot(ShotAccuracy[1], c= 'red', ls = '--',marker='o', ms = 3, label=Players[1])
plt.plot(ShotAccuracy[2], c= 'green', ls = '--',marker='^', ms = 3, label=Players[2])
plt.plot(ShotAccuracy[3], c= 'blue', ls = '--',marker='D', ms = 3, label=Players[3])
plt.plot(ShotAccuracy[4], c= 'magenta', ls = '--',marker='s', ms = 3, label=Players[4])
plt.plot(ShotAccuracy[5], c= 'black', ls = '--',marker='^', ms = 3, label=Players[5])
plt.plot(ShotAccuracy[6], c= 'red', ls = '--',marker='^', ms = 3, label=Players[6])
plt.plot(ShotAccuracy[7], c= 'green', ls = '--',marker='D', ms = 3, label=Players[7])
plt.plot(ShotAccuracy[8], c= 'blue', ls = '--',marker='s', ms = 3, label=Players[8])
plt.plot(ShotAccuracy[9], c= 'magenta', ls = '--',marker='o', ms = 3, label=Players[9])
plt.xticks(list(range(0,len(Seasons))),Seasons, rotation='vertical')
plt.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.show()
 
import math 
def removeNanValue(matrice):
    for i in matrice:
        for j in range(len(i)):
            if math.isnan(i[j]):
                i[j] = 0
    return matrice 
 
ShotAccuracy = removeNanValue(ShotAccuracy)
print(ShotAccuracy)
 
import random 
 
def getVisuals(matrice, labels, xticks): 
    for i in range(len(matrice)):
        c = random.choice(['b', 'g', 'r', 'c', 'm', 'y', 'k'])
        s = random.choice(['o','D','^','.','s','P'])
        plt.plot(matrice[i], c= c, ls = '--',marker='s', ms = 3, label=labels[i])
    
    plt.xticks(list(range(0,len(xticks))),xticks, rotation='vertical')
    plt.legend(loc='upper left', bbox_to_anchor=(1,1))
    plt.show()
 
getVisuals(ShotAccuracy, Players, Seasons)
