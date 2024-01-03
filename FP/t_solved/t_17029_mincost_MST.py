import sys;sys.stdin = open("../17029.txt", "r")

# SWEA 17029 최소비용
# 각 지역의 높이 데이터 테이블. 출발(0,0) 도착(N-1,N-1). 인접지역 이동하며 도착지까지 드는 최소 연료량
# 이동시 드는 연료량 = 1 + (높은 곳으로 이동 시 높이 차이만큼)
# T /N /~~

from heapq import heappop, heappush

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

INF = 100000000

def dijkstra():
    q = []
    fuel[0][0] = 0
    heappush(q, (0, 0, 0))

    while q:
        w, r, c = heappop(q)
        #
        if fuel[r][c] < w :
            continue

        # r, c와 인접한 위치 탐색
        # 4방향 탐색
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0<=nr<N and 0<=nc<N:
                # nr, nc가 r,c보다 높은지 계산
                height_diff = 0
                if arr[nr][nc] > arr[r][c]:
                    height_diff = arr[nr][nc] - arr[r][c]

                # nr, nc까지 이동하는데 사용한 연료량 = r,c까지 이동하는데 사용한 연료량 + 1 + he
                # 이전에 계산해놓은 nr,nc까지 이동하는데 사용한 연료량보다 작으면 갱신
                cost = fuel[r][c] + height_diff + 1
                if cost < fuel[nr][nc]:
                    # 새로 계산한 연료사용량이 이전보다 작으면 갱신
                    fuel[nr][nc] = cost
                    # 갱신이 일어날 때만 추가
                    heappush(q, (cost, nr, nc))
T = int(input())
for tc in range(1, T+1):
    N = int(input()) # table size
    arr = [list(map(int, input().split())) for _ in range(N)]
    fuel = [[10000000] * N for _ in range(N)]

    dijkstra()

    # 목표 지점은 (N-1, N-1)
    print(fuel)
    print(f"#{tc} {fuel[N - 1][N - 1]}")