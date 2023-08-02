# 배열 2

# 2차원 배열

## 2차원 배열의 선언

- 1차원 list 를 묶어놓는 list
- 2차원 이상의 다차원 list 는 차원에 따라 Index 를 선언
- 2차원 list 의 선언: 세로길이(행의 개수), 가로길이(열의 개수)를 필요로 함
- Python 에서는 데이터 초기화를 통해 변수선언과 초기화가 가능함

![img.png](img.png)

## 참고

![img_5.png](img_5.png)

## 2차원 배열의 접근

- 배열 순회
  - n X m 배열의 n*m 개의 모든 원소를 빠짐없이 조사하는 방법
    
- 행 우선 순회
```python

# i 행의 좌표
# j 열의 좌표

for i in range(n):  # 행
    for j in range(m): # 열
        f(array[i][j]) # 필요한 연산 수행

```
![img_1.png](img_1.png)

- 열 우선 순회
```python

# i 행의 좌표
# j 열의 좌표

for j in range(m):   # 열
    for i in range(n):  # 행
        f(array[i][j]) # 필요한 연산 수행
```
![img_2.png](img_2.png)

- 지그재그 순회
```python

# i 행의 좌표
# j 열의 좌표

for i in range(n):
    for j in range(m):
        f(array[i][j + (m-1-2*j) * (i%2)])   # i%2 는 홀수일때만 남기는 방법 중 하나
        # 필요한 연산 수행
```
![img_3.png](img_3.png)

- 델타를 이용한 2차 배열 탐색
  - 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법
    
```python

arr[0, 1, 2, N-1][0,1, 2, N-1]  # NxN 배열
dj[] = [0, 1, 0, -1] #
dj[] = [1, 0, -1, 0] 
for i in arr: # 0-> N-1
    for j in arr: # 0 -> N-1:
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N  # 유효한 인덱스면
                f(arr[ni][nj])

```

- 전치 행렬
```python

# i: 행의 좌표, len(arr)
# j: 열의 좌표, len(arr[0]
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # 3*3 행렬

for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

```
![img_4.png](img_4.png)

