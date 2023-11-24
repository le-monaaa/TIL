import sys
sys.stdin = open("16944.txt", "r")

# SWEA 병합 정렬
# 병합정렬로 오름차순 정렬
# N개의 정렬 대상을 가진 리스트 L을 분할시 L[:N//2], L[N//2:]으로 분할,
# 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수 출력.
# T/N/N values //output: tc, Arr[N//2], 경우의수

def merge(l, r):
    result = []
    lf, rf = 0, 0

    global cnt
    if l[-1] > r[-1]:
        cnt += 1

    while rf<len(r) or lf<len(l):
        lr = len(r)
        ll = len(l)
        if rf<len(r) and lf<len(l):
            if l[lf] <= r[rf]:
                result.append(l[lf])
                lf += 1
            else:
                result.append(r[rf])
                rf += 1
        elif rf<len(r):
            return result + r
        elif lf<len(l):
            return result + l
    return result

def mergeSort(Arr):
    size = len(Arr)

    if size == 1:
        return Arr
    # 분할
    mid = size // 2
    l, r = Arr[:mid], Arr[mid:]
    # 정복
    l = mergeSort(l)
    r = mergeSort(r)
    # 병합
    return merge(l, r)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    A = mergeSort(A)
    print(f"#{tc} {A[N//2]} {cnt}")