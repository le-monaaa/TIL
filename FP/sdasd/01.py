# T: 테스트케이스 개수/ N: 수열의 길이/arr: 주어진 수열(0, 1)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))
    # input().split('0') 으로 찾아부림

    cnt = 0
    maxi = 0

    for i in arr:
        if i == 1:
            cnt += 1
            if maxi < cnt:
                maxi = cnt

        else:
            if maxi < cnt:
                maxi = cnt
            cnt = 0

    print(f"#{t} {maxi}")
