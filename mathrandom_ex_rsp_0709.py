import random


player = input("가위, 바위, 보 중에서 하나를 선택하세요.")

number = random.randint(0,2) #정수 난수 0,1,2 중 하나 생성

if (number == 0) :
    computer = "가위"
elif (number == 1) :
    computer = "바위"
elif (number == 2) :
    computer = "보"

print ("사용자: ", player, "컴퓨터", computer)

if player == computer:
    print("비겼습니다.")
elif player == "바위":
     if computer == "보":
         print("이겼습니다.")
     else :
         print("졌습니다.")
elif player == "보":
     if computer == "가위":
         print("이겼습니다.")
     else :
         print("졌습니다.")
elif player == "가위":
     if computer == "보":
         print("이겼습니다.")
     else :
         print("졌습니다.")



