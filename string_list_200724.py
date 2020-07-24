NUM = 5
stringlist = []

for i in range (NUM):
    value = input("학생 이름을 입력하세요 : ")
    stringlist.append(value)

print(stringlist)

for i in range(len(stringlist)):
    print(stringlist[i],", ")



names = []
while True:
    name = input("학생 이름을 입력하세요 : ")
    if name == "" :
        break
    names.append(name)


print("학생 이름 :" )
for name in names :
    print(name, end=", ") # 이렇게하면 옆으로 연결 가능 