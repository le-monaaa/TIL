# SWEA 1227 미로2
# 100*100 테이블. 1: 길 0: 벽 2: 출발점 3: 도착점// 도착시 1 도착불가능 0
# tc 10/ 100*100 table
import sys
sys.stdin = open("../ip2.txt", "r")

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(table, sr, sc):
    N = 100
    visited = [[0]*N for _ in range(N)]
    q = []
    q.append((sr,sc))
    visited[sr][sc] = 1

    while q:
        r, c = q.pop()
        if table[r][c] == 3:
            return 1
        # 조건만족x
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and table[nr][nc] != 1 and not visited[nr][nc]:
                q.append((nr,nc))
                visited[nr][nc] = 1
    return 0

T = 10
for tc in range(1, T+1):
    t = input()
    N = 100
    table = [list(map(int, input())) for i in range(N)]
    # 시작점 구하기
    for r in range(N):
        for c in range(N):
            if table[r][c] == 2:
                sr, sc = r, c

    result = bfs(table, sr, sc)

    print(f"#{tc} {result}")