# DFS

# 그래프의 형태를 어떤 방법으로 나타내느냐

# 1. 인접행렬 -> 2차원배열
# adj_m[][]
# 1번 정점에서 2번 정점으로 가는 길이 있다 --> adj_m[1][2] = 1
# 2번 정점에서 3번 정점으로 가는 길이 없다 --> adj_m[2][3] = 0
# S : 시작 정점 번호 V : 정점의 개수

# 현재 있는 정점에서 탐색할 수 있는 정점이 있는지 확인
# 현재 정점 i 에서 다른 정점 j로 가는 길이 있는지 어떻게 확인하는가?
# 인접 행렬 or 인접 리스트

def dfs(s, v):
    visited = [0] * v
    visited[s] = 1 # 시작 정점은 방문했다고 넣어줌
    stack = []

    print(node[s], end = " ")
    # 현재 방문한 정점을 i 라고 함
    i = s

    # 모든 정점을 방문할 때까지 확인
    while True:
        # adj_m[i][j] == 1 이면 길이 있다.
        for j in range(v):
            # 내가 이전에 j번 정점을 방문한 적이 있는지도 확인해야 함.
            if adj_m[i][j] == 1 and not visited[j]:
                # j번째 정점을 방문할 것이기 때문에 이전 정점인 i로 돌아오기 위해
                # 스택에 j를 추가
                stack.append(i)
                print(node[j], end= " ")
                # 방문했다고 처리
                visited[j] = 1
                # 현재 위치를 j로 바꾸고 다음 탐색을 시작하도록 해준다.
                i = j
                # 새로운 i 에서의 탐색을 하기 위해 break
                break
        else: # i에서 탐색해봤는데 더이상 탐색할 곳이 없더라 --> 돌아가기
                # 제일 최근에 방문했던 정점으로 돌아가기
            if stack:
                # stack에 원소가 존재 -> 돌아갈 곳이 있다
                # 하나 꺼내서 되돌아가기. i번 정점부터 탐색 시작
                i = stack.pop()
            else:
                # stack에 남은 정점이 없다 --> 탐색완료, 반복종료
                break

    return

#        A  B  C  D  E  F  G
adj_m =[[0, 1, 1, 0, 0, 0, 0], # A
        [1, 0, 0, 1, 1, 0, 0], # B
        [1, 0, 0, 0, 1, 0, 0], # C
        [0, 1, 0, 0, 0, 1, 0], # D
        [0, 1, 1, 0, 0, 1, 0], # E
        [0, 0, 0, 1, 1, 0, 1], # F
        [0, 0, 0, 0, 0, 1, 0]] # G

node = ["A", "B", "C", "D", "E", "F", "G"]
N = 7
dfs(0, N)

# i 번 정점 -> j번 정점 있다 1 없다 0 이었는데 사실 갈 수 있는 정보만 있으면 된다.
# 쓸모없는 공간이 너무 많다--> 노드에서 갈 수 있는 곳의 정보만 가지고 탐색해보자.

# 2. 인접리스트
# adj_l[i] --> i번 정점과 연결되어 있는 정점의 모음(리스트)
# adg_l[A] = [B, C]

"""
7 8
1 2 
1 3
2 4
2 5
3 7
4 6
5 6
6 7
"""

def dfs_l(s, V):
    # 초기화
    visited = [0] * (V + 1)
    stack = []
    # 시작 정점 방문처리
    i = s
    visited[i] = 1
    print(i, end = " ")

    # 모든 정점을 방문할 때까지 반복
    while True:
        # 현재 정점 i에서 갈 수 있는 정점 j 찾기
        for j in adj_l[i]: # i랑 연결되어 있는 j를 하나씩 가져옴
            # j는 i와 연결되어 있는 정점.
            # 길이 연결되어 있기 때문에 1인지 아닌지는 확인할 필요가 없다.
            if visited[j] == 0:
                stack.append(i)
                i = j # 새로운 i에서 탐색 시작하도록 바꾸기
                visited[j] = 1
                print(i, end = " ")
                break #새로운 i에서 다시 탐색해야 하므로 break
        # 현재 정점 i에서 갈 수 있는 정점이 없었다.
        else: # 돌아가기
            if stack: #stack이 비어있지 않다면 최근 저장한곳으로 돌아감
                i = stack.pop()
            else:
                break


V, E = map(int, input().split())
# V: 정점의 개수 E : 간선의 개수
adj_l = [[] for _ in range(V + 1)] # 노드 번호가 1부터 시작. 0번인덱스는 사용할 수 없기에 V+1개 생성

for i in range(E):
    # 연결이 되려면 연결시작점 s, 연결종료 e
    s, e = map(int, input().split())
    # 인접 행렬
    # adj_m[s][e] = 1
    # adj_m[e][s] = 1 # 방향이 없는 그래프는 반대로도 이어줘야 함

    # 인접 리스트
    # adj_l[s] = s 정점에서 갈 수 있는 정점들의 리스트
    adj_l[s].append(e)
    adj_l[e].append(s)

dfs_l(1, V) # 테스트케이스 입력하면 나옴~

