dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 0이 이동할 수 있는 칸
# 1이 이동할 수 없는 벽
# 3은 도착점

arr = [[0, 0, 0, 0, 1, 3],
       [1, 1, 0, 0, 1, 0],
       [0, 0, 0, 0, 1, 0],
       [0, 1, 0, 0, 1, 0],
       [0, 1, 0, 0, 1, 0],
       [0, 0, 0, 0, 0, 0]]

# dfs로 2차원 배열 순회하기
# 인접한 정점 == 상하좌우
# 시작 행 번호 : r
# 시작 열 번호 : c
# 한 변의 길이 : n

def dfs(r, c, n):
    # 방문 체크 배열도 2차원으로 만들어야 함.
    visited = [[0] * n for _ in range(n)]
    # visited[i][j] == 0 -> (i,j) 방문한 적이 없다
    # visited[i][j] == 1 -> (i,j) 방문한 적이 있다
    stack = []
    # 시작 위치 표시
    visited[r][c] = 1

    while True:

        for i in range(n):
            for j in range(n):
                if (i,j) == (r,c):
                    print("*", end=" ")
                else:
                    print(arr[i][j], end= " ")
                print()
            print("=================")
        # 현재 위치가 도착지점인지 확인
        if arr[r][c] == 3: #도착했음
            print("도착")
            break

        # 현재위치 (r,c)에서 다음 위치로 갈 수 있나 확인
        # 상하좌우로 움직일 수 있나 확인, 움직일 수 있으면 이동
        for d in range(4):
            # 다음위치 계산
            nr = r + dr[d]
            nc = c + dc[d]
            # 계산 후에 (nr,nc) 갈 수 있는 곳인지 확인
            if 0 <= nr and 0 <= nc < n and not visited[nr][nc]:
                if arr[nr][nc] != 1: # == 0 이라고 해버리면 3에는 영영 도달X
                    # (nr, nc) 위치로 이동가능함을 확인
                    # 돌아올 위치를 stack에 append
                    stack.append((r,c)) # 돌아갈위치!!! -> r, c
                    # 방문 체크
                    visited[nr][nc] = 1
                    # (nr,nc)를 방문체크하고 현재 위치로 저장
                    r, c = nr, nc
                    # 이전에 탐색하던 r, c
                    # 새로운 위치에서 탐색하기 위해
                    break
            else: # 4방향을 모두 봤지만 갈 수 있는 곳이 없다.
                # 내가 저장했던 최근 위치로 돌아가기
                # 반드시 stack에 남은 원소가 있는지 확인 후에!!
                if stack:
                    r, c = stack.pop()
                else: # stack이 비었다.
                    break



dfs(0,0,6)