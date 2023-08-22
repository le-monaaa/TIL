"""
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
"""
N = int(input())
tree = list(map(int, input().split()))

# 인덱스가 부모노드의 번호
cleft = [0] * (N + 1)
cright = [0] * (N + 1)

for i in range(N - 1):
    p = tree[i * 2]
    c = tree[i * 2 + 1]
    if cleft[p] == 0:
        cleft[p] = c
    else:
        cright[p] = c


# 1. 전위순회 preorder V - L - R
def preorder(t):
    if t:
        # t에서 방문처리
        print(t, end=" ")
        # 왼쪽
        preorder(cleft[t])
        # 오른쪽
        preorder(cright[t])


# 2. 중위순회 inorder L - V - R
def inorder(t):
    if t:
        # 왼쪽
        inorder(cleft[t])
        # t에서 방문처리
        print(t, end=" ")
        # 오른쪽
        inorder(cright[t])


# 3. 후위순회 postorder L - R - V
def postorder(t):
    if t:
        # 왼쪽
        postorder(cleft[t])
        # 오른쪽
        postorder(cright[t])
        # t에서 방문처리
        print(t, end=" ")

preorder(1)
print()
inorder(1)
print()
postorder(1)
