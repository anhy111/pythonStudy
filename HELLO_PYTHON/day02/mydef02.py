# 구구단짜기

# def dan(dan):
#     for i in range(1,9+1):
#         print("{} * {} = {}".format(dan,i,dan*i))
#
# def gugudan():
#     for i in range(1,9+1):
#         if i % 2 == 0:
#             dan(i)
#
# gugudan()

for i in range(2,9+1):
    if i % 2 == 0:
        for j in range(1,9+1):
            print("{} * {} = {}".format(i,j,i*j))
