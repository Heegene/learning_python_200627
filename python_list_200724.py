# list = 여러개의 데이터가 저장되어있는 장소

scores = [32, 56, 64, 72, 12, 37, 98, 77, 59, 69]

stringlist = ["값1", "값2", "값3"]

# list는 zero-indexed datatype임

print(stringlist[2])


print('값1' in stringlist) # true가 출력됨 
print('값1' not in stringlist) # false 출력 

# 리스트 함수 기본 라이브러리
# 리스트명.append(값) 맨뒤에 항목추가
# 리스트명.pop() 맨뒤의 항목 빼내고 삭제함
# 리스트명.sort() 항목 정렬
# 리스트명.reverse() 리스트 항목 순서 역순화
# 리스트명.index(찾을 값) 지정값 찾아서 위치 반환
# 리스트명.insert(위치,값) 지정된 위치에 값 삽입
# 리스트명.remove(지울 값) 리스트에서 지정한 값 제거
# 리스트명.extend(리스트) 리스트 뒤에 리스트 추가함(리스트 더하기)
# 리스트명.count(찾을 값) 찾을 값의 개수를 세서 반환
# del(리스트명[위치]) 리스트에서 해당 위치항목 삭제
# len(리스트명) 리스트에 포함된 전체 항목의 개수를 셈

# 예제: 성적 처리 프로그램
# 사용자로부터 성적 입력받아서 리스트에 저장
# 성적 평균을 구하고 80점 이상 성ㅈ거을 받은 학생 숫자 출력

scores = []
highscore = 0
STUDENTS = 5
sum = 0 



for i in range(STUDENTS): 
    value = int(input("성적을 입력하세요 : "))
    scores.append(value) # 리스트에 값 추가
    sum += value

avg = sum / len(scores)
for i in range(len(scores)):
    if scores[i] >= 80:
        highscore += 1


print("성적 평균은 ", avg)
print("80점 이상 성적을 받은 학생은", highscore, " 명 입니다.")




