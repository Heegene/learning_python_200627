for x in range(1,10) :
    if x % 3 == 0:
        break
    print(x, end=" ")

print("끝")


hap = 0
for i in range(1,10) :
    if i % 2 == 0:
        continue
    hap += i
print(hap)