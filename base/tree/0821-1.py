def preorder(t):
    global count
    if t != 0:
        # V - L - R
        count += 1
        preorder(cleft[t])
        preorder(cright[t])


T = int(input())

for tc in range(1, T + 1):
    E, N = map(int, input().split())

    # 왼쪽 cleft[i] => i번 노드의 왼쪽 자식 노드 번호
    cleft = [0] * (E + 2)
    # 오른쪽 cright[i] => i번 노드의 오른쪽 자식 노드 번호
    cright = [0] * (E + 2)

    tree = list(map(int, input().split()))
    for i in range(E):
        p = tree[i * 2]
        c = tree[i * 2 + 1]
        # 왼쪽이 비었으면 왼쪽부터
        if cleft[p] == 0:
            cleft[p] = c
        # 왼쪽에 자식이 이미 있으면 오른쪽 자식으로
        else:
            cright[p] = c

    # N을 루트 노드로 하는 서브트리의 노드 개수
    count = 0
    preorder(N)
    print(f"#{tc} {count}")