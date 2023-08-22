
# 노드 저장
n = int(input()) # n:간선수
tree = list(map(int, input().split()))

# 부모노드 번호 인덱스로 저장하기

cleft = [0] * (n+1)
cright = [0] * (n+1)

for i in range(n-1):
    p = tree[i*2] # 부모노드
    c = tree[i*2+1] # 자식노드
    if cleft[p] == 0: # 만약 자식 배열의 인덱스(부모노드인덱스)가 비어있으면
        cleft[p] = c # p(부모노드)의 왼쪽 자식 노드가 등록되어있지 않으면 등록
    else: # 왼쪽은 이미 있다
        cright[p] = c # 그럼 오른쪽~


# 전위순회 V - L - R
def preorder(t):
    if t: # t가 존재하는 동안
        # t에서 방문처리
        print(t, end=" ")
        # 왼쪽 자식 노드
        preorder(cleft[t])
        # 오른쪽 자식 노드
        preorder(cright[t])

# 중위순회 L - V - R
def inorder(t):
    if t: # t가 존재하는 동안
        # 왼쪽 자식 노드
        inorder(cleft[t])
        # t에서 방문처리
        print(t, end=" ")
        # 오른쪽 자식 노드
        inorder(cright[t])

# 후위순회 V - R -L
def postorder(t):
    if t: # t가 존재하는 동안
        # 왼쪽 자식 노드
        postorder(cleft[t])
        # 오른쪽 자식 노드
        postorder(cright[t])
        # t에서 방문처리
        print(t, end=" ")

