'''
단순 재귀문제 X 분할정복.
지수법칙과 나머지법칙 활용( (a*b)%c = (a%c * b%c)%c
문제의 입력값이 커지면서 재귀 깊이를 늘려도 메모리 초과 에러가 발생했다.

분류조건
b%2 == 0 일 때, b%2 == 1일 때 + 나머지법칙 적용

'''


# baekjoon 1629 곱셈
# 자연수 A를 B번 곱한 수를 C로 나눈 나머지 출력
# A, B, C

'''
import sys
sys.setrecursionlimit(10**6)

def mul(num, times):
    global answer
    if times == B:
        print(num)
        return

    mul(num * A, times+1)

A, B, C = map(int,input().split())

answer = mul(A, 0)

'''
def pow(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        return (pow(a, b//2, c) ** 2) % c
    else: # b % 2 == 1인 경우
        return (pow(a, b//2, c) ** 2) * a % c


A, B, C = map(int,input().split())
print(pow(A, B, C))