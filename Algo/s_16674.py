# SWEA 16674 미로의 거리
# N*N maze, shortcut value
# 경로 없음 0. 1: 벽, 2: 출발, 3: 도착 0: 이동가능
# T/N/N lines N values
import sys
sys.stdin = open("../si2.txt", "r")

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(table, sr, sc):
    visited = [[0] * N for _ in range(N)]

    q = []
    q.append((sr, sc))
    visited[sr][sc] = 1

    # 탈출 최소 거리 구하기
    while q:
        r, c = q.pop(0)
        # 현위치 정보 체크
        if table[r][c] == 3:
            return visited[r][c] - 2
        # 도착지점 아닐 경우 사방 탐색
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # 인덱스 유효성, 값, 방문기록 체크
            if 0 <= nr < N and 0 <= nc < N and table[nr][nc] != 1 and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
    return 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 테이블 사이즈
    maze = [list(map(int, input())) for i in range(N)]

    # 시작점 찾기
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                sr, sc = r, c

    result = bfs(maze, sr, sc)

    print(f"#{tc} {result}")