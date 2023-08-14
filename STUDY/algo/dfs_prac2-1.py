graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]
def dfs2(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end=" ")
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]: # graph[v]에서 i를 순차적으로 가져오는데
        if not visited[i]: # visited[i]가 False ==> 방문한적없음
            dfs2(graph, i, visited) # 재귀적으로 해당 노드를 방문하는 함수 호출

# 1차원 리스트로 각 노드의 방문 정보 저장
size = len(graph)
visited = [False] * size

# 정의된 DFS 함수 호출
dfs2(graph, 1, visited)
