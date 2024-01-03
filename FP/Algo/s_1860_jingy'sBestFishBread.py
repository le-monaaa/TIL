import sys
sys.stdin = open("1860.txt", "r")

# SWEA 1860 진기의 최고급 붕어빵
# N명에게 0초부터 만든 붕어빵 판매. M초에 K개 생산.
# 기다림없이 제공가능한지 출력
# T/ N,M,K(1<=N,M <= 100)/ N values -> ETA

T = int(input())
for tc in range(1, T+1):
    n, m, k =  map(int, input().split()) # n:손님 수  m: 단위시간 k: m동안 만드는 붕어빵 수
    ETA = sorted(map(int, input().split())) # 도착시간 별 손님 정렬 리스트
    c = [0] *(max(ETA)+1)
    flag = 1
    for d in ETA:
        c[d] += 1
    now_bread = 0
    idx = 0
    while idx < max(ETA) + 1:
        if idx != 0 and idx%m == 0:
            now_bread += k

        if c[idx] != 0:
            # print(idx, c[idx], now_bread)
            now_bread -= c[idx]

            if now_bread <0:
                flag = 0
                break
        idx += 1

    if flag == 1:
        result = "Possible"
    else:
        result = "Impossible"

    print(f"#{tc} {result}")
