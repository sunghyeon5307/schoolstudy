import os
os.system('clear')

def addFunc(a, b):
    return a+b
a=3
b=4
print("a+b=", addFunc(a, b))

# def 함수명(매개변수):
#     함수 내용
#     return 변수

def login(msg, times=3, warn="wrong ID"):
    while True:
        id=input(msg)
        if id in ("user", "User", "USER"):
            return True
        times=times-1
        if times<=0:
            print("time out")
            return False
        print(warn)
print(login("#1:ID 입력"))
#login("#2:ID 입력", 2)
#login("#3:ID 입력", 2, "다시")

