# SWEA 원재의 메모리 복구하기
# bit를 수정하면 뒤의 값이 같은 값으로 덮어씌워짐
# 원상태가 주어졌을때 모든 bit가 0인 상태에서 원래대로 돌아가려면 최소 몇번 수정해야하는지
# T/original memory
import sys
sys.stdin = open("1289.txt", "r")

T = int(input())
for tc in range(1, T+1):
    origin = list(map(int, input()))
    now = 0
    cnt = 0
    for i in origin:
        if i == now:
            pass
        else:
            now = i
            cnt += 1

    print(f"#{tc} {cnt}")

