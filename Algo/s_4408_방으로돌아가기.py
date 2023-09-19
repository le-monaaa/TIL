import sys
sys.stdin =open("../4408.txt", "r")
T = int(input())
for tc in range(1, T+1):
    n = int(input()) # n: 경로 수
    corridor = [0]* 201
    for i in range(n):
        f, t = map(int, input().split())
        if t < f:
            t, f = f, t
        if t%2 == 0:
            if f%2 == 0:
                for j in range(f//2, t//2+1):
                    corridor[j] += 1
            else:
                for j in range(f//2+1, t//2+1):
                    corridor[j] += 1
        else:
            if f%2 == 0:
                for j in range(f//2, t//2+2):
                    corridor[j] += 1
            else:
                for j in range(f//2+1, t//2+2):
                    corridor[j] += 1
    print(f"#{tc} {max(corridor)}")