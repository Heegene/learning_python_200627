
def add(a, b):
    return a+b




add(10,20)


# 함수: 독립적으로 수행하는 프로그램 단위
# 특정 작업을 수행하는 명령어들의 모음에 이름을 붙인 것

# 함수 정의
# def 함수이름(입력 인수) :
# 수행할 문장 ...
# return 반환값


def add2(a, b):
    result = a + b
    return result

add2(100,200)


# 정수 거듭제곱

def power(x, y) :
    result = 1
    for i in range(y):
        result = result * x
    return result
print(power(10,2))
