T = int(input())

for t in range(1, T+1):

    N = int(input())
    cards = list(map(int, input()))

    count = [0] * (max(cards)+1)
    max_n = temp = 0

    for i in cards:
        count[i] += 1

    for i in range(len(count)):
        if count[i] >= temp:
            temp = count[i]
            max_n = i

    print(f"#{t} {max_n} {max(count)}")


