import heapq

# 우리 강한 파이썬!! 장하다!! 멋지다!!

# 최대힙 만들 어 보 기?
def insert(item):
    global last

    last += 1
    heap[last] = item  # 값 변경 완료
    c = last
    p = c // 2
    while c > 1 and heap[p] < heap[c] :
        # p = c // 2
        # heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c//2
        # else:
        #     break
    return c

def hpop():
    global last


    res = heap[1]
    heap[1] = heap[last]
    last  -= 1

    p = 1
    c = p * 2
    while c <= last:
        if c+1 <= last and heap[c] < heap[c+1]:
            c = c+1
        if heap[p] < heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            p = c
            c = p * 2
        else:
            break

    return res

heap = [0, 33, 31, 27, 21, 22, 18, 23, 14, 19] + [0] * 100
# print(tree)
last = 9  # 힙 마지막 자리는 알고있어야지.
print(insert(32))
print(heap)

print(insert(20))
print(heap)

print(insert(25))
print(heap)
print(hpop())
print(heap)