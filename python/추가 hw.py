# 함수 작성 연습

# 1. 리스트를 입력 받아
# 100을 초과하는 값을 리스트로 반환하기
# len 함수 사용 x

arr = [98, 99, 100, 101, 102, 103]

def test1(X):
    result = []
    for i in X:
        if i > 100:
            result.append(i)
    return result

res = test1(arr)
print(res)

# 2. 리스트를 입력받아
# 그 안에서 큰 요소 3개를 리스트로 반환하기
# (*단, 원본 리스트에는 영향을 주면 안됨)
# len 함수 사용 x

def test2(x):
    n_lst = sorted(x)[::-1]
    return n_lst[:3]


    # max_list = []
    # for i in x:
    #     if x[i+1] > x[i]:
    #         max_list.append(i+1)

print(test2(arr))
print(test2([1, 2]))
print(test2([1]))
print(test2([]))
# 3. 리스트를 입력 받아서
# 최댓값과 최솟값을 튜플 형태로 반환하기
# min, max 내장함수 사용x

def test3(x):
    # arr이 빈 리스트라면..
    if len(arr) == 0:
        return (None, None)
    # 최솟값, 최댓값
    mn = arr[0]
    mx = arr[0]
    # 리스트를 전부 순회하면 최댓값과 최솟값을 갱신...
    for i in x:
        if mn > i:
            mn = i
        if mx < i:
            mx = i
    return mn, mx

print(test3(arr))
print(test3([1, 2]))
print(test3([1]))
print(test3([]))

# 4. 리스트를 입력받아서
# 짝수에 해당하는 값만을 리스트로 반환하기
# 내장함수 x

def test4(x):
    result = []
    for i in x:
        if i % 2 ==0:
            result.append(i)
    return result

print(test4(arr))


# 5. 리스트의 평균 값을 반환하기
# 내장함수 x

def test5(x):
    total = 0
    length = 0
    for i in x:
        total += i  # 요소값을 total 에 누적
        length += 1 # 요소의 갯수를 카운트
    return total / length

print(test5((arr)))
print(test5([1, 2]))
print(test5([1]))
print(test5([]))

# 6. 리스트의 시작점과 종료점을 받아서 슬라이스한 부분의 리스트를 반환하기

def test6(x, start, end):
    return x[start:end]

print(test6(arr, 2, 5))
print(test6([1, 2]))
print(test6([1]))
print(test6([]))
