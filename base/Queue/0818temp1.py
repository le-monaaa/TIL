def bfs(sti, stj, N):
    # visited 생성
    visited =[[0]*N for _ in range(N)]
    # 큐 생성
    q = []
    # 시작점 인큐
    q.append((sti, stj))
    visited[sti][stj] = 1
    while q:
        i, j = pop(0) # pop()하면 stack이 되고 dfs가됩니당
        if maze[i][j] == 3:
            return visited[i][j]-2
        # 인접하고 인큐된 적이 없으면
        # 인큐ㅡ 인큐표시
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i +di, j + dj
            if 0 <= ni< N and 0 <= nj<N and maze[ni][nj] != 1 and visited[ni][nj] ==0:
                q.append((ni,nj))
                visited[ni][nj] = visited[i][j] +1
    return 0 # 3인 칸에 도착할 수 없는 경우

    # 시작점 인큐 표시

def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i,j

T = int(input())
for tc in range(1, T+1):
    N =int(input())
    maze = [list(map(int, input().split())) for _ in range(N)]
    sti, stj = find_start(N)
    ans = bfs(sti, stj,N)
    print(f"{tc} {ans}")