# SWEA 1225 암호생성기
# 8개의 숫자를 받아서 첫번째 숫자부터 뒤로 갈수록 1~5 작아짐.
# 이때 마지막 숫자가 0이 되었을 때 암호. 암호를 출력
# tc/ 8 values
import sys
sys.stdin = open("../ip1.txt", "r")

for tc in range(1, 11):
    _ = int(input())
    nums = list(map(int,input().split()))
    size = 8
    q = [0] * size
    for k in range(8):
        q[k] = nums[k]
    fr = -1
    re = size -1
    while q[re] != 0:
        for i in range(1,6):
            fr = (fr + 1)%size
            temp = q[fr] - i
            if temp <= 0:
                temp = 0
            re = (re + 1)%size
            q[re] = temp
            if q[re] == 0:
                break
    re += 1
    print(f"#{tc}",end = " ")
    for i in range(8):
        print(q[re], end= " ")
        re = (re+1)%size
    print()


