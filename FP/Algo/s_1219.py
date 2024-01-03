# 1219 길찾기
# A도시->B도시 길 여부. 최대 2개의 갈림길, 일방통행. 돌아올 수 X
# A= 0, B = 99. 모든 길은 순서쌍으로 나타남.
# 가는 길의 수와 상관없이 한가지 길이라도 존재하면 참. 일방향길.
# tc, 간선 수/ 순서쌍~~
import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    o, n = map(int, input().split()) # o: tc / n: 간선수
    nodes = list(map(int, input().split()))
    # print(nodes)
    lines = [[] for _ in range(100)]

    # 주어진 간선 정보 저장
    for i in range(n):
        start = nodes[i*2]
        end = nodes[i*2+1]
        lines[start].append(end)

    # 방문, 스택리스트 초기화
    visited = [0] * 100 # 노드 수만큼 visited 배열 생성
    stack = [0] # 시작점 0점에서 시작.

    # stack이 빌 때 까지 visited 갱신
    while stack:
        i = stack.pop() # stack에서 pop한 위치가 현재위치 i

        if not visited[i]: # i를 방문한 적이 없다면
            visited[i] = 1 # 방문기록 남기고
            stack.extend(reversed(lines[i])) # i의 자식노드 추가.


    if visited[99] == 1:
        result = 1
    else:
        result = 0

    print(f"#{tc} {result}")



    # visited 확인해 목적지에 도달했는지 체크
