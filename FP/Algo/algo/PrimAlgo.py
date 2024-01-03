from heapq import heappop, heappush


"""
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
"""

def prim(s):
    heap = [] # 최소 힙 (루트가 최소값, 원소를 꺼내면 루트에서 꺼내므로 최소값임)

    MST = [0] * V # 내가 만들 신장 트리에 포함시킨 정점 정보
    # MST[1] = 1: 1번 정점은 신장 트리에 포함되어 있다.
    # MST[1] = 0: 1번 정점은 신장 트리에 포함되지 않았다.

    heappush(heap, (0, s))  # 시작 정점 넣고 시작 (가중치, 정점 번호)

    # 최소 신장 트리(가중치 합)
    MIN_V = 0

    while heap:
        # 가장 작은 가중치를 가진 정점을 꺼낸다.
        # 힙을 사용하면 반복문을 돌면서 최소 가중치를 가진 정점을 찾을 필요가 없음
        w, v = heappop(heap)

        # 정점 v가 현재 내가 만들고 있는 신장 트리에 이미 포함되어있다면 pass
        if MST[v]:
            continue

        # 신장트리에 포함이 되지 않은 정점 v를 꺼낸 경우 체크
        # 신장트리에 포함시킨다
        MST[v] = 1

        # 방금 꺼낸 정점과 가중치는 연결된 적이 없고, 최소 가중치를 가졌으므로 가중치 합 추가
        MIN_V += w


        # 연결된 모든 노드들을 확인
        for u in range(V):

            # u 노드가 v 노드와 인접해있지 않거나 u가 이미 신장트리에 포함이 되어있으면 pass
            if adjm[v][u] == 0 or MST[u]:
                continue

            # u 노드가 v 노드와 인접해있고, 신장트리에 포함된 적이 없으면
            # 일단 힙에 넣음(자동으로 최소 가중치를 꺼내줄 수 있도록)
            heappush(heap, (adjm[v][u], u))
            # u로 무조건 간다 x 후보군에 추가하는 것

    return MIN_V

V, E = map(int, input().split())
adjm =[[0] * V for _ in range(V)]

for _ in range(E):
    # s: 시작 정점, e: 도착 정점, w: 가중치
    s, e, w = map(int, input().split())
    adjm[s][e] = w
    adjm[e][s] = w

print(prim(0))




