# 분할 정복 & 백트래킹

설계전략
- 분할 : 해결할 문제를 여러 개의 작은 부분으로 나눈다
- 정복 : 나눈 작은 문제를 각각 해결한다
- 통합 : (필요하다면) 해결된 해답을 모은다.

반복 알고리즘 : O(n)
```
iterative_Power(x,n):
    result <- 1
    
    for i in 1 -> n
        result <- result * x
      
    return result
```

분할 정복 기반의 알고리즘 : O(log n)
```
Recursive_Power(x, n):
    if n == 1 : return x
    if n is even
        y <- Recursive_Power(x, n/2)
        return y * y
    else:
        y <- Recursive_Power(x, (n-1)/2)
        return y * y * x
```

# 병합 정렬

- 여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식
- 분할 정복 알고리즘 활용
  - 자료를 최소 단위의 문제까지 나눈 후에 차례대로 정렬하여 최종 결과를 얻어냄.
  - top-down 방식
- 시간 복잡도 : O(n log n)

- 병합 정렬 과정
  - {69, 10, 30, 2, 16, 8, 31, 22}를 병합 정렬하는 과정
  - 분할 단계: 전체 자료 집합에 대하여, 최소 크기의 부분집합이 될 때까지 분할 작업을 계속한다.
  - 병합 단계 : 2개의 부분집합을 정렬하면서 하나의 집합으로 병합
  - 8개의 부분집합이 1개로 병합될 때까지 반복함
    
- 알고리즘 : 분할 과정
```
merge_sort(LIST m):
    if length(m) == 1 : return m
    
    LIST left, right
    middle <- length(m) / 2         # 가운데
    for x in m before middle        # 왼쪽
        add x to left
    for x in m after or equal middle        # 오른쪽
        add x to right
    
    left <- merge_sort(left)
    right <- merge_sort(right)
    
    return merge(left, right)
```

- 알고리즘 : 병합 과정
```
merge(LIST left, LIST, right):
    LIST result
    
    while length(left) > 0 or length(right) > 0
        if length(left) > 0 and length(right) > 0
            if first(left) <= first(right)          # 더 작은 것을 result 배열에 넣어라
                append popfirst(left) to result
            else
                append popfirst(right) to result
        elif length(left) > 0                       # 남은 데이터를 모두 넣어라
            append popfirst(left) to result
        elif length(right) > 0
            append popfirst(right) to result
    return result
```

# 퀵 정렬
- 주어진 배열을 두 개로 분할하고, 각각을 정렬한다.
  - 병합 정렬과 동일?
- 다른점1 : 병합정렬은 그냥 두 부분으로 나누는 반면에, 퀵 정렬은 분할할 때, 기준 아이템(pivot item) 중심으로, 이보다 작은 것은 왼편, 큰 것은 오른편에 위치시킨다.
- 다른점2 : 각 부분 정렬이 끝난 후, 병합정렬은 "병합"이란 후처리 작업이 필요하나, 퀵 정렬은 필요로 하지 않는다.

- 알고리즘
```
quickSort(A[], l, r)
    if l < r
        s <- partition(a, l, r)
        quickSort(A[], l, s - 1)
        quickSort(A[], s + 1, r)
```

- Hoare-Partition 알고리즘
```
partition(A[], l, r)
    p <- A[l]
    i <- l, j <- r
    while i <= j
        while i <= j and A[i] <= p : i++
        while i <= j and A[i] >= p : j--
        if i < j : swap(A[i], A[j])
    
    swap(A[l], A[j])
    return j
```

- 아이디어
  - P(피봇)값들 보다 큰 값은 오른쪽, 작은 값들은 왼쪽 집합에 위치하도록 한다.
  - 피봇을 두 집합의 가운데에 위치시킨다.
  - 왼쪽 끝/오른쪽 끝/임의의 세개 값 중에 중간 값
    
