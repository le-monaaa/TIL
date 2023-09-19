# SWEA 3499 퍼펙트 셔플
# 카드 덱을 절반으로 나누고 나눈 것들에서 교대로 카드를 뽑아 새로운 덱을 만드는 것
# T/N/N values
import sys
sys.stdin = open("../3499.txt", "r")

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    cards = list(input().split())
    answer = []
    if n%2 == 0:
        deck1 = cards[:n//2]
        deck2 = cards[n//2:]
        for i in range(n // 2):
            answer.append(deck1[i])
            answer.append(deck2[i])

    else:
        deck1 = cards[:n//2+1]
        deck2 = cards[n//2+1:]
        for i in range(n // 2):
            answer.append(deck1[i])
            answer.append(deck2[i])
        answer.append(deck1.pop())

    print(f"#{tc}", *answer)

