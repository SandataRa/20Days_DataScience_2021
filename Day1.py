# Task N°1
v_integer = int(500)
v_float = float(3.141315)
v_string = "Hello world"
v_boolean = bool(1)
 
print(type(v_integer), type(v_float), type(v_string), type(v_boolean))
 
print('%i, %.2f, %s, %s' % (v_integer, v_float, v_string, v_boolean))
s = '{0}: {1:d}\t{2}\t{3}\t{4}'.format(v_string, v_boolean, v_integer, v_float, v_boolean)
 
print(s)
 
#Task N°2
values = [3, 53, 19, -5, 60, 41,"test",5,22,9,22]
for n in values:
    if(isinstance(n,int)):
        if(n%2 == 0):
            print('%d is an even number'% (n))
            continue
        elif(n == 9):
            print('5 cavaliers of apocalypses! Goodbye!')
            break
    else:
        print("ALERT : New type identified :", type(n) )
        pass

#Task N°3
import copy
 
groceries = [['beef','chicken','shrimp','fish']
          ,['tomato','lemon','pepper','salad','potatoe','eggplant','cucumber']
            ,['salt','olive oil','butter','hot sauce']
            ]
 
shallow_groceries = copy.copy(groceries) #shallow copy of the list
deep_groceries = copy.deepcopy(groceries) #deep copy of the list
 
print(shallow_groceries[0][1])
shallow_groceries[0][1] = 'duck'
print(shallow_groceries[0][1])
print(groceries)
 
print(deep_groceries[2][0])
deep_groceries[2][0] = 'black pepper'
print(deep_groceries[2][0])
 
#Task N°4
squared_numbers = [x**2 for x in range(10)]
print(squared_numbers)
 
even_squared = [x for x in squared_numbers if x % 2 == 0]
print(even_squared)
 
def add_five(x):
    return int(x) + 5
 
plus_five_list = [add_five(x) for x in even_squared]
print(plus_five_list)
 
[print(x) for x in plus_five_list if x%3 == 0]

#Task N°5
import numpy as np 
 
print("START PROGRAM")
 
v_integer64 = np.int64(2**33)
print('a' , v_integer64)
 
v_float64 = np.float64(387438.2384398439843984398439843984)
print('b', v_float64)
 
# Type Conversion
v_integer32 = v_integer64.astype(np.int32)
print('a_bis', v_integer32)
 
v_integer_32_bis = np.int32(2**31)
print('a_ter', v_integer_32_bis)
 
v_float32 = np.float32(v_float64)
print('b_bis', v_float32)