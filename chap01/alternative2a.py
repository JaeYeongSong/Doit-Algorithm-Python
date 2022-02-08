# +와 -를 번갈아 출력하기 3

print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))

for i in range(1, n // 2 + 1): # count 변수 변경
    print('+-', end='')   # +-를 n//2개의 출력

if n % 2:
    print('+', end='')    # n이 홀수일 때만 +를 출력

print()