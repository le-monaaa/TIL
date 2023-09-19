import sys
sys.stdin = open("../11315.txt", "r")

# SWEA 11315 오목 판정
# N*N table / 다섯 개 이상이면 YES 아니면 NO
# T/N/N lines N values

dr = [0, 1, 1, 1]
dc = [1, 1, 0, -1]

def find_omok(table):
    for r in range(n):
        for c in range(n):
            if table[r][c] == "o":
                for d in range(4):
                    cnt = 0
                    for k in range(5):
                        nr = r + dr[d] * k
                        nc = c + dc[d] * k
                        if 0 <= nr < n and 0 <= nc < n and table[nr][nc] == "o":
                            cnt += 1
                        else:
                            break
                        if cnt >= 5:
                            return "YES"
    return "NO"

# 델타 탐색 하면서 5개 이상 만나면 YES return

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    table = [list(input()) for _ in range(n)]
    answer = find_omok(table)

    print(f"#{tc} {answer}")
