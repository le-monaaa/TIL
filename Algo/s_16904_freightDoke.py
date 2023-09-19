import sys
sys.stdin = open("../16904.txt", "r")

# SWEA 16904 화물 도크
# 24시. 최대한 많은 화물차가 이용할 수 있는지.
# T/N/N lines s, e

T = int(input())
for tc in range(1, T+1):
    n = int(input()) # n: 신청서 수
    lst = []
    for i in range(n):
        lst.append(tuple(map(int, input().split()))) # s: 시작 시간 e: 종료 시간
    lst.sort()
    # 시작 시간이 같은 경우 비교해서 작업 시간이 더 짧은 작업 남기기
    idx = 0
    while True:
        if lst[idx][0] == lst[idx+1][0]:
            if lst[idx][1] > lst[idx+1][1]:
                lst.pop(idx)
            else:
                lst.pop(idx+1)
        idx += 1
        if idx >= len(lst)-1:
            break
    lst.sort(key = lambda x: x[1])
    time = 0
    work = 0
    # 오름차순으로 정렬한 작업 시간 하나씩 가져와서 종료 시간 이후라면 cnt +=1 하고 시간 조정.
    while lst:
        s, e = lst.pop(0)
        if s >= time:
            work += 1
            time = e

    print(f"#{tc} {work}")
