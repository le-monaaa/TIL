import sys
sys.stdin = open("4408.txt", "r")

# SWEA 4408 자기 방으로 돌아가기
# 최소 몇 단위시간만에 모든 학생이 방으로 돌아갈 수 있는지 구하기.

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # N: 학생 수
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = [0] * 201 # 방 사이 공간을 지나는 사람 수(복도)
    for a, b in arr: # a<= b 라는 보장이 없음!
        # 인덱스 에러 방지를 위해
        a = (a+a%2)//2
        b = (b+b%2)//2
        for i in range(min(a, b), max(a,b)+1): # 둘 중 작은데서 큰데로 이동할 것
            cnt[i] += 1
    print(f"#{tc} {max(cnt)}")

    # 나 이게 왜 이렇게 되는 지 이해가 안 감