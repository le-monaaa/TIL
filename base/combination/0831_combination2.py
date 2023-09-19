def nCr(n, r, s): # n개에서 r개를 고르는 조합. s: 선택할 수 있는 구간의  시작
    if r == 0:
        print(*comb)
    else:
        for i in range(s, n-r+1):
            comb[r-1] = a[i]
            nCr(n, r-1, r)

a = [1, 2, 3, 4, 5]
n = len(a)
r = 3
comb = [0]*r

# n개 중에 2개 뽑는 경우 -> 2중 for문
# 3개 뽑는 경우 -> 3중 for 문
# 근데 r개 뽑는 경우? 이렇게 해야댐..
