# 출력을 원하는 단수를 입력하세요    5
# 5 * 1 = 5
# 5 * 2 = 5


dan = int(input("출력을 원하는 단수를 입력하세요 : "))

for i in range(1,10):
    print("{} * {} = {}".format(dan,i,dan*i))


