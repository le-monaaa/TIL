import sys;sys.stdin = open("17015.txt", "r")

# SWEA 17015 그룹 나누기
# T/N, M/M*2 values


def findSet(x):
    global temp
    if p[x] == x:
        return x
    else:
        return findSet(p[x])

def union(x, y):
    x = findSet(x)
    y = findSet(y)

    if x == y:
        return

    if x < y:
        p[y] = x

    else:
        p[x] = y

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    p = [i for i in range(N+1)]

    line = list(map(int, input().split()))

    for i in range(0, len(line), 2):
        union(line[i], line[i+1])
    s1 = set()

    for i in range(N+1):
        s1.add(findSet(i))


    print(f"#{tc} {len(list(s1))-1}")


