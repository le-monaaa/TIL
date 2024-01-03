# SWEA 4047 영준이의 카드 카운팅
# S D H C 각 13장. 같은 카드 있으면 ERROR 출력
# 각 카드덱에서 몇 장이나 부족한지 출력
# T/card list
import sys
sys.stdin = open("../4047.txt", "r")

T = int(input())
for tc in range(1, T+1):
    cards = input()
    card_list = []
    # 카드 목록
    for i in range(0, len(cards), 3):
        card_list.append(cards[i:i+3])
    # 중복 값 확인
    sc, dc, hc, cc = 13, 13, 13, 13
    if len(card_list) != len(set(card_list)):
        print(f"#{tc} ERROR")
    else: # 중복 없을 경우
        for i in card_list:
            if i[0] == "S":
                sc -= 1
            if i[0] == "D":
                dc -= 1
            if i[0] == "H":
                hc -= 1
            if i[0] == "C":
                cc -= 1
        print(f"#{tc} {sc} {dc} {hc} {cc}")



