
try:
    num = int(input('100으로 나눌 값을 입력해: '))
    print(100 / num)

except BaseException:
    print('숫자를 입력하라고')

except ZeroDivisionError: #baseException 의 하위 클래스라서 죽어버림.
    print('왜 0을 입력하는거야??')
except:
    print('에러가 발생했어')

