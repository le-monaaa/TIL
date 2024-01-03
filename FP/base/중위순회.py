import sys
sys.stdin = open("1231.txt", "r")

# 트리를 중위 순회하는 함수
def in_order(a):  # 중위 순회
    if a <= N:
        in_order(a * 2)  # 왼쪽 자식 노드
        print(tree[a], end='')  # 루트
        in_order(a * 2 + 1) # 오른쪽 자식 노드


for tc in range(1, 2):
    N = int(input())  # N: 총 정점의 수
    tree = [[0] for _ in range(N + 1)]
    for i in range(N):
        line = input().split()
        print(f"line[0] = {line[0]}, line[1] = {line[1]}")
        tree[int(line[0])] = line[1]
    print(f'#{tc} ', end='')
    in_order(1)
    print()