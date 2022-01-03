# 세 정수를 입력받아 최댓값 구하기

print('세 정수의 최댓값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요.: '))
b = int(input('정수 b의 값을 입력하세요.: '))
c = int(input('정수 c의 값을 입력하세요.: '))

maximum = a
if b > maximum: # b가 a보다 크다면
    maximum = b
if c > maximum: # c가 b보다 크다면
    maximum = c

print(f'최댓값은 {maximum}입니다.')