def print_tree(root):
    if cl[root]:  #  왼쪽이 tree라면
        print_tree(cl[root])
    print(root)
    if cr[root]:  # 오른쪽이 tree 라면
        print_tree(cr[root])


def ptree(root):
    if root:
        print_tree(cl[root])
        print(root)
        print_tree(cr[root])


def pre_order(root):
    if root:
        print(root)
        pre_order(TREE[root][0])
        pre_order(TREE[root][1])

def post_order(root):
    if len(G[root]) >= 1:
        post_order(G[root][0])
    if len(G[root]) == 2:
        post_order(G[root][1])
    print(root)


N = 13
lst = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]
G = [[] for _ in range(N+1)]


print('----------좌우따로-----------------------')

cl = [0] * (N+1)
cr = [0] * (N+1)
Pr = [0] * (N+1) # 부모도 저장하자.
for i in range(0, len(lst), 2):
    p = lst[i]
    c = lst[i+1]
    Pr[c] = p
    if cl[p] == 0:
        cl[p] = c
    else:
        cr[p] = c

print(Pr,'Pr')
print(cl,'cl')
print(cr,'cr')
print('-------------탐색------------------------')


print('----------------------------------이차원--------------')
TREE = [[0,0] for _ in range(N+1)] # [왼쪽 자식노드, 오른쪽 자식노드]
# [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
for i in range(0, len(lst), 2):
    p = lst[i]
    c = lst[i+1]
    if TREE[p][0] == 0 :
        TREE[p][0] = c
    else:
        TREE[p][1] = c
print(TREE, '이차-원')

print('----------------리스트하나에 넣을 것임 ------------------')
for i in range(0, len(lst), 2):
    p = lst[i]
    c = lst[i+1]
    G[p].append(c)

print(G,'G')
# [[], [2, 3], [4], [5, 6], [7], [8, 9], [10, 11], [12], [], [], [], [13], [], []]
print_tree(1)
print('----------------------')
ptree(1)

print('--------------------------')
post_order(1)