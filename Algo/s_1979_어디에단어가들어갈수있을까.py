# SWEA 1979 어디에 단어가 들어갈 수 있을까
# N*N table word puzzle. k길이의 단어가 들어갈 수 있는 자리의 수를 출력
# T/N,K/table, 0:F 1: T
import sys
sys.stdin = open("1979.txt", "r")

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split()) # n: table size k: length of word
    table = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
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
