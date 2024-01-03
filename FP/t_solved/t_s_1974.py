# 9*9 테이블. 1~9까지의 숫자가 한 번만 들어감. 3*3안에서도 1~9까지의 숫자가 한번만.
# 겹치는 숫자가 없을 경우 1. 아닐 경우 0
# T/9 * 9 array
import sys
sys.stdin = open("si3.txt", "r")

def sudoku(arr):
    for i in range(9):
        cnt = [0] * 10
        cnt2 = [0] * 10
        for j in range(9):
            cnt[arr[i][j]] += 1
            cnt2[arr[j][i]] += 1
        for k in range(1, 10):
            if cnt[k] == 0: # 1~9에 빠진 숫자가 있으면 0 리턴
                return 0
            if cnt2[k] == 0:
                return 0
    i = 0
    while i< 9:
        cnt3 = [0] * 10
        for r in range(3):
            for c in range(3):
                cnt3[arr[r][c]] += 1
        for k in range(1, 10):
            if cnt3[k] == 0:
                return 0
        else:
            i += 3

T = int(input())
for tc in range(1, T+1):

    # 입력받기
    arr = [list(map(int, input().split())) for _ in range(9)]

    ans = sudoku(arr)
    if ans == None:
        ans = 1
    print(f"#{tc} {ans}")