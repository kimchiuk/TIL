
try:
    num = int(input('100으로 나눌 값을 입력해: '))
    print(100 / num)

except ValueError:   # 여러개 묶어서도 가능
    print('숫자를 입력하라고')

except ZeroDivisionError:  # 하위 클래스 먼저 사용해야함
    print('왜 0을 입력하는거야??')
except:
    print('에러가 발생했어')

