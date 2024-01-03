# backjoon 2798 블랙잭 https://www.acmicpc.net/problem/2798
# 카드의 합이 21을 넘지 않는 한도 내에서 합을 최대한 크게 만드는 게임.
# N장의 카드 오픈되어있는 상태에서 M이 선언되었을 때, 3장의 카드를 골라 M을 넘지 않으면서
# 최대한 가까운 수 만들기.
# N, M/N values //3장의 합 출력

def dfs(L, beginWith):
    global max_sum
    # 종료조건
    if L == 3:
        sum_cards = sum(cards)
        if sum_cards <= M and sum_cards > max_sum:
            max_sum = sum_cards

    else:
        for i in range(beginWith, len(card_list)):
            cards.append(card_list[i])
            dfs(L + 1, i + 1)
            cards.remove(card_list[i])

N, M = map(int, input().split())
card_list = list(map(int, input().split()))

max_sum = 0

cards = []

dfs(0, 0)
print(max_sum)