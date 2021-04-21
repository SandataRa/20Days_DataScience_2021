#Testing the Law of large Number

import random

def LawLargeNumber (sample_size, mean = 0, sigma = 1, expected_value = 68.2):
    counter = 0
    selected = [] 

    while sample_size > 0:
        pick = random.normalvariate(mean, sigma)
        selected.append(pick)
        if (-1 < pick and pick < 1):  
            counter += 1

        sample_size -= 1    
    print("Mean(Xn)=", (counter / len(selected)), " | n=", len(selected), " | E(X)=", expected_value)

LawLargeNumber(10)
LawLargeNumber(1000)
LawLargeNumber(100000)
LawLargeNumber(1000000)
LawLargeNumber(10000000)
LawLargeNumber(100000000)