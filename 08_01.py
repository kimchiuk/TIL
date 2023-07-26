# 클래스 정의
class Person:
    # 속성(변수)
    blood_color = 'red'

    # 메서드
    def __init__(self, name):  # 개발자가 직접 호출하지 않는다. 자연스럽게 동작
        self.name = name      # 생성자 메서드

    def singing(self):
        return f'{self.name}가 노래합니다.'
    

# 인스턴스 생성
singer1 = Person('iu')
singer2 = Person('BTS')

# 메서드 호출
print(singer1.singing())
print(singer2.singing())

# 속성(변수) 사용
print(singer1.blood_color)
print(singer2.blood_color)

