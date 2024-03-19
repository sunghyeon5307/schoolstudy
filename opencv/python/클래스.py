import os
os.system('clear')

# 클래스 선언
class Dog:
    name="default"
    gender="male/Female"
    owner="default name"

    def Bark(self):
        print(self.name+":멍멍")

# 객체 생성과 사용 방법
dog=Dog()
dog.name="노랑이"
dog.gender="Female"
dog.owner="J.Kim"
dog.Bark()

# 클래스 상속
class Parent:
    num=0
    # constructor(생성자)
    def __init__(self, num) -> None:
        self.num=num
        print("constructor of the parent class was called")
class Child(Parent):
    # constructor(생성자)
    def __init__(self, num) -> None:
        super().__init__(num)
        print("constructor of the child class was called")

        # child에만 추가된 함수
        def displayValue(self):
            print("num :", self.num)
    
cd=Child(20)
cd.displayValue()