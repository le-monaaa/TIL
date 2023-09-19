import sys
sys.stdin = open("../12712.txt", "r")

# SWEA 12712 파리퇴치3
# N*N table. + 또는 x 범위의 값의 합.
# T/ N,M/ N lines N vlaues

dr1 = [-1, 1, 0, 0]
dc1 = [0, 0, -1, 1]

dr2 = [-1, -1, 1, 1]
dc2 = [-1, 1, -1, 1]

def is_valid(r, c):
    return 0<= r < n and 0<= c < n

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split()) # n: table size m: range
    table = [list(map(int, input().split())) for _ in range(n)]
    max_sum = 0
    # + 방향 최대합 구하기
    for r in range(n):
        for c in range(n):
            sum = table[r][c]
            for d in range(4):
                for k in range(1, m):
                    nr = r + dr1[d]*k
                    nc = c + dc1[d]*k
                    if is_valid(nr, nc) and table[nr][nc]:
                        sum += table[nr][nc]
            if max_sum < sum:
                max_sum = sum

    # x 방향 최대 합 구하기
    for r in range(n):
        for c in range(n):
            sum = table[r][c]
            for d in range(4):
                for k in range(1, m):
                    nr = r + dr2[d] * k
                    nc = c + dc2[d] * k
                    if is_valid(nr, nc) and table[nr][nc]:
                        sum += table[nr][nc]
            if max_sum < sum:
                max_sum = sum

    print(f"#{tc} {max_sum}")