import sys
sys.stdin = open("../7087.txt", "r")

# SWEA 6190 정곤이의 단조 증가하는 수
# 배열 내에서 [i -1]* [i] 가 단조 증가하는 수 중 최곳값 출력
# 없을 시 -1 반환
# T/N/N values

def check(num):
    num = str(num)
    for i in range(len(num)-1):
        if int(num[i]) > int(num[i+1]):
            return 0
    return 1

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))

    max = -1

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            else:
                c = nums[i] * nums[j]
                if check(c):
                    if max < c:
                        max = c

    print(f"#{tc} {max}")