from random import random

# 홀/짝을 입력하시오 홀
# 나 : 홀
# 컴 : 홀
# 결과 : 승리

na = input("홀/짝을 입력하시오 : ")

com = ""
ran = random()

# 컴퓨터의 홀/짝
if ran >= 0.5:
    com = "홀"
else:
    com = "짝"


# 결과
result = ""

if com == na:
    result = "승리"
else:
    result = "패배"

print("나 : " + na)
print("컴 : " + com)
print("결과 : " + result)


