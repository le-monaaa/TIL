import heapq

hq = []

for i in range(10, 0, -1):
    heapq.heappush(hq, i)

for i in range(10):
    print(heapq.heappop(hq), end = " ")

print()

# 응용
# heappush에 숫자만 넣을 수 있는 게 아니라 튜플도 넣을 수 있다
heapq.heappush(hq, (4, "4등"))
heapq.heappush(hq, (1, "1등"))
heapq.heappush(hq, (2, "2등"))
heapq.heappush(hq, (3, "3등"))

for i in range(4):
    print(heapq.heappop(hq), end = " ")
