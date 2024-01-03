import sys;sys.stdin = open("../17028.txt", "r")

# SWEA 17028 최소신장트리
# 0번부터 V번까지의 노드와 E개의 간선을 가진 그래프 정보가 주어질 때
# 최소신장트리를 구성하는 간선의 가중치를 모두 더해 출력
# T/V, E/ E lines n1, n2, w

def findSet(x):
    if p[x] == x:
        return x
    else:
        p[x] = findSet(p[x])
        return p[x]

def union(x, y):
    x = findSet(x)
    y = findSet(y)

    if x > y:
        p[y] = x
    else:
        p[x] = y

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split()) # V: 노드 마지막 번호(0~V번) E: 간선 수

    edge = []

    for _ in range(E):
        n1, n2, w = map(int, input().split())
        edge.append((w, n1, n2))

    # 가중치 기준 정렬
    edge.sort()

    p = [i for i in range(V+1)]

    sum_w = 0

    for w, n1, n2 in edge:
        if findSet(n1) != findSet(n2): # 둘의 루트노드가 같지 않으면
            union(n1, n2)
            sum_w += w

    print(f"#{tc} {sum_w}")


