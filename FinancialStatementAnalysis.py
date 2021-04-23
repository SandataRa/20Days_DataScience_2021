# Financial Statement Homework
import numpy as np 

#Data of the year
revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]

months = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'] 

fprofit = lambda x,y : round(x,2) - round(y,2) 
fprofit_AT = lambda x : round(x,2) * 0.70 # Tax Rate= 30% 

profit = []
profit_AT = []
margin = []

good_month = {'index': 0, 'max': 0}
bad_month = {'index': 0, 'min': 0}

for i in range(12):
    profit.append(int(fprofit(revenue[i],expenses[i]))) 
    profit_AT.append(int(fprofit_AT(profit[i])))
    margin.append( round((profit_AT[i] / revenue[i])*100, 2) )
   
print("Profit:" , profit)
print("Profit (After tax):" ,profit_AT)
print("Profit margin:", margin)

mean = np.mean(profit_AT)
print("Mean =", mean)

best_months = [months[i] for i in range(12) if profit_AT[i] > mean]
print(best_months)

worst_months = [months[i] for i in range(12) if profit_AT[i] < mean]
print(worst_months)

print("The best month is:", months[np.argmax(profit_AT)])
print("The worst month is:", months[np.argmin(profit_AT)])