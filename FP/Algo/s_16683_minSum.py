import sys
sys.stdin = open("../26883.txt", "r")

# SWEA 16883 최소 합
# N*N table. 이동은 오른쪽, 아래만 가능. 지나는 칸의 합계가 최소가 되도록.
# T/N/N line N values

dr = [0, 1] # 우, 하
dc = [1, 0]

def find_min_road(r, c, sum_v):
    # 종료조건
    if r == n-1 and c == n-1:
        sum_v += table[r][c]
        sum_list.append(sum_v)
        return
    # 아닐 경우 이동
    sum_v += table[r][c]
    for d in range(2):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0<= nr < n and 0<= nc < n:
            find_min_road(nr, nc, sum_v)

T = int(input())
for tc in range(1, T+1):
    n = int(input()) # table size
    table = [list(map(int, input().split())) for _ in range(n)]
    sum_list = []
    road_list = []

    # 재귀로..?
    find_min_road(0, 0, 0)
    answer = min(sum_list)
    print(f"#{tc} {answer}")


