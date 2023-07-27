### 다중 상속

class Person:
    def __init__(self, name):
        self.name = name
        

    def greeting(self):
        return f'안녕, {self.name}'


class Mom(Person):
    gene = 'XX'

    # def __init__(self, name):
    #     super().__init__(name)   스타일가이드 권장

    def swim(self):
        return '엄마가 수영'
    

class Dad(Person):
    gene = 'XY'

    def __init__(self, name, age):
        super().__init__(name)   #스타일가이드 권장
        self.age = age

    def walk(self):
        return '아빠가 걷기'
    

class FirstChild(Mom, Dad):   # 상속 순서에 따라서 결과가 달라진다.
    dad_gene = Dad.gene
    
    def __init__(self, name, age):
        Dad.__init__(self, name, age)  # 스타일가이드 권장
    
    def swim(self):
        return '첫째가 수영'
    
    def cry(self):
        return '첫째가 응애'


baby1 = FirstChild('아가')
print(baby1.cry())   # 첫째가 응애
print(baby1.swim())  # 첫째가 수영
print(baby1.walk())  # 아빠가 걷기
print(baby1.gene)    # XX
print(baby1.dad_gene)# XY

print(FirstChild.mro())



