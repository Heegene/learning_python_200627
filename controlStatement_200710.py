for fivetimes in range(5) :
    print("Hello python!")

    #레인지는 지정된 범위의 값을 받음
    # for문을 이용하여 원하는 만큼 반복 가능

# range() 함수 이용
# range([start,] stop [,step]) 의 syntax

# 1부터 10까지 더한다면 1, 11 이렇게 start, stop 지정
# step은 간격

for fivetimes in range(1,11,2) :
    print("실험")
    # 이것도 2,4,6,8,10 이렇게 5번

# 리스트 데이터 구조 []
for list in [0, 1, 2, 3, 4] :
    print( list, end = " ")


for name in ["문", "자", "열", "상", "수"] :
    print(name, " ")

# 문자열의 반복
for c in "abcedf":
    print(c, end=" ")
    # 문자열 하나하나 한줄에 각각 프린트

#while 반복문
i = 0; # 초기화

while i < 5:
    print("얼굴맛집 이콩이~!")
    i += 1
print("반복이 종료되었습니다.")

#5번 반복하고 (0,1,2,3,4) 반복이 종료됨 


for i in range(1,100) :
    print("for문을 %d번 실행합니다" %i)
    break
# 첫번째에 바로 빠져나가서 더이상 수행되지 않음(jump statement)

# 반복문으로 다시 돌아가는 continue 문
# 반복문의 처음으로 돌아감

hap, i = 0, 0

for i in range(1,101) : # 100번 반복
    if i % 3 == 0: # i가 3의 배수이면
        continue # 더하지 않고 건너뜀
    hap +=i
print("1~100의 합계(3의 배수는 제외한다. : %d" %hap)

for number in [1,2,3]
    print(number)