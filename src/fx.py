
import math
import numpy as np

def x2(x):
    return x**2

def lnx(x):
    return math.log(x)

def mb1(x, r, n):
    x0 = x
    r0 = r
    for i in range(1, n + 1):
        x =  r * x * (1 - x)
        if x <= 0:
            return 0
        # if x >=1:
        #     return 1

    return x

        
if __name__ =="__main__":
    print(mb1(0.001001001001001001, 4.084084084084084, 9))