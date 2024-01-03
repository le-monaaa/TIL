## 원형큐


size = 10
cq = [0] * size
front = rear = 0

def enqueue(item):
    global rear
    # 큐가 가득차있으면 삽입 x
    if isFull():
        print("full")
        return
    rear = (rear + 1) % size
    # rear +1이 사이즈를 벗어나지않았으면 그냥 그대로 벗어났다면 size만큼 나눈 나머지~ 순환할 수 있게끔 하는 구조
    cq[rear] = item


def dequeue():
    global front
    if isEmpty():
        print("empty")
        return
    front = (front + 1) % size
    return cq[front]


def isEmpty():
    return rear == front


def isFull():
    return (rear + 1) % size == front


for i in range(10):
    enqueue(i)

print(cq)
print(isEmpty())
print(isFull())

for i in range(10):
    print(dequeue(), end = " ")
print()

print(cq)
print(isEmpty())
print(isFull())