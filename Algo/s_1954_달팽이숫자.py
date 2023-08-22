# 1954 달팽이숫자

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    snail = [[0] * n for _ in range(n)]
    num = 1
    r, c = 0, 0
    d = 0

    for i in range(n*n):
        snail[r][c] = num

        nr = r + dr[d]
        nc = c + dc[d]

        if 0<=nr<n and 0<=nc<n and snail[nr][nc] == 0:
            r, c = nr, nc
        else:
            d = (d+1)% 4
            r = r + dr[d]
            c = c + dc[d]
        num += 1

    print(f"#{tc}")
    for i in range(n):
        print(*snail[i])