- Lomuto partition 알고리즘
```
partition(A[], p, r)
    x <- A[r]
    i <- p - 1
    
    for j in p -> r - 1
        if A[j] <= x
            i++, swap(A[i], A[j])
    
    swap(A[i+1], A[r])
    return i + 1
```

## 병합정렬, 퀵정렬 
- 내장 라이브러기가 매우 강력 (sort(), sorted())

병합 정렬
- 직접 구현할 일은 적다.
- 과거에 면접 단골 질문 + 분할 정복 학습에 좋다
  -> 코드를 보기 전에 반드시 손으로 직접 해보기
  
퀵 정렬
- 직접 구현할 일은 적다.
- 과거에 면접 단골 질문 + 분할 정복 학습에 좋다
  -> 코드를 보기 전에 반드시 손으로 직접 해보기
  
# 이진 검색  ★★★

- 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
  - 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검새개 범위를 반으로 줄여가면서 보다 빠르게 검색을 수행함
- 이진 검색을 하기 위해서는 자료가 정렬된 상태여야 한다.

- 검색 과정
1. 자료의 중앙에 있는 원소를 고른다.
2. 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다.
3. 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색을 수행하고, 크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행한다.
4. 찾고자 하는 값을 찾을 때까지 1~3의 과정을 반복한다.

- 예) 이진 검색으로 7을 찾는 경우
  - 2 4 7 9 11 19 23
    
  1. 7 < 9 : 왼쪽 검색
  2. 7 > 4 : 오른쪽 검색
  3. 7 = 7 : 검색 성공
    
- 예) 이진 검색으로 20을 찾는 경우
  - 2 4 7 9 11 19 23
    
  1. 20 > 9 : 오른쪽 검색
  2. 20 > 19 : 오른쪽 검색
  3. 20 != 23 : 검색 실패
    
- 알고리즘 : 반복구조
```
binarySearch(n, S[], key)
    low <- 0
    high <- n - 1
    
    while low <= high
        mid <- low + (high - low) / 2
        
        if S[mid] == key
            return mid
        elif S[mid] > key
            high <- mid - 1
        else:
            low <- mid + 1
            
    return -1
```

- 알고리즘 : 재귀 구조
```
binarySearch(a[], low, high, key)
  if low > high
    return -1
  else
    mid <- (low+high) / 2
    if key == a[mid]
      return a[mid]
    elif key < a[mid]
      return binarySearch(a[], low, mid - 1, key)
    else
      return binarySearch(a[], mid + 1, high, key)
```

- 병합 정렬은 외부 정렬의 기본이 되는 정렬 알고리즘이다. 또한, 멀티코어 CPU 나 다수의 프로세서에서 정렬 알고리즘을 병렬화하기 위해 병합 정렬 알고리즘이 활용된다.
- 퀵 정렬은 매우 큰 입력 데이터에 대해서 좋은 성능을 보이는 알고리즘이다.

- 병합 정렬
  - 직접 구현할 일은 적다
    -> 멀티 쓰레드
  - 과거에 면접 단골 질문 + 분할 정복 학습에 좋다
    -> 코드를 보기 전에 반드시 손으로 직접 해보기
    
- 퀵 정렬
  - 직접 구한할 일이 적다
    -> 평균적으로 굉장히 좋음 O(NlogN)
    -> 특히, 큰 데이터를 다룰 때 좋다.
    -> 단점 : 역순 정렬 등 최악의 경우 O(N^2)
  - 과거에 면접 단골 질문 + 분할 정복 학습에 좋다.
    -> 코드를 보기 전에 반드시 손으로 직접 해보기
    
- 이진 검색
  - 코딩 테스트의 메인 알고리즘 중 하나
  - 목적 : "원하는 값을 빨리 찾는 것"
  - 시간 : O(logN)
  - Parametric Search
    - lower bound
    - upper bound
    - 여러 개의 데이터 중 2가 처음 나온 시점
    - 2~9 사이의 데이터는 몇개인가?
  
