from random import random


def getLotto():
    arr45 = list(range(1, 45+1))

    for i in range(100):
        ran = int(random()*len(arr45))
        
        a = arr45[0]
        b = arr45[ran]
        arr45[0]=b
        arr45[ran]=a
        
        # temp = lottoArr[ran]
        # lottoArr[ran] = lottoArr[0]
        # lottoArr[0] = temp
    return arr45[0:6]


arr6 = getLotto()
print(arr6)