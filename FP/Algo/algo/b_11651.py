# baekjoon 11651 좌표 정렬하기2 https://www.acmicpc.net/problem/11651
# 2차원 평면. 점 N개. y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순으로 정렬, 출력
from operator import itemgetter
N = int(input())
dots = []
for n in range(N):
    x, y = map(int,input().split())
    dots.append((x,y))

dots = sorted(dots, key=itemgetter(1, 0))
for dot in dots:
    print(*dot)