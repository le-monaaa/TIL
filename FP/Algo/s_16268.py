# 16268 풍선팡2
# N*M 사이즈 테이블. 상하좌우풍선이 터졌을 때 꽃가루 합의 최댓값
# testcase/N,M/N line*M 개 각각의 꽃가루들

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(n)]

    dr = [-1, 1, 0, 0]  # 상, 하, 좌, 우
    dc = [0, 0, -1, 1]
    max_n = 0
    for r in range(n):  # 행 수 만큼 반복
        for c in range(m):  # 열 수 만큼 반복
            sum = table[r][c]
            for d in range(4):  # 상하좌우 값 찾기
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < n and 0 <= nc < n:
                    sum += table[nr][nc]
            if max_n < sum:
                max_n = sum

    print(f"#{tc} {max_n}")
