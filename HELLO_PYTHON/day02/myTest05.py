# 첫수를 넣으세요    2

# 끝수를 넣으세요    4

# 배수를 넣으세요    3

# 2에서 4까지 3의 배수의 합은 3입니다.

first = int(input("첫수를 넣으세요 : "))
last = int(input("끝수를 넣으세요 : "))
dainage = int(input("배수를 넣으세요 : "))

sum = 0
for i in range(first, last+1):
    if i % dainage == 0:
        sum += i
        
print("{}에서 {}까지의 {}의 배수의 합은 {}입니다.".format(first, last, dainage, sum))