# SWEA 1226 미로1
# 16*16 table
# tc 10/ tc/ table

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(maze, sr, sc):
    visited = [[0] * n for _ in range(n)]
    q = []

    q.append((sr, sc))
    visited[sr][sc] = 1

    while q:
        r, c = q.pop(0)
        if maze[r][c] == 3:
            return 1
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < n and maze[nr][nc] != 1 and visited[nr][nc] != 1:
                q.append((nr, nc))
                visited[nr][nc] = 1
    return 0

T = 10
for tc in range(1, T+1):
    _ = input()
    n = 16
    maze = [list(map(int, input())) for _ in range(n)]

    # 시작점찾기
    for r in range(n):
        for c in range(n):
            if maze[r][c] == 2:
                sr, sc = r, c

    result = bfs(maze, sr, sc)
    print(f"#{tc} {result}")
