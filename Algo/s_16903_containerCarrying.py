import sys
sys.stdin = open("../16903.txt", "r")

# SWEA 16903 컨테이너 운반
# 화물이 실린 N개의 컨테이너를 M대의 트럭으로 A->B 운반한다.
# 컨테이너 각각의 화물 무게와 트럭 각각의 적재용량이 주어짐. A->B로 최대 M대의 트럭이 편도로 한번만 운행
# 화물의 총 중량이 최대가 되는 경우에 옮겨진 화물의 전체 무게가 얼마인지 출력.
# 하나도 못 옮기는 경우 0 출력
# T/N, M/ N weights/ M volumes

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split()) # n: 컨테이너 수 m: 트럭 수
    freights = list(map(int, input().split()))
    trucks = list(map(int, input().split()))

    freights.sort(reverse=True)
    trucks.sort(reverse=True)
    now = 0
    weight = 0
    while freights:
        n_freight = freights.pop(0)
        if n_freight <= trucks[now]:
            weight += n_freight
            now += 1
        if now >= len(trucks):
            break

    print(f"#{tc} {weight}")