# 16719 이진 힙
# min heap.
# 입력 순서대로 이진 최소힙에 저장하고 마지막 노드의 조상 노드에 저장된 정수의 합을 알아내는 프로그램
# T/N/N values

import sys
sys.stdin = open("16719.txt", "r")

def enq(item):
    global last
    # 마지막 자리에 원소 추가하기 위한 위치조정
    last += 1
    # 일단 삽입하고 비교하기
    heap[last] = item

    # 부모노드 < 자식노드 조건 만족을 위해 작업
    c = last
    # 부모노드의 위치는 자식노드를 2로 나눈 값
    p = c//2
    # 부모노드보다 자식노드가 작으면 자리 바꿈
    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        # 현재 위치에서 비교했으면 위치정보 갱신
        c = p
        p = c //2


T = int(input())
for tc in range(1, T+1):
    n = int(input()) # 자연수 개수
    values = list(map(int, input().split()))

    heap = [0] * (n + 1)
    last = 0

    for i in range(n):
        enq(values[i])

    # 마지막 노드의 조상 노드의 합 구하기
    sum = 0
    while last != 0:
        last //= 2
        sum += heap[last]

    print(f"#{tc} {sum}")