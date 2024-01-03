# 가장 높은 곳에 있는 박스를 가장 낮은 곳으로 옮기는 작업- 덤프
# 치우는 위치나 놓는 위치는 상관없다.
# 주어진 덤프 수행 횟수 후 최고점과 최저점의 높이 차 출력.
# 평탄화 완료 : 최고점과 최저점의 차이가 1 이내.
# 주어진 횟수 내에 평탄화가 완료되면 그 때의 최고점과 최저점의 높이 차를 반환(0 or 1)

def maxx(list1):
    max = 0
    for i in list1:
        if max < i:
            max = i

    return max

def minn(list1):
    min = 101
    for i in list1:
        if min > i:
            min = i

    return min

for t in range(1, 11):
    tr = int(input())
    box = list(map(int, input().split()))

    for j in range(tr):
        max = maxx(box)
        min = minn(box)
        box[box.index(max)] -= 1
        box[box.index(min)] += 1

        if max - min <= 1:
            break

    result = max - min
    print(f"#{t} {result}")



'''
        for j in range(tr):
            box[box.index(max)] -= 1
            box[box.index(min)] += 1

            if max - min <= 1:
                break

    result = max - min

    print(f"#{t} {result}")
'''
