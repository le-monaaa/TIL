# SWEA 1645 간단한 소인수분해
# N 이 주어질 때 2**a, 3**b, 5**c, 7**d, 11**e의 abcde를 출력
# T/N
import sys
sys.stdin = open("i1.txt", "r")

T= int(input())
for tc in range(1, T+1):
    n = int(input())
    a = b = c = d = e = 0

    while n!= 1:
        if n%2 == 0:
            a += 1
            n /= 2
        if n%3 == 0:
            b += 1
            n /= 3
        if n%5 == 0:
            c += 1
            n /= 5
        if n%7 == 0:
            d += 1
            n /= 7
        if n%11 == 0:
            e += 1
            n /= 11

    print(f"#{tc} {a} {b} {c} {d} {e}")

