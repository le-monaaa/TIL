def subset(i, n): # i번 원소를 결정할거고, n개의 원소가 있다.
    if i ==n:
        s = 0
        for j in range(n):
            if bit[j]:
                s += arr[j]
            if s == 0:
                for j in range(n):
                    if bit[j]:
                        print(arr[j], end = " ")
                print()
        else:
            bit[i] = 1
            subset(i + 1, n)
            bit[i] = 0
            subset(i+1, n)
        return

arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
n = len(arr)
bit = [0] * n
subset(0, n)


# 왜 난 안됨??

