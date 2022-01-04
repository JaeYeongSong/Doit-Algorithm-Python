# 세 정수를 입력받아 중앙값 구하기 1

def med3(a, b, c):
    """a, b, c의 중앙값을 구하여 반환"""
    if a >= b: # a가 b보다 같거나 크다면
        if b >= c: # b가 c보다 같거나 크다면
            return b
        elif a <= c: # c가 a보다 같거나 크다면
            return a
        else:
            return c
    elif a > c: # a가 c보다 크다면
        return a
    elif b > c: # b가 c보다 크다면
        return c
    else:
        return b

print('세 정수의 중앙값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요.: '))
b = int(input('정수 b의 값을 입력하세요.: '))
c = int(input('정수 c의 값을 입력하세요.: '))

print(f'중앙값은 {med3(a, b, c)}입니다.')