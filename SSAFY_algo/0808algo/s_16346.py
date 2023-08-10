# SWEA 16346 문자열비교
# str1, str2. str2안에 str1과 일치하는 부분이 있는지 찾는 프로그램
# str1이 str2 안에 존재하면 1, 없으면 0 출력
import sys
sys.stdin = open("sample_input.txt", "r")
T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    result = 0
    for i in range(len(str2)- len(str1)+1):
        cnt = 0
        for j in range(len(str1)):
            if str2[i+j] == str1[j]: # 같을경우
                cnt += 1
            else: # 다른게 나오면 카운트 초기화
                cnt = 0
                break
        if cnt == len(str1):
            result = 1
            break

    print(f"#{tc} {result}")


