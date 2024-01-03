import sys
sys.stdin = open("../2578.txt", "r")

# 사회자가 부르는 숫자 하나씩 체크
def findnum(num):
    for r in range(5):
        for c in range(5):
            if num == table[r][c]:
                table[r][c] = 99
                return

# 첫번째 행에서 빙고 확인
def check1():
    bingo = 0
    # 행에서 체크
    for r in table:
        if r.count(99) == 5:
            bingo += 1

    # 첫번째 행에서 조건성립시 해당 열 체크
    for c in range(5):
        if table[0][c] == 99:
            count = 0
            for r in range(5):
                if table[r][c] != 99:
                    break
                count += 1
            if count == 5:
                bingo += 1
    # 우측 하단 대각선 체크
    count = 0
    if table[0][0] == 99:
        for i in range(5):
            if table[i][i] != 99:
                break
            count += 1
        if count == 5:
            bingo += 1

    # 좌측 하단 대각선 체크
    if table[0][4] == 99:
        if table[1][3] == 99 and table[2][2] == 99 and table[3][1] == 99 and table[4][0] == 99:
            bingo += 1

    return bingo >= 3

table = [list(map(int, input().split())) for _ in range(5)] # 빙고판에 쓰인 숫자
n = [] # 사회자가 부르는 숫자
for _ in range(5):
    n+= list(map(int, input().split()))
cnt = 0
while cnt < 26:

    # 사회자가 부를 숫자 앞에서부터 하나씩 체크
    findnum(n.pop(0))
    cnt += 1

    # 숫자 체크 후에 빙고 확인해야함.
    # 3줄 이상 되면 종료.
    if cnt >= 5:
        if check1():
            break

print(cnt)
