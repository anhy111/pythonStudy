# 첫 수를 넣으세요    2

# 끝수를 넣으세요    4

# 2에서 부터 4까지의 합은 9입니다.

first = int(input("첫 수를 넣으세요 : "))
last = int(input("끝수를 넣으세요 : "))
sum = 0

for i in range(first, last+1):
    sum += i
    
# print(first,"에서",last,"까지의 합은",sum,"입니다")
print("{}에서 {}까지의 합은 {}입니다.".format(first, last, sum))

