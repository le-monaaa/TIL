lst = list(map(int,input().split()))
for i in range(len(lst)):
    if abs(lst[i]-lst[i+1])<3:
        print('완벽한배치')
        break
    else:
        print('재배치필요')
        break