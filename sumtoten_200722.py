
sum = 0;


limit=int(input("어디까지 계산할까요 : "))
for i in range(1, limit+1) :
    sum += i

print("1부터 " , limit , "까지의 정수의 합 " , sum)


# 팩토리얼 계산
# 팩토리얼 n!은 1부터 n까지의 정수를 모두 곱한 것
# 2! 는 1*2

fac = 1;

limit = int(input(" 어디까지 계산할까요? "))
for i in range (1, limit+1):
    fac += fac * i;

print(limit, "!의 값은", fac)


# 자리수의 합 계산
number = int(input("정수를 입력하세요."))
sum = 0;
while number > 0 :
    digit = number % 10
    sum = sum + digit
    number = number // 10
print("자리수의 합은 %d 입니다." %sum)

