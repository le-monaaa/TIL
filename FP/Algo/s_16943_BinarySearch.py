import sys
sys.stdin = open("../16943.txt", "r")

# SWEA 16943 이진탐색
# 정수 N개를 정렬한 상태로 리스트 A에 저장. 리스트 B에 저장된 M개의 정수에 대해 A에 들어있는 수인지
# 이진탐색으로 확인. B에 속한 어떤 수가 A에 들어있으면서 동시에 탐색 과정에서 양쪽구간을 번갈아
# 선택하게 되는 숫자의 개수 알아보기.
# T/N, M/N values/M values

def binarySearch(Arr, la, target):
    l = 0
    r = la
    di = ""
    while l <= r:
        mid = (l + r) // 2
        # 이진탐색으로 찾기
        if Arr[mid] == target:
            if  "rr" in di or "ll" in di:
                return 0
            else:
                return 1
        elif Arr[mid] > target:
            r = mid -1
            di = di + "l"
        else:
            l = mid + 1
            di = di + "r"

    return 0


T = int(input())
for tc in range(1, T+1):
    la, lb = map(int, input().split()) # A, B의 길이
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    cnt = 0


    for target in B:
        if target in A: # 만약 B의 원소가 A에 있다면.
            if binarySearch(A, la-1, target):
                cnt += 1

    print(f"#{tc} {cnt}")
