import sys
sys.stdin = open('input.txt')  # input() 위치에 파일 한 줄 한 줄 알아서 들어가더라....


T = int(input())
for tc in range(1, T+1):
    #           ['#1', '7041']  이렇게 나오는 것을 받아서 쓰자!
    tc_str, N = input().split()  # '#1' : 굳이 사용하지 않아도 됨 / 다음 문자열인 내용은 총 길이 나타냄 (필요한 내용)
    # N 은 길이를 나타냄!!! => 문자 그대로 사용 불가! 숫자로 변경할 필요가 있음
    N = int(N)
    arr = input().split()  # ['ZRO', 'ONE', 'TWO', ... .]

    COMP_NUMBERS = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]  # 이미 순서대로 정렬된 상태!!!

    # 테스트 케이스 번호를 출력!!
    print(f'#{tc}')
    for number in COMP_NUMBERS:
        # number : ZRO, ONE, ....  # COMP_NUMBERS 에서 순서대로 나옴 (이미 오름 차순으로 정리된 상태)
        for num in arr:
            # num : 테스트 케이스로 받은 무작위 문자열 SVN, FIV, ...  하나씩 나올것임
            if num == number:       # 정렬된 number 와 같은 num 문자열만 출력!!
                print(num, end=' ') # end 를 이용하여 출력을 한 칸 씩 띄워서 출력하자!!!
    print() # 모든 반복이 끝나면 줄바꿈!!