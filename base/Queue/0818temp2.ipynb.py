
def bfs(gr, st, nodes): # 그래프, 시작노드, 노드 수
    visited = [0] * (nodes+1)
    q = []
    q.append(st)
    visited[st] = 1

    while q:
        now = q.pop(0)
        for i in gr[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[now] + 1 # 방문처리 하면서 지나온 간선 개수 count


v, e = map(int,input().split()) # v : 노드 수 e 간선의 개수
gr = [[] for _ in range(v + 1)] # 인접리스트

for i in range(e): # 간선의 정보 받아서 배열 만드는 함수
    start, to = map(int, input().split())
    gr[start].append(to)
    gr[to].append(start)

bfs(gr, 1, v)
