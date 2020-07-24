# 파이썬에서는 두 개의 값을 서로 swap 할 수 있음
# 파이썬, c에 모두 통용되는 방법은 temp 만들어서
# 거기에 넣고 temp를 거쳐 이동시키는 것

# 근데 파이썬에서는 그냥 스왑 가능
# a, b = b, a 이런식

def add(a,b) :
    return a+b

def swap(c,d) :
    c, d = d, c
    return c,d



# 시작코드

a = int(input("정수 1을 입력하세요 : "))
b = int(input("정수 2를 입력하세요 : "))

sum = add(a,b)
average = sum/2

print(" 두 수의 합 : " , sum)
print(" 두 수의 평균 : " , average)

a,b = swap(a,b)
print(" 두 수의 교환 : ", a, b)




