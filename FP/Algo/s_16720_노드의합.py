# 16720 노드의 합
# 완전 이진 트리의 리프 노드에 1000이하의 자연수 저장.
# 리프 노드 제외 노드에는 자식 노드에 저장된 값의 합이 저장.
# n개의 노드. 루트가 1번. L-R 증가.
# 리프 노드의 번호와 저장된 값이 주어지면 나머지 노드에 자식 노드 값의 합을 저장한 다음
# 지정한 노드 번호에 저장된 값을 출력
# 리프 노드: 루트 노드를 제외한 차수가 1인 정점(자식이 없는 노드. 단말 노드)
# T/ N,M/ lines(m개의 줄에 걸친 리프 번호와 자연수)
import sys
sys.stdin = open("16720.txt", "r")

T = int(input())
for tc in range(1, T+1):
    n, m, l = map(int, input().split())
    # n:노드 수 m: 리프 노드의 개수 l: 값을 출력할 노드 번호

    heap = [0] * (n+1)
    last = n

    # 리프 노드에 자연수 저장
    for i in range(m):
        node, num = map(int, input().split())
        heap[node] = num
    for i in range(n, 0, -1):
        sum = 0
        if heap[i] == 0:
            if i*2+1 <  n +1:
                sum += heap[i*2+1]
            sum += heap[i*2]
            heap[i] = sum


    print(f"#{tc} {heap[l]}")


