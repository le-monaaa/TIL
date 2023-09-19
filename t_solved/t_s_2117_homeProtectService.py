import sys
sys.stdin = open("2117.txt", "r")

T = int(input())

cost = [k * k + (k-1) * (k+1) for k in range(40) ]
for tc in range(1, T+1):
    # n : 크기, n: 집 하나당 낼 수 있는 비용
    n, m = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # 최대 집 수
    max_count = 0

    # 집 위치만 계산
    home_lst = []
    for r in range(n):
        for c in range(n):
            # r, c 위치에 집이 있었다.
            if arr[r][c] == 1:
                home_lst.append((r,c))
    # 모든 위치 (r,c) 에서 k=1 ~ k=40부터 검사
    for r in range(n):
        for c in range(n):
            # dist[k] 거리가 정확히 k일 때 포함되는 집의 개수
            dist = [0] * 40
            for hr, hc, in home_lst:
                # 거리 계산
                k = abs(r-hr) + abs(c-hc) + 1
                # 거리가 정확히 k일 때 집 개수 1 증가
                dist[k] += 1

            for k in range(1, 40):
                # 거리가 k일 때 포함되는 집의 개수 -> k-1일 때 집 개수 포함
                dist[k] += dist[k-1]
                # 운영비용보다 이익이 더 크기만 하면 최대 집 개수 갱신
                if cost[k] <= dist[k] * m:
                    max_count = max(max_count, dist[k])

    print(f"#{tc} {max_count}")