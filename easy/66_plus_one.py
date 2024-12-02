import math
from math import remainder


def plus_one(arr):
    num = 0
    for i, n in enumerate(arr):
        j = len(arr)-i-1
        num += n*math.pow(10,j)
    print(num)
    num_plus_one = int(num+1)
    print(num_plus_one)
    return [int(i) for i in str(num_plus_one)]



print(plus_one([6,1,4,5,3,9,0,1,9,5,1,8,6,7,0,5,5,4,3]))

