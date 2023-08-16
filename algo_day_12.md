# [참고] 부분집합, 순열

- 집합 {1, 2, 3}의 원소에 대해 각 부분집합에서의 포함 여부를 트리로 표현

- i 원소의 포함 여부를 결정하면 i 까지의 부분 집합의 합 si를 결정할 수 있음
- si-1 이 찾고자 하는 부분집합의 합보다 크면 남은 원소를 고려할 필요가 없음

- A[i] 원소를 부분 집합의 원소로 고려하는 재귀 함수 (A는 서로 다른 자연수의 집합)

```python
def f(i, N, s, t):
    if s == t:
        return
    elif i == N:
        return 
    elif s > t:
        return
    else:
        subset[i] = 1
        f(i+1, N, s+A[i], t)   # i 원소 포함
        subset[i] = 0
        f(i+1, N, s, t)   # i 원소 미포함
```

- 추가 고려 사항

1 2 3 4 5 6 7 8 9 10

고려한 구간의 합 S
S > T 이면 중단.

남은 구간의 합 RS
S + RS < T

남은 원소의 합을 다 더해도 찾는 값 T 미만인 경우 중단

# 순열

- A[1, 2, 3] 의 모든 원소를 사용한 순열
  - 123, 132, 213, 231, 312, 321
  - 총 6가지 경우
    
```
f(i, N)
    if i ==N   # 순열 완성
        
    else
        가능한 모든 원소에 대해
            p[i] 결정
            f(i+1, N)
            p[i] 복구


```


```python
def f(i, N):
    if i == N:    # 순열 완성
        return 
    else:
        for j in range(i, N):
            P[i] = P[j]
            f(i+1, N)
            P[i] = P[j]
```

- 순열 생성 과정 그려보기


# 분할정복 알고리즘
- 유래
  - 1805년 12월 2일 아우스터리츠 전투에서 나폴레옹이 사용한 전략
  - 전력이 우세한 연합군을 공격하기 위해 나폴레옹은 연합군의 중앙부로 쳐들어가 연합군을 둘로 나눔
  - 둘로 나눈 연합군을 한 부분씩 격파함

- 설계 전략
  - 분할(Divide): 해결할 문제를 여러 개의 작은 부분으로 나눈다.
  - 정복(Conquer): 나눈 작은 문제를 각각 해결한다.
  - 통합(Combine): (필요하다면) 해결된 해답을 모은다.
    

## 분할정복 예제
- 거듭 제곱
  - O(n)
    C^2 = C x C
    C^3 = C x C x C
    ...
    C^n = C x C x C x ... x C
    
```python
def Power(Base, Exponent):
    if Base == 0:
        return 1
    result = 1 # Base^0 은 1이므로
    for i in range(Exponent):
        result *= Base
    return result
```

- 분할 정복 기반의 알고리즘: O(log2n)
    C^8 = CxCxCxCxCxCxCxC
    C^8 = C^4 * C^4 = (C^4)^2 = ((C^2)^2)^2
  
    C^n = C^(n/2)*C^(n/2)   n 은 짝수
    C^n = C^((n-1)/2)*C^((n-1)/2)   n 은 짝수
  
```python
def Power(Base, Exponent):
    if Exponent == 0 or Base == 0:
        return 1
        
    if Exponent & 2 == 0:
        NewBase = Power(Base, Exponent/2)
        return NewBase * NewBase
    else:
        NewBase = Power(Base, (Exponent - 1) // 2)
        return (NewBase * NewBase) * Base
```


# 퀵 정렬
- 주어진 배열을 두 개로 분할하고, 각각을 정렬한다.
  - 합병정렬과 동일?
  
- 다른점 1: 합병정렬은 그냥 두 부분으로 나누는 반면에, 퀵정렬은 분할할 때, 기준 아이템(pivot item) 중심으로, 이보다 작은 것은 왼편, 큰 것은 오른편에 위치시킨다.

- 다른점 2: 각 부분 정렬이 끝난 후, 합병정렬은 '합병'이란 후처리 작업이 필요하나, 퀵정렬은필요로 하지 않는다.

- 알고리즘
```python
def quickSort(a, begin, end):
    if begin < end:
        p = partition(a, begin, end)
        quickSort(a, begin, p-1)
        quickSort(a, p+1, end)

```
![img.png](img.png)