import sys
sys.stdin = open("../2819.txt", "r")

# SWEA 2819 격자판의 숫자 이어붙이기
# 4*4 table. 0~9 values.
# 동서남북 인접 격자로 여섯 번 움직이면서 각 칸에 적혀있는 숫자를 모두 붙이면 7자리 숫자 됨
# 벗어나는 이동 X, 만들 수 있는 서로 다른 수들의 개수
# T/ 4 lines 4 values

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(visited, r, c):
    if len(visited) == 7:
        routes.add(visited)
        return
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < n and 0 <= nc < n:
            dfs(visited+ table[nr][nc], nr, nc)
    return

T = int(input())
for tc in range(1, T+1):
    n = 4
    table = [input().split() for _ in range(n)]

    routes = set()

    # 시작점
    for r in range(n):
        for c in range(n):
            visited = ""
            dfs(visited, r, c)

    print(f"#{tc} {len(routes)}")
