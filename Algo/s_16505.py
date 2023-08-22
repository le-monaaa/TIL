# SWEA 16505 종이붙이기
# 가로*세로 길이가 10*20, 20*20 인 종이들.
# 20*N 크기의 직사각형을 테이프로 표시, 이 안에 종이를 빈틈없이 붙이는 방법
# 10의 배수인 N이 주어졌을 때, 종이를 붙이는 모든 경우의 수 갯수.
# testcase/N
import sys
sys.stdin = open("si1.txt", "r")

def paper(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return paper(n-1) + 2*paper(n-2)


T = int(input())
for tc in range(1, T+1):
    N = int(input())//10

    print(f"#{tc} {paper(N)}")
