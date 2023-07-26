# Person 정의
class Person:
    name = 'unknown'

    # 인스턴스 메서드
    def talk(self):
        print(self.name)

p1 = Person()
p1.talk()   # unknown, 인스턴스는 인스턴스 변수가 없으면 클래스 변수를 찾아간다.
# p2 인스턴스 변수 설정 전/후

p2 = Person()
p2.talk()   # unknown

p2.name = 'Kim'
p2.talk()   # Kim

print(Person.name)   # unknown
print(p1.name)   # unknown
print(p2.name)   # Kim