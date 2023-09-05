string = '문자열'
integer = 10
floating_point = 3.14
a_list = [1, 2, 3, 4, 5]
dictionary = {'name': '홍길동', 'age': 20}
a_set = {1, 2, 3, 4, 5}
a_range = range(11)
a_tuple = (1, 2, 3)
boolean = True

print(type(string))
print(type(integer))
print(type(floating_point))
print(type(a_list))
print(type(dictionary))
print(type(a_set))
print(type(a_range))
print(type(a_tuple))
print(type(boolean))

  # 사전 dictionary... "키-값"
# fruits = {'사과':'apple',
#           '바나나':'banana', 
#           '키위':'kiwi'
# }
# fruit = '사과'
# print('사과' + '는 영어로 ' + fruits[fruit])
# fruit = '바나나'
# print('바나나' + '는 영어로 ' + fruits[fruit])
# fruit = '키위'
# print('키위' + '는 영어로 ' + fruits[fruit])

apple1 = '사과는'
banana1 = '바나나는'
kiwi1 = '키위는'
eng = '영어로'
apple1_eng = 'apple'
banana1_eng = 'banana'
kiwi1_eng = 'kiwi'

print(apple1, eng, kiwi1_eng)
print(banana1, eng, banana1_eng)
print(kiwi1, eng, kiwi1_eng)


print('3의 2배의 값 : ', 3 * 2)
print('3의 제곱 값 : ', 3 ** 2)
print('3의 제곱 값에 3의 2배의 값으로 나눈 몫 : ', (3 ** 2) // (3 * 2))
print('3의 제곱 값에 3의 2배의 값으로 나눈 나머지 : ', (3 ** 2) % (3 * 2))
print('3의 제곱 값에 -3의 제곱 값을 더한 결과 : ', 3 ** 2 + (-3 ** 2))


num1 = 3 * 2
num2 = 3 ** 2
num3 = -3 ** 2

print('3의 2배의 값 : ', int(num1))
print('3의 제곱 값 : ', int(num2))
print('3의 제곱 값에 3의 2배의 값으로 나눈 몫 : ', int(num2 // num1))
print('3의 제곱 값에 3의 2배의 값으로 나눈 나머지 : ', int(num2 % num1))
print('3의 제곱 값에 -3의 제곱 값을 더한 결과 : ', int(num2 + (num3)))

print('makit "code" lab')
print('she\'s gone')

# '\n' : 띄어쓰기...
# '\t' : 들여쓰기...
# '\\' : \겹치는 것 방지

# 한줄 문자열을 입력하는 함수 : input(내가 출력하고싶은 메시지) 함수...

# 인덱스
# [시작:끝], 시작 <= x < 끝
# [0:5] <= [:5] 앞자리 생략가능
# [6:13] <= [6:] 마지막일 경우 뒷자리 생략가능
# [::n] [시작, 끝, 스텝수], 시작 <= x < 끝
# [::-1] 스텝수를 음수 값으로 주면, 거꾸로 출력되는 문자를 만들 수 있다.

# 문자열 바꾸기
# 문자열.replace(변경이전문자, 변경이후문자)
# new_phone = phone.replace('-', '.')

a_list = ['메이킷', '우진', '시은']
print(a_list[0])
