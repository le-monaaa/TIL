# 시작은 0 도착은 99 고정
# s= 시작

def dfs(s):
    # 방문 배열 만들기
    visited = [0]*100
    # 스택 만들기
    stack = []
    # 시작 정점은 방문처리 해준다
    visited[s] = 0
    # 현재 정점 번호를 i라고 한다
    i = s

    # 모든 정점을 방문할 때까지 반복
    while True:
        # 현재 정점 i가 도착지점인지 확인
        if i == 99: # 도착지점 도착
            break

        # 현재 위치 i 에서 방문할 수 있는 정점 j를 확인하고
        # 방문 가능하면 방문
        for j in range(100):
            # i 정점에서 j로 가는 길이 있고 내가 j정점을 방문한 적이 없을 때
            if adj[i][j] == 1 and not visited[j]:
                # j를 방문처리
                visited[j] = 1
                # 돌아올 위치(현재 위치) 기억
                stack.append(i)
                # 다음 위치로 이동
                i = j
                # 이전 위치로의 탐색을 중단
                break
        else: # i에서 갈 수 있는 j가 없었다.
            if stack:
                i = stack.pop() # 제일 최근 방문했던 정점으로 돌아가기
            else:
                # 갈 수 있는 정점을 모두 방문했음.
                break

    # 여기까지 코드가 실행되었는데
    # 반복이 끝나고 여기까지 오면서 현재위치가 한번도 99가 된 적이 없다
    # 반복이 끝났으니까 내가 갈 수 있는 정점은 모두 방문한 상태
    # 갈 수 있는 길이 없다.



T= int(input())
for tc in range(1, T+1):
    # E: 간선의 개수
    _, E = map(int, input().split())

    # 순서쌍을 배열로 받기
    edgs = list(map(int, input().split()))
    # 인접행렬
    adj = [[0] * 100 for _ in range(100)]
    # adj[i][j] ==> i정점에서 j정점으로 가는 길이 있는지 표현

    # 순서쌍을 통해 인접행렬 만들기
    for i in range(E):
        # 간선의 개수 *2= 정점의 개수
    adj[edgs[i*2][edgs[i*2+1]]
