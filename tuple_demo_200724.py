# 튜플: 변경될 수 없는 리스트

colors = ("red", "green", "blue")
# 둥근 괄호로 됨
# colors[0] = "redddd" # 컴파일에러 발생 tuple 변경 불가


# dictonary 키와 값을 가지는 객체
# 딕셔너리 = { 키1:값1, 키2:값2, ... }
contacts = {'Kim':'01012341234', 'Kong':'02234', 'kongE':'12323'}
if "Kim" in contacts:
    print("해당 키가 딕셔너리에 있습니다. ")

# 딕셔너리의 순회 
for item in contacts.items():
    print(item)

print(contacts['Kim'])

# 문자열 다루기
word = 'Python'
print(word[0:2]) # 'py' 출력됨
print(word[2:4]) # thon 출력 2부터 끝까지 

if 'p' in word:
    print('p가 포함되어 있음')
else :
    print('p가 포함되어 있지 않음 ')

