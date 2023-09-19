import sys
sys.stdin = open("../16942.txt", "r")

# SWEA 16942 퀵 정렬
# N개의 정수를 정렬해 리스트 A에 넣고 A[N//2]에 저장된 값 출력
# T/N/Ai
def partition(A, left, right):
    p = A[left]
    i, j = left, right

    while i <= j:
        while i <= j and A[i] <= p:
            i += 1
        while i <= j and A[j] >= p:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]

    A[left], A[j] = A[j], A[left]

    return j

def quickSort(Arr, left, right):
    if left < right:
        if left < right:
            s = partition(Arr, left, right)
            quickSort(Arr, left, s-1)
            quickSort(Arr, s+1, right)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    quickSort(A, 0, N-1)
    print(f"#{tc} {A[N//2]}")