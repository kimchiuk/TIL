class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f'안녕, {self.name}입니다.')


class Professor(Person):
    def __init__(self, name, age, department):
        # self.name = name
        # self.age = age
        super().__init__(name, age)
        self.department = department


class Student(Person):
    def __init__(self, name, age, gpa):
        # self.name = name
        # self.age = age
        # Person.__init__(self, name, age)  # 위 두줄 대신 작성해도 됨, 대신 유연함이 떨어짐 (Person이름을 수정할 경우)
        # 다중 상속을 받게 되는 경우
        super().__init__(name, age)
        self.gpa = gpa

p1 = Professor('박교수', 49, '컴공')
s1 = Student('김학생', 20, 3.5)

p1.talk()
s1.talk()



