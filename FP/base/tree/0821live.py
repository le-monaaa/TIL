"""
V
부모 자식
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
"""
def preorder(n):
    if n:
        print(n)
        preorder(ch1[n])
        preorder(ch2[n])



V = int(input()) # 정점수 혹은 마지막 정점 번호
arr = list(map(int, input().split()))

# 부모를 인덱스로 자식을 저장
ch1 = [0] * (V+1)
ch2 = [0] * (V+1)
for i in range(V):
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0: # 자식1이 아직 없으면
        ch1[p] = c
    else:
        ch2[p] = c


