import sys

sys.stdin = open("../2817.txt", "r")


# SWEA 2817 부분 수열의 합
# N개의 자연수가 있을 때 최소 1개 이상의 수를 선택해 그 합이 K가 되는 경우의 수 구하기
# T/ N, K/ N values(1<=values<=100)

T = int(input())
for tc in range(1, T + 1):
    n, k = map(int, input().split())  # n: 자연수 개수 k: 조건 합
    nums = list(map(int, input().split()))  # n개의 자연수 배열
    cnt = 0
    # 부분집합을 구하면서 조건 만족시 카운팅.
    for i in range(1 << n): # n개만큼 반복
        sum_v = 0
        for j in range(n):
            if i & (1 << j):
                sum_v += nums[j]
                if sum_v > k:
                    break
        if sum_v == k:
            cnt += 1

    print(f"#{tc} {cnt}")