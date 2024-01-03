# https://www.acmicpc.net/problem/10886

n = int(input())
cute = 0
not_cute = 0
for N in range(n):
    a = input()

    if a == "1":
        cute +=1
    else:
        not_cute += 1


if cute > not_cute:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")