# 로또 생성하기
from random import random
from numpy import math

lottoArr = list(range(1, 46))

for i in range(len(lottoArr)):
    ran = int(random()*len(lottoArr))
    
    temp = lottoArr[ran]
    lottoArr[ran] = lottoArr[i]
    lottoArr[i] = temp
    
    
print(lottoArr[0:6])