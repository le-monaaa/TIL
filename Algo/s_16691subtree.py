# SEWA 16691 subtree
# 주어진 이진 트리에서 노드N을 루트로 하는 서브 트리에 속한 노드의 개수를 출력
# 부모가 없는 노드가 전체의 루트 노드.
# T/E,N/E lines value
import sys
sys.stdin = open("16691.txt", "r")

def preorder(t):
    global cnt
    if t != 0: # 기준 노드가 0이 아니라면
        # V - L - R
        cnt += 1
        preorder(c1[t])
        preorder(c2[t])
T = 1
for tc in range(1, T+1):
    e, n = map(int, input().split()) # e: 간선 수 n: 루트 노드
    tree = list(map(int, input().split()))

    c1 = [0]*(e+2)
    c2 = [0]*(e+2)
    parent =[0] * (e+2)

    for i in range(e):

        p = tree[i*2]
        c = tree[i*2+1]
        # 자식노드를 왼쪽부터 저장
        if c1[p] == 0:
            c1[p] = c
        # 왼쪽이 이미 있으면 오른쪽에 저장
        else:
            c2[p] = c
        parent[c] = p

    # n을 루트 노드로 하는 서브트리의 노드 개수
    cnt = 0
    preorder(n)
    print(f"#{tc} {cnt}")