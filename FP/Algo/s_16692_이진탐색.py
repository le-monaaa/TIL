# SWEA 16692 이진탐색
# 1부터 N까지 자연수를 이진 탐색 트리에 저장.
# 왼쪽자식노드값<현재노드값<오른쪽자식노드값.
# N이 주어졌을 때 완전 이진 트리로 만든 이진 탐색 트리의 루트에 저장된 값과 N//2번 노드에 저장된 값을 출력
# T/N
import sys
sys.stdin = open("16692.txt", "r")
# 중위순회를 하면서 값 저장하기
def inor(t):
    global num
    if t:
        if t < n + 1:
            # 완전 이진트리 안에 있으면
            inor(t*2)
            # 왼쪽 L
            # v : t번 노드에서 해야 할 일
            tree[t] = num
            num += 1
            inor(t*2+1)
            # 오른쪽 R


T = int(input())
for tc in range(1, T+1):
    n = int(input()) # 저장할 자연수 범위
    tree = [0]*(n+1)
    num = 1
    inor(1)
    print(f"#{tc} {tree[1]} {tree[n//2]}")