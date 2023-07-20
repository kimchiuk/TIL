# num = int(input('숫자를 입력하세요: '))

# # if statement
# # num이 홀수라면 (2로 나눈 나머지가 1이라면)
# if num % 2 == 1:  # 얼마나 더 명시적인 코드를 쓰는지가 중요하다.
# # if num % 2:
#     print('홀수입니다.')
# # num이 홀수가 아니라면(짝수면)
# else:
#     print('짝수입니다.')

# 0~9 요소를 가지는 리스트 만들기
# 1. 일반적인 방법
new_list = []
for i in range(10):
    new_list.append(i)
print(new_list)  
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 2. list comprehension
new_list_2 = [i for i in renge(10)]
print(new_list_2)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 홀수1    
new_list = []
for i in range(10):
    if i % 2 == 1:
        new_list.append(i)

print(new_list)

# 홀수2
new_list_2 = [i for i in renge(10) if i % 2 == 1]
print(new_list_2)

### 위 두가지 리스트를 작성할 수 있는 능력을 길러야 한다. 
### 하지만 가독성이 중요하므로 위 조건문이 더 일반적인 방법


new_list_2 = [i for i in renge(10) if i % 2 == 1]
new_list_3 = [i if i % 2 == 1 else str(i) for i in range(10)]   # elif 사용 불가능, 중첩 if은 가능 
print(new_list_2)
print(new_list_3)  # ['0', 1, '2', 3, '4', 5]

 # 위 아래 동일

new_list = []
for i in range(10):
    if i % 2 == 1:
        new_list.append(i)
    else:
        new_list.append(str(i))
print(new_list)



# 리스트를 생성하는 3가지 방법 비교
# 정수 1, 2, 3을 가지는 새로운 리스트 만들기
# 어떤게 제일 빨라요??

numbers = ['1', '2', '3']

# 1. for loop
new_numbers = []
for number in numbers:
    new_numbers.append(int(i))
print(new_numbers)  # [1, 2, 3]

# 2. map
new_numbers_2 = list(map(int, numbers))
print(new_numbers_2) # [1, 2, 3]

# 3. list comprehension
new_numbers_3 = [int(number) for number in numbers]
print(new_numbers_3)

# 성능? => 일반화가 불가능 (외부요인, 상황)
# loop & map & comprehension

# - 대부분의 상황에서는 comprehension 이 빠르다.
# - 하지만 다른 함수, 내장함수에 따라 map이 더 빠른 경우도 많았다.
# - 파이썬이 3점대 후반에 for loop 성능에 비약적인 향상이 있었음
# - 그래서 극단적인 차이는 존재하지 않는다.
# 코드의 가독성이 > 간결함 보다 중요하다.
# 프로그래밍은 우리 프로그램이 어떻게 그 목적을 명확하게 전달하는지에 대한 것
# "작은 효율성에 대해서는, 말하자면 97% 정도에 대해서는, 잊어버려라. 섣부른 최적화는 모든 악의 근원이다." - 도널드 knuth



# enumerate
result = ['a', 'b', 'c']

print(enumerate(result))  # <enumerate object at ,,,>
print(list(enumerate(result))) # [(0, 'a'), (1, 'b'), (2, 'c')]

for index, elem in enumerate(result):
    print(index, elem)


