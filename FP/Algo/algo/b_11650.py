# baekjoon 11650 좌표 정렬하기 https://www.acmicpc.net/problem/11650
# 2차원 평면. 점 N개. x 좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순으로 정렬, 출력
from operator import itemgetter
N = int(input())
dots = []
for n in range(N):
    x, y = map(int,input().split())
    dots.append((x,y))

dots = sorted(dots, key=itemgetter(0, 1))
for dot in dots:
    print(*dot)