
# 컴퓨터가 선택한 랜덤 숫자를 사용자가 맞히기
# 입력한 숫자가 선택한 숫자보다 높은지 낮은지 정보 제공
# 시도 횟수 제공


import random

tries = 0

number = random.randint(1,100)

print("1부터 100 사이의 정수를 맞혀 주세요.")

while tries < 10:
    guess = int(input("숫자를 입력하세요.  :"))
    tries = tries + 1
    if guess < number :
        print("낮습니다. ")
    elif guess > number :
        print("높습니다. ")
    else :
        break
if guess == number :
    print('축하합니다. 시도 횟수 = ', tries)
else:
    print('정답은', number)

