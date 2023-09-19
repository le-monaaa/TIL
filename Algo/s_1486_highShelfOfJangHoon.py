import sys
sys.stdin = open("../1486.txt", "r")

# SWEA 1489 장훈이의 높은 선반
# 높이가 B인 선반. N명의 직원의 키가 주어졌을 때 B이상인 합 중 가장 최솟값 구하기
# T/N, B/ N values(H)

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split()) # N: 직원 수/B: 목적 높이
    H = list(map(int, input().split()))

    h = len(H)
    # 부분집합 구하면서 목표 합 이상이면서 현 최솟값과 비교했을 때 작으면 갱신
    min_sum = sum(H)
    for i in range(1<<h):
        now_sum = 0
        for j in range(h):
            if i & (1 << j):
                now_sum += H[j]
                if now_sum >= B:
                    if min_sum >= now_sum:
                        min_sum = now_sum
                        break
    print(f"#{tc} {min_sum - B}")
