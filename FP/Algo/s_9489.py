# SWEA 9489 고대유적
# 폭1, 길이 2 이상의 직선형태. 구조물이 있는 자리는 1로 나타남.
# N*M 테이블. 가장 긴 구조물의 길이 출력. 구조물은 직선이고 겹쳐있을 수 있음
# T/N, M/N lines M values
import sys
sys.stdin = open("ip4.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N: lines M: values
    # 행, 열 탐색하다가 1을 만났을 경우 카운트해서 최댓값보다 높으면 갱신

    table = [list(map(int, input().split())) for _ in range(N)]

    # 행 순회
    max_r = 0
    for r in range(N):
        cnt = 0
        for c in range(M):
            if table[r][c] == 1:
                cnt += 1
                if cnt > max_r:
                    max_r = cnt
            elif table[r][c] == 0:
                cnt = 0


    # 열 순회
    for c in range(M):
        cnt = 0
        for r in range(N):
            if table[r][c] == 1:
                cnt += 1
                if cnt > max_r:
                    max_r = cnt
            elif table[r][c] == 0:
                cnt = 0

    print(f"#{tc} {max_r}")