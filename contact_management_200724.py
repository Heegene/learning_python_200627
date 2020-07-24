menu = 0

contacts = []

while menu != 9:
    print("---------------------")
    print("1. 친구 리스트 출력")
    print("2. 친구 추가")
    print("3. 친구 삭제 ")
    print("4. 이름 변경")
    print("9. 종료")
    menu = int(input("메뉴를 선택하세요 : "))

    if menu == 1:
        print(contacts)
    elif menu == 2:
        name = input("이름을 입력하세요.")
        contacts.append(name)
    elif menu == 3:
        delname = input("지울 이름을 입력하세요.")
        if delname in contacts:
             contacts.remove(delname)
        else: 
            print("해당되는 이름이 없습니다. ")
    elif menu == 4:
        orgname = input("원래 이름을 입력하세요.")
        if orgname in contacts:
                index = contacts.index(orgname)
                chgname = input("바꿀 이름을 입력하세요.")
                contacts[index] = chgname
        else :
                print("일치하는 이름이 없습니다. ")
