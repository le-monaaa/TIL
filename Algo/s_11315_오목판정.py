# SWEA 11315 오목 판정
# N*N table 오목이 된 부분이 있는지 없는지 판정
# T/N/o는 돌 .는 빈칸
import sys
sys.stdin = open("11315.txt", "r")

dr = [1, 0, 1, 1] # 아래 우측 대각선우측 대각선좌측
dc = [0, 1, 1, -1]

def omok(table):
    for r in range(n):
        for c in range(n):
            if table[r][c] == "o":
                for d in range(4):
                    for k in range(5):
                        nr = r + dr[d]*k
                        nc = c + dc[d]*k
                        if not 0 <= nr < n or not 0 <= nc < n or table[nr][nc] == ".":
                            break
                    else:
                        return "YES"

    return "NO"

T = int(input())
for tc in range(1, T+1):
    n = int(input()) # n: table size
    table = [list(input()) for _ in range(n)]

    print(f"#{tc} {omok(table)}")