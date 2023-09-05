# # min1 = int(input('분을 입력하세요:'))

# # print(min1, '분은', min1 // (60 * 24), '일', (min1 // 60) % 24, '시간', min1 % 60, '분입니다.')


# #sec_1 = int(input('초를 입력하세요:'))

# #min_1 = sec_1 // 60
# #sec_1 = sec_ % 60 # 분으로 변환하고 남은 나머지

# #print(sec_1, '초(sec)는', min_1,'분(min)', sec_1,'초(sec)입니다.')

# hour = 23
# min = 59
# second = 40

# # 1001초 후의 시간으로 변경
# # 최소단위가 몇인지 파악... -> 초단위다!
# # 최소단위로 모든 값을 변환...

# HOUR_PER_SECONDS = 60 * 60  # 상수값은 대문자로...
# MIN_PER_SECONDS = 60

# seconds = (hour * 60 * 60) + (min * 60) + second + 1001
# ㄴ
# # 최소단위의 시간을 역으로 시분초 포멧으로 변경...
# hour = seconds // 3600 // 24  # or (60 * 60)
# min = seconds % (3600) // 60
# second = seconds % 60

# print(hour, min, second)

a = ['우진','시은']
a.append(메이킷)
print(a)
del a[2]
print(a)

a = ['우진','시은']
b = ['메이킷','소피아','하워드']
c = []
c = extend(a)
print(c)
