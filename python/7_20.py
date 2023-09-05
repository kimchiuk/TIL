# 단순 조건문 연습1 if ~ else 
# 비가 온다면 "우산을 쓰세요!"
# 아니라면 "우산을 가져가지 마세요!"

weather = '맑음'

if weather == '비':  # 비가 온다면
    print('우산을 쓰세요!')
else:   # 비가 x
    print('우산을 가져가지 마세요!')



# 단순 조건문 연습 2 if ~ else
# 성적이 60점 이상이면은 '통과!'
# 아니라면, '과락' 메세지를 출력

score = 70 # 성적

if score >= 60:  # 60 점 이상이면
    print('통과!')
else:
    print('과락!')


# 성적에 따라서
# 90점이상이면 'A'
# 80점이상 90미만 'B'
# 70점이상 80미만 'C'
# 60점이상 70미만 'D'
# 60 미만 'F'

score = 85

if score >= 90:
    print('A')
if score >= 80 and score < 90:
    print('B')
if score >= 70 and score < 80:
    print('C')
if score >= 60 and score < 70:
    print('D')
if score < 60:
    print('F')


# 복합 조건문... 연습1 if ~ elif ~ else

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:   # score < 60
    print('F')


# 중첩 조건문
# score 95점 이상이라면... '고득점 입니다!'를 추가로 출력해세요.

if score >= 90:
    print('A')
    if score >= 95:
        print('고득점입니다!')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:   # score < 60
    print('F')


# 조건문 연습 4
# 성적 80점 이상이면 3점 추가되고,
# 성적 80점 미만이라면, 1점이 추가된다고 합니다.

score = 70
point = 1000

# score 80점 이상이면 임시변수p 3을 할당하고
# 아니라면 1을 할당한다.
# 그 다음에, point 값에 p를 더해 할당한다.

if score >= 80:  
    p = 3
else:
    p = 1
point += p
print(point)


# 조건 표현식
# 조건문: 실행 코드 블럭을 사용해서 코드분기를 나누는 용도로 사용해왔다.
# 조건에 따라서 하나의 표현식 자체를 만들 수 있는 (한줄)
# => 조건표현식

변수명 = 참 if 표현식 else 거짓

p = 3 if score >= 80 else 1
point += p
# 아래로 변신

point += 3 if score >= 80 else 1   # 3항 연산자라는 표현도 사용한다.


arr = []
dir(arr)   # __iter__ 가 나온다면 순회 가능한 객체

a = dict()
dir(a)   # __iter__ 가 나옴.
