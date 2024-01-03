T = 10

for t in range(1, T+1):
    N = int(input())
    buildings = list(map(int, input().split()))

    # 조망권을 가지는 세대 수 count
    count = 0

    # 반복문을 통해 각 빌딩의 조망권이 확보된 세대의 갯수를 세준다.
    # 중첩 반복문 써서

    # 양 끝 두 칸은 무조건 높이가 0 -> 확인 필요 x
    for i in range(2, N-2):
        # 빌딩 하나의 높이 height
        height = buildings[i]
        for j in range(height, -1, -1): #시작 = 위에서부터 아래로, 끝 = 0, -1
            # 현재 i 번째 건물의 층수 j
            # j 층에서 양쪽 2칸을 확인 후 조망권이 있다면 count +1

            # 왼쪽 -1, -2 건물의 높이 확인, 오른쪽 +1, +2 건물의 높이 확인.
            # 현재 j 층이 왼쪽, 오른쪽 건물의 높이보다 높아야 조건 만족
            # 왼쪽 -1 -> building[i-1], 왼쪽 -2 -> buildings[i-2] .. 이런식

            if j > buildings[i-1] and j > buildings [i-2] and j > buildings[i+1] and j > buildings[i+2]:
                count += 1
            else:
                # 조건을 만족하지 못하는 경우 다음 케이스로 넘어감
                break

    print(f"#{t} {count}")