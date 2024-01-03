# 테스트 케이스를 입력받는다
T = int(input())


# 플레이어의 현재 패 상황을 받아 run, triple을 판정하는 함수
def check(player):
    # 매개변수에 p1 또는 p2를 전달받는다.
    # 어느쪽이든 카드가 늘어난 순간 triplet이나 run을 검사한다.
    # triplet -> p1 또는 p2를 순서대로 탐색하면서 해당 값이 3이 있는지 확인한다.
    for p in player:
        if p == 3:
            return True
    # run -> p1 또는 p2를 인덱스로 탐색하면서 0-2, 1-3, 2-4 묶음이 모두 1 이상인지 확인한다.
    for j in range(len(player) - 2):  # 맨 뒤 2개의 인덱스는 에러남
        if player[j] and player[j+1] and player[j+2]:
            # 값의 존재 여부를 확인하므로 조회만 해도 됨 (0이 아닌지만 검사)
            return True
    return False  # 어차피 결과가 None이라 안해줘도 됨


# 테스트 케이스만큼 반복한다
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    # 테스트케이스 별로 12장의 카드 순서 정보를 전달 받는다. (order)
    order = list(map(int, input().split())) # 순회를 돌 것이기 때문에 list 변환 필요
    # 플레이어별로 가지고 있는 카드 번호별 수를 나타내는 리스트를 만든다. (p1, p2)
    p1 = [0] * 10  # 각각의 인덱스가 숫자에 대응한다 (0~9)
    p2 = [0] * 10
    # 숫자인덱스(i)를 통해 반복문으로 order를 탐색한다.
    for i in range(len(order)):  # 인덱스를 쓰인 이유는 짝수번/홀수번을 판단하기 위해서
        card = order[i] # 순서의 i번째 카드는 편의상 card 변수에 할당
        # i가 0, 2, 4, … 짝수이면 p1에 해당 숫자 카드(card)를 +1 한다.
        if not i % 2: # if i % 2 == 0 과 동일한 코드
            p1[card] += 1
            if check(p1):
                print(1)
                break
        # i가 1, 3, 5, … 홀수이면 p2에 해당 숫자 카드(card)를 +1 한다.
        if i % 2: # if i % 2 == 1 과 동일한 코드
            p2[card] += 1
            if check(p2):
                print(2)
                break
        # triplet 또는 run이 확인된다면 그 플레이어의 승리다.
    else:
        # order를 정상적으로 모두 탐색했는데도 승자가 안 나온다면 무승부(0)을 출력한다.
        print(0)