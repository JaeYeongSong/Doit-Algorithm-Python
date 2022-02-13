# 10~99 사이의 난수 n개 생성하기(13이 나오면 중단)

import random

n = int(input('난수의 개수를 입력하세요.: '))

for _ in range(n):
    r = random.randint(10, 99)
    print(r, end=' ')
    if r == 13:
        print('\n프로그램을 종료합니다.')
        break
else: # for-else for문이 중간에 break문으로 끝기지 않고, 끝가지 수행되었다면 실행
    print('\n난수 생성을 종료합니다.')