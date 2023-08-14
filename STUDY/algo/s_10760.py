# SWEA 10760 우주선착륙
# 어느 지점에서 8개의 방향 중 중심지보다 적은 값을 가지고 있는 구역의 갯수
# T/N,M/N lines M values
import sys
sys.stdin = open("ip1.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N: 라인수 M: 한 라인에 있는 값 수

    dr = [-1, -1, -1, 0, 0, 1, 1, 1] # 좌상 상 우상 좌 우 좌하 하 우하
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]

    table = [list(map(int, input().split())) for _ in range(N)]

    total_cnt = 0
    # 범위가 되는 지점 안에서 8방향 탐색하여 조건에 맞을 경우 cnt+=1
    for r in range(N):
        for c in range(M):
            cnt = 0
            for d in range(8):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < N and 0 <= nc < M:
                    if table[nr][nc] < table[r][c]:
                        cnt += 1
            if cnt >= 4:
                total_cnt += 1

    print(f"#{tc} {total_cnt}")