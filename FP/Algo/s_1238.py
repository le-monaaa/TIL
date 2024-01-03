# SWEA 1238 contact
# 가장 마지막에 연락을 받는 사람 중 번호가 큰 사람. 단방향, 양방향 섞인 노드
# 간선 정보가 중복될 수도 있다. 못된놈들 근데 그냥 탐색할때 set 적용하면 될 것 같음
# tc 10/ 데이터 길이, 시작점/간선정보
import sys
sys.stdin = open("ip4.txt", "r")

def bfs(gr, sn): # 그래프, 시작노드
    visited = [0] * 101
    q = []

    q.append(sn)
    visited[sn] = 1

    while q:
        node = q.pop(0)

        for i in set(gr[node]):
            if not visited[i]:
                q.append(i)
                visited[i] = 1





T = 1
for tc in range(1, T+1):
    N, st = map(int, input().split()) # N: 정보의 길이(len(lines)) st: 시작점
    lines = list(map(int, input().split()))

    # visited

    contact = [[] for _ in range(101)]

    # 간선 그래프 생성
    for i in range(0, N, 2):
        contact[lines[i]].append(lines[i+1])



