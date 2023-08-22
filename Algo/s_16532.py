# N*N table/ 도착 1 else 0
# 0: 길 1: 벽 2: 출발지점 3: 도착지점
# T/N/table

import sys
sys.stdin = open("si0.txt", "r")

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(table, sr, sc):
    visited = [[0] * N for _ in range(N)]
    q = []

    q.append((sr, sc))
    visited[sr][sc] = 1

    while q:
        r,c = q.pop()

        if maze[r][c] == 3:
            return 1

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0<= nc < N and table[nr][nc] != 1 and visited[nr][nc] != 1:
                q.append((nr,nc))
                visited[nr][nc] = 1

    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]


    # 시작점 찾기
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                sr, sc = r, c


    result = bfs(maze, sr, sc)
    print(f"#{tc} {result}")