import sys; sys.stdin = open("../16977.txt", "r")

# SWEA 16977 전기버스2
# 교체용 충전지(또 각자 사용할 수 있는 거리 다름(왜?))가 중간중간 있는데 최소 교체 횟수 구하기
# T/N, N-1 values

def elecBus(stop, now_changed):
    global min_change
    # 종료
    if stop >= N:
        if min_change > now_changed:
            min_change = now_changed
        return

    # 반복
    available_range = stops[stop]
    available_stops = range(stop+1, stop + available_range + 1)
    for s in available_stops:
        now_changed += 1
        if now_changed < min_change:
            elecBus(s, now_changed)
        now_changed -= 1


T = int(input())
for tc in range(1, T+1):
    info = list(map(int, input().split()))
    N = info[0]
    stops = [0] + info[1:]

    # 현위치로부터 이동 가능 거리 범위 내의 충전기 탐색
    # 리스트에서 하나씩 체크
    # 만약 이동가능하지만 이전에 갱신된 최소 충전횟수보다 크면 x
    min_change = 12323123123123142313123123

    elecBus(1, 0)

    print(f"#{tc} {min_change - 1}")
