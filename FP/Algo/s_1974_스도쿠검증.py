import sys
sys.stdin = open("../1974.txt", "r")

# SWEA 1974 스도쿠 검증
# 9*9 table. T = 1, F = 0
# T/ 9 lines 9 values

T = int(input())
for tc in range(1, T+1):
    table = [list(map(int, input().split())) for _ in range(9)]

    flag = 1

    # 행 체크
    for r in range(9):
        visited = set()
        for c in range(9):
            visited.add(table[r][c])
        if len(visited) != 9:
            flag = 0

    # 열 체크
    for c in range(9):
        visited = set()
        for r in range(9):
            visited.add(table[r][c])
        if len(visited) != 9:
            flag = 0

    # 3*3 체크
    for rr in range(0,9,3):
        for cc in range(0,9,3):
            visited = set()
            for r in range(3):
                for c in range(3):
                    nr = rr + r
                    nc = cc + c
                    visited.add(table[nr][nc])
            if len(visited) != 9:
                flag = 0

    print(f"#{tc} {flag}")