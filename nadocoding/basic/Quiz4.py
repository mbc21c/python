# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2,3,4]
# -- 축하합니다 --

# (활용 예제)
from random import *
users = range(1, 21) # 1부터 20까지 숫자를 생성
users = list(users)
#lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(users)

shuffle(users)

print(users)
 
winner = sample(users, 4)
print(type(winner))
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winner[0]))
print("커피 당첨자 : {0}".format(winner[1:]))
print("-- 축하합니다 --")