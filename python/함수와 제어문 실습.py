# def greeting(name, age):
#     print(f'안녕, {name}, {age}!!')


# greeting('Alice', 25)   # 안녕, Alice, 25!!

# greeting(25, 'Alice')  # 안녕, 25, Alice!!

# greeting(age=25, name='Alice')  # 안녕, Alice, 25!!

# greeting(age=25, 'Dave')  # 문법 에러, 위치 인자가 키워드 인자 이후에 등장하고있다.

# print('hi', 'aaa', 'bbb', 'ccc')
# print('hi', 'aaa', 'bbb')   # print 함수는 임의의 개수를 받을 수 있다.

# def calculate_sum(*args):
#     print(args)    #(1, 2, 3, 4, 5)
    


# calculate_sum(1, 2, 3, 4, 5)


# def calculate_sum(*kwargs):
#     print(kwargs)    #{'name': 'Alice', 'age': 30, 'adderss': korea}

# calculate_sum(name='Alice', age=30, address='korea')

# def my_func():
#     num = 1

# print(num)   # nameError: name 'num is not defined
#             # 위 num 과 아래 num은 다른 저거임


# print(sum([1, 2, 3]))   # 6


# sum = 10

# print(sum)   # 10

# print(sum([1, 2, 3]))   # typeError: 'int' object is not callable



# numbers = [1, 2, 3]
# result = map(str, numbers)

# print(result)  # map object ,,,
# print(list(result))  # ['1', '2', '3']


# def my_func():
#     result = x * 2
#     return result


# reslut = []
# for number in numbers:
#     result.append(str(number))

# print(result)

# # map + lambda
# numbers = [1, 2, 3, 4, 5]
# result = list(map(lambda x: x * 2, numbers))
# print(result)   # [2, 4, 6, 8, 10]

number_of_people = 0


def increase_user():
    number_of_people += 1
    return number_of_people

increase_user()
print(number_of_people)
