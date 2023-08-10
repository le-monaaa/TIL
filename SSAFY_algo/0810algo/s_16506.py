# SWEA 16506 그래프 경로
# V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어짐.
# 특정 두개의 노드에 경로가 존재하는지 확인하는 프로그램
# 존재시 1, 없을 경우 0
# testcase/ V(노드수), E(간선수)/E개의 줄에 걸쳐 출발 도착 노드로 간선 정보 주어짐
# E개 라인 후에는 경로 유무를 확인할 출발 노드(S)와 도착노드(G)가 주어짐

import sys
sys.stdin = open("sample_input.txt", "r")

def dfs(graph, start, goal):
    visited = [] * (V+1)
    stack = []
    result = 0
    stack.append(start) # stack에 시작 노드를 담아준다

    while stack: # stack에 원소가 남아있는 동안
        node = stack.pop() # 방문할 노드를 꺼냄
        if node not in visited: # 방문했던 노드가 아니라면
            visited.append(node) # 방문리스트에 node 추가
            stack.extend(graph[node]) # 해당 노드의 자식 노드도 stack에 넣고 체크
    if S in visited and G in visited:
        result = 1

    return result
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split()) # v: 노드 수 E: 간선 수
    result = 0
    w = [[] for _ in range(V + 1)]

    for i in range(E): # 간선 수만큼 반복하면서 리스트에 담아줌
        s, e = map(int, input().split())

        w[s].append(e)
    S, G = map(int, input().split()) # S: 확인할 출발 노드 G: 도착 노드
    result = dfs(w,S,G)

    print(f"#{tc} {result}")


# 문제를 좀 읽자..
# 양방향이 아니라 단방향이었고
# 한번에 가지 않고 돌아와서 가도 인정되는 문제였다
# 이걸로 뭘한거니..