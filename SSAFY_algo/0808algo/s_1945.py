# 1945 간단한 소인수분해
# N = 2**a * 3**b * 5**c * 7**d * 11**e
# testcase/ num/ a b c d e 출력

T = int(input())
for tc in range(1, T+1):
    num = int(input())

    a = b = c = d = e = 0

    while num != 1:  # 숫자가 1이 되면 탈출
        if num % 11 == 0:
            num //= 11
            e += 1
        elif num % 7 == 0:
            num //= 7
            d += 1
        elif num % 5 == 0:
            num //= 5
            c += 1
        elif num % 3 == 0:
            num //= 3
            b += 1
        elif num % 2 == 0:
            num //= 2
            a += 1

    print(f"#{tc} {a} {b} {c} {d} {e}")
