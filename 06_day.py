numbers = [1, 2, 3]
numbers2 = [4, 5, 6]
#print(numbers.append(numbers2))    # 복사본을 반환하지 않았따.

numbers.append(numbers2)
print(numbers)   # [1, 2, 3, [4, 5, 6]]


# print(numbers.extend(numbers2))    # None, 복사본을 반환하지 않았다. 

numbers.extend(numbers2)
print(numbers)   # [1, 2, 3, 4, 5, 6]






numbers = [1, 2, 3]
# sort 메서드
print(numbers.sort())   # None


numbers = [3, 2, 1]
# sorted 함수
print(sorted(numbers))   # [1, 2, 3], 원본은 건드리지 않고 복사본을 만들어서 정렬을 한다.
print(numbers)           # [3, 2, 1], 원본은 바뀌지 않았다.

