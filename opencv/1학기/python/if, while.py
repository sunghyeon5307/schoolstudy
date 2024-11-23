# if
import os
os.system('clear')

num=int(input("정수형 숫자 입력:"))
if num<0:
    num=0
    print("음수라서 0설정")
elif num==0:
    print("0")
elif num==1:
    print("1")
else:
    print("일보다 큼")

# while
import os
os.system('clear')

num=0
while num<5:
    print(num)
    num+=1
print("end")

