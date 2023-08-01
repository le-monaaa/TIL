T = 3
# 테스트케이스 수
N = 5
# 카드 장 수
cards = list(map(int, "49679"))
print(cards)

for t in range(1, T+1):
    # cards : 입력배열
    # result : 정렬된 배열
    # count : 카운트 배열

    # 카운트 배열(원소갯수 체크, 카운팅 할 배열)
    count = [0] * (max(cards) + 1)

    result = [0] * len(cards)

    for i in range(0, N):
        count[cards[i]] += 1

    for i in range(1, len(count)):
        count[i] += count[i-1]

    for i in range(len(result) - 1, -1, -1):
        count[cards[i]] -= 1
        result[count[cards[i]]] = cards[i]

    

    print(f"#{t} {result}")







