graph1 = {
    "A" : ["B"],
    "B" : ["A", "C", "H"],
    "C" : ["B", "D"],
    "D" : ["C","E","G"],
    "E" : ["D", "F"],
    "F" : ["E"],
    "G" : ["D"],
    "H" : ["B", "I", "J", "M"],
    "I" : ["H"],
    "J" : ["H", "K"],
    "K" : ["J", "L"],
    "L" : ["K"],
    "M" : ["H"]
}

def dfs1(graph, start_node):
    visited = [] # 방문한 노드를 담을 배열
    stack = [] # 정점과 인접한 방문 예정 노드 담을 배열

    stack.append(start_node) # stack에 시작 노드를 담아준다.

    while stack: # stack이 차 있는 동안(더이상 방문할 노드가 없을 동안)
        node = stack.pop() # 방문할 노드를 하나씩 꺼냄

        if node not in visited: # 방문했던 노드가 아니라면
            visited.append(node) # visited 에 추가 (방문했음)
            # stack.append(graph[node]) # 해당 노드의 자식 노드로 추가
            stack.extend(reversed(graph[node])) # 왼쪽부터 순회
            # pop으로 마지막 원소부터 뽑아가니까 반대로 저장해야하는것!!

    print("dfs = ", visited)
    return visited

dfs1(graph1, "G")