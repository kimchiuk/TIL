# 비트연산

- 연산자
  - & : 비트단위로 AND 연산을 한다.
    예) num1 & num2
  - | : 비트단위로 OR 연산을 한다.
    예) num1 | num2
  - ^ : 비트단위로 XOR 연산을 한다. (같으면 0 다르면 1)
    예) num1 ^ num2
  - ~ : 단항 연산자로서 피연산자의 모든 비트를 반전시킨다.
    예) ~ num
  - << : 피연산자의 비트 열을 왼쪽으로 이동시킨다.
    예) num << 2
  - \>> : 피연산자의 비트 열을 오른쪽으로 이동시킨다.
    예) num >> 2
    
- 1 << n
  - 2^n 의 값을 갖는다.
  - 원소가 n개일 경우의 모든 부분집합의 수를 의미한다.
  - Power set (모든 부분 집합)
    - 공집합과 자기 자신을 포함한 모든 부분집합
    - 각 원소가 포함되거나 포함되지 않는 2가지 경우의 수를 계산하면 모든 부분집합의 수가 계산된다.
    
-i & (1 << j)
  - 계산 결과는 i의 j번째 비트가 1인지 아닌지를 의미한다.

- 비트 연산 예제1
```python
def Bbit_print(i):
    output = ''
    for j in range(7, -1, -1):
        output += '1' if i & (1 << j) else '0'
    print(output)
    
for i in range(-5, 6):
    print('%3d = ' & i, end= '')
    Bbit_print(i)
```

- 비트 연산 예제2
```python
def Bbit_print(i):
    output = ""
    for j in range(7, -1, -1):
        output += "1" if i & (1 << j) else '0'
    print(output, end=' ')

a = 0x10
x = 0x01020304
print('%d = ' % a, end='')
Bbit_print(a)
print()
print('0%X = ' % x, end='')
for i in range(0, 4):
    Bbit_print((x >> i*8) & 0xff)
```

- 엔디안(Endianness)
  - 컴퓨터의 메모리와 같은 1차원 공간에 여러 개의 연속된 대상을 배열하는 방법을 의미하며 HW 아키텍쳐마다 다르다.
  - 주의 : 속도 향상을 위해 바이트 단위와 워드 단위를 변환하여 연산 할 때 올바로 이해하지 않으면 오류를 발생 시킬 수 있다.
  - 엔디안은 크게 두 가지로 나뉨
    - 빅 엔디안
      - 보통 큰 단위가 앞에 나옴. 네트워크
    - 리틀 엔디안
      - 작은 단위가 앞에 나옴. 대다수 데스크탑 컴퓨터
    
- 엔디안 확인 코드
```python
import sys

print(sys.byteorder)
```

- 비트 연산 예제3
```python
def ce(n):  # change endian
    p = []
    for i in range(0, 4):
        p.append((n >> (24 - i * 8)) * 0xff)
    return p

def ce1(n):
    return (n << 24 & 0xff000000 | (n << 8 & 0xff0000) | n >> 8 & 0xff00 | (n >> 24 & 0xff))

x = 0x01020304
p = []
for i in range(0, 4):
    p.append((x >> (i*8)) & 0xff)

print('x = %02x%02x%02x%02x%02x' % (p[0], p[1], p[2], p[3]))
p = ce(x)
print('x = %02x%02x%02x%02x%02x' % (p[0], p[1], p[2], p[3]))

print(hex(ce1(x)))
```

- 비트 연산 예제4
  - 비트 연산자 ^를 두 번 연산하면 처음 값을 반환한다.
    
# 진수
- 2진수, 8진수, 10진수, 16진수

- 10진수 -> 타 진수로 변환
  - 원하는 타진법의 수로 나눈 뒤 나머지를 거꾸로 읽는다.
  - 예제) (149)10 = (10010101)2
            = (225)8
            = (95)16
    
  - 타 진수 -> 10 진수로 변환
    - 예) (135)8 = 1 * 8^2 + 3 * 8^1 + 5 * 8^0 = 93 (10진법)
    - 소수점이 있을 때의 예)
      - (135.12)8 = 1 * 8^2 + 3 * 8^1 + 5 * 8^0 + 1 * 8^-1 + 2 * 8^-2 = 93.15625 (10진법)
    
  - 2진수, 8진수, 16진수간 변환
    
- 컴퓨터에서의 음의 정수 표현 방법
  - 1의 보수 : 부호와 절대값으로 표현된 값을 부호 비트를 제외한 나머지 비트들을 0은 1로, 1은 0로 변환한다.
    -6: 1 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 : 부호와 절대값 표현
    -6: 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 1 : 1의 보수 표현
    
  - 2의 보수 : 1의 보수방법으로 표현된 값을 최하위 비트에 1을 더한다.
    -6: 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 0 : 2의 보수 표현
    

# 실수
- 실수의 표현
  - 소수점 이하 4자리를 10진수로 나타내보면
  - 컴퓨터는 실수를 표현하기 위해 부동 소수점(floating-point) 표기법을 사용한다.
  - 부동 소수점 표기 방법은 소수점의 위치를 고정시켜 표현하는 방식이다.
    - 소수점의 위치를 왼쪽의 가장 유효한 숫자 다음으로 고정시키고 밀수의 지수승으로 표현
      1001.0011 -> 1.0010011 x 2^3    
  - 컴퓨터는 실수를 근사적으로 표현한다.
    - 이진법으로 표현할 수 없는 형태의 실수는 정확한 값이 아니라 근사 값으로 나타낸다   

- 실수를 저장하기 위한 형식
  - 단정도 실수(32비트)
  - 배정도 실수(64비트)
    - 가수부(mantissa) : 실수의 유효 자릿수들을 부호화된 고정 소수점으로 표현한 것
    - 지수부(exponent) : 실제 소수점의 위치를 지수 승으로 표현한 것
    
- 단정도 실수의 가수 부분을 만드는 방법
  - 예: 1001.0011
    - 정수부의 첫 번째 자리가 1이 되도록 오른쪽으로 시프트
    - 소수점 이하를 23비트로 만든다.
    - 소수점 이하만을 가수 부분에 저장
    - 지수 부분은 시프트 한 자릿수 만큼 증가 또는 감소
    - 지수부에는 8비트가 배정(256개의 상태를 나타낼 수 있음)
    - 숫자로는 0-255까지 나타낼 수 있지만, 음수 값을 나타낼 수 있어야 하므로 익세스 (excess) 표현법을 사용
      - 익세스 표현법 : 지수부의 값을 반으로 나누어 그 값을 0으로 간주하여 음수지수와 양수지수를 표현하는 방법
    
- 파이썬에서의 실수 표현 범위를 알아보자
  - 파이썬에서는 내부적으로 더 많은 비트를 사용해서 훨씬 넓은 범위의 실수를 표현할 수 있다.
  - 최대로 표현할 수 있는 값은 약 1.8 X 10^308 이고 이 이상은 inf 로 표현
  - 최소로 표현할 수 있는 값은 약 5.0 X 10^-324 이며, 이 이하는 0으로 표현
    
