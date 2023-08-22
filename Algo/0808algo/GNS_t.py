import sys
sys.stdin = open('GNS_test_input.txt')  # input() 위치에 파일 한 줄 한 줄 알아서 들어가더라....


T = int(input())
for tc in range(1, T+1):
    m, N = input().split()
    N = int(N)
    nums_str = input().split()

    nums_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    print(f'#{tc}')
    for number in nums_list: # 이미 정렬되어 있는 num_list 순회하면서
        for num in nums_str: # 입력받은 문자열 순회
            if num == number:# 문자열 일치시에만 출력
                print(num, end=' ') # 한 칸씩 띄워서
    print() # 다음 테스트 케이스 전에 띄워주기

    #
