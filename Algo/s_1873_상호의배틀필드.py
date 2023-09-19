# SWEA 1873 상호의 배트필드
# . 평지(이동가능)/ * 벽돌/ # 강철/ - 물(진입불가)/ ^v<> 각각 상하좌우를 바라보는 전차
# U up D down L left R right 각각 해당방향으로 방향을 바꾸고 평지라면 한 칸 전진. S shoot 현재방향으로 포탄발사
# 맵 밖이라면 이동x. 포탄발사-벽돌(*),강철(#)을 만나거나 맵 밖으로 나갈때까지 직진.
# 포탄 + 벽돌벽-> 평지. 포탄 + 강철벽 -> 포탄만 소멸. 모든 입력 후 맵이 어떻게 되는지 출력
# T/H,W/H lines W length string/N
import sys
sys.stdin = open("../1873.txt", "r")

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def is_valid(r,c):
    return 0<=r<h and 0<=c<w

T = int(input())
for tc in range(1, T+1):
    h, w = map(int,input().split()) # h: 높이 w: 너비
    field = [list(input()) for _ in range(h)]
    n = int(input()) # n: 입력의 수
    do = input() # do: 입력값

    # 시작 위치 찾기
    for r in range(h):
        for c in range(w):
            if field[r][c] in "<>^v":
                sr, sc = r, c
    # 바라보는 방향 찾기
    now = field[sr][sc]
    if field[sr][sc] == "^":
        d = 0
        now = "^"
    elif field[sr][sc] == "v":
        d = 1
        now = "v"
    elif field[sr][sc] == "<":
        d = 2
        now = "<"
    elif field[sr][sc] == ">":
        d = 3
        now = ">"
    # 입력값대로 연산
    r, c = sr, sc
    for k in do:
        if k == "U":
            d = 0
            nr = r + dr[d]
            nc = c + dc[d]
            if is_valid(nr,nc) and field[nr][nc] == ".":
                field[r][c] = "."
                r, c = nr, nc
            now = "^"
            field[r][c] = now
        elif k == "D":
            d = 1
            nr = r + dr[d]
            nc = c + dc[d]
            if is_valid(nr, nc) and field[nr][nc] == ".":
                field[r][c] = "."
                r, c = nr, nc
            now = "v"
            field[r][c] = now
        elif k == "L":
            d = 2
            nr = r + dr[d]
            nc = c + dc[d]
            if is_valid(nr, nc) and field[nr][nc] == ".":
                field[r][c] = "."
                r, c = nr, nc
            now = "<"
            field[r][c] = now
        elif k == "R":
            d = 3
            nr = r + dr[d]
            nc = c + dc[d]
            if is_valid(nr, nc) and field[nr][nc] == ".":
                field[r][c] = "."
                r, c = nr, nc
            now = ">"
            field[r][c] = now
        elif k == "S":
            rr, cc = r, c
            while True:
                nr = rr + dr[d]
                nc = cc + dc[d]
                if is_valid(nr,nc):
                    if field[nr][nc] == "*":
                        field[nr][nc] = "."
                        break
                    if field[nr][nc] == "#":
                        break
                    rr, cc = nr, nc
                else:
                    break

    print(f"#{tc}", end=" ")
    for i in range(h):
        for j in range(w):
            print(field[i][j],end="")
        print()