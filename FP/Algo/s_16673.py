# SWEA 16673 노드의 거리
# V개의 노드 개수, 양방향 E개의 간선 정보. 출발노드, 도착노드가 주어질 때 최소 몇개의 간선으로 도착할 수 있는지
# T/ V(노드수),E(간선수)/E lines node numbers/S(출발노드), G(도착노드)
import sys
sys.stdin = open("../si1.txt", "r")

def bfs(gr ,start, end):
    visited = [0] * (V+1)
    q = []
    q.append(start)
    visited[start] = 1

    while q:
        node = q.pop(0)
        for i in gr[node]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[node] + 1

    result = visited[end] - 1
    if result < 0:
        result = 0
    return result

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split()) # v: 노드수 E: 간선수

    gr = [[] for _ in range(V+1)]

    q = []

    for i in range(E):
        start, end = map(int, input().split())
        gr[start].append(end)
        gr[end].append(start)

    S, G = map(int,input().split()) # S: 출발 G: 도착

    print(f"#{tc} {bfs(gr, S, G)}")
