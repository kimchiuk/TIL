# 진법 변경 (10진수 -> n진수)
print(bin(12))
print(oct(12))
print(hex(12))

print(2 / 3)
print(5 / 3)

# 지수(제곱하는 횟수) 표현 10^ 
print(314e-2)  # 3.14
print(314e2)   # 31400.0


# f-string
bugs = 'roaches'
counts = 13
area = 'living room'

# Debugging roaches 13 living room
print(f'Debugging {bugs} {counts} {area}')
# print('Debugging {bugs} {counts} {area}'.format(bugs, counts, area))
# print('Debugging %s %d %s' % (bugs, counts, area))   

# f-string 응용
greeting = 'hi'
print(f'{greeting:>10}')   # 10칸 오른쪽 정렬
print(f'{greeting:^10}')   # 10칸 가운데 정렬
print(f'{3.141592:.4f}')   # 앞 실수를 소수점 4자리까지


# 불변과 가변
my_str = 'hello'
#my_str[0] = 'z'    # str 변경 불가.

my_list = [1, 2, 3]
my_list[0] = 100
print(my_list)    # [100, 2, 3]


#리스트는 객체들의 참조만을 모아놓은 컬렉션

list_1 = [1, 2, 3]
list_2 = list_1

list_1[0] = 100
print(list_1) # [100, 2, 3]
print(list_2) # [100, 2, 3] , 값이 아니라 메모리 주소를 할당 하는 것
# 파이썬 튜터 활용하면 설명 가능


x = 10
y = x

x = 20
print(x) # 20, 불변과 가변 특징을 확인할 수 있다. 
print(y) # 10, 


vowels = 'aeiou'

print(('a' and 'b') in vowels) # False,  문자열일 경우에 '??'(무엇이든 있으면) -> True
print(('b' and 'a') in vowels) # True, '' (비어있으면) -> False
                               
