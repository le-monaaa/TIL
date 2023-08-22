# SWEA 1859 백만장자 프로젝트
# 연속된 N일 간의 물건의 매매가 주어짐. 하루에 최대 1만큼 구입 가능. 판매는 제한x
# T/N/N개의 자연수(매매가)
# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    days = int(input())
    sales = list(map(int, input().split()))
    money = 0
    # 마지막날 매매가를 최댓값으로 지정.
    # 처음 날짜로 돌아가면서 전날의 매매가가 더 적으면 그 차익을 이익으로 저장.
    max_sale = sales[-1]
    for i in sales[-2: :-1]:
        if i < max_sale:
            money += max_sale - i
        elif i > max_sale:
            max_sale = i

    print(f"#{tc} {money}")
