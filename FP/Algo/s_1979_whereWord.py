import sys
sys.stdin = open("../1979.txt", "r")

# SWEA 1979 어디에 단어가 들어갈 수 있을까
# N*N puzzle table. k lenght word
# T/N,K/puzzle info (0: block 1: null)

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split()) # n: size k: word len
    table = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    # 가로방향 순회
    for r in range(n):
        cnt = 0
        for c in range(n):
            if table[r][c] == 1:
                cnt += 1
            else:
                if cnt == k:
                    answer += 1
                cnt = 0
        if cnt == k:
            answer += 1

    # 세로방향 순회
    for c in range(n):
        cnt = 0
        for r in range(n):
            if table[r][c] == 1:
                cnt += 1
            else:
                if cnt == k:
                    answer += 1
                cnt = 0
        if cnt == k:
            answer += 1

    print(f"#{tc} {answer}")
