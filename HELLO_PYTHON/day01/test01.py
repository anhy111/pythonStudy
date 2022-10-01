# 1 ~에서 100까지의 정수 중 3의 배수의 합을 구하시오

sum = 0
for i in range(1, 101):
    if i % 3 == 0:
        sum += i

print("sum=",sum)