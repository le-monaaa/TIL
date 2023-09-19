import sys
sys.stdin = open("1242.txt", "r")

table = {(2, 1, 1): 0, (2, 2, 1): 1, (1, 2, 2): 2, (4, 1, 1): 3,
              (1, 3, 2): 4, (2, 3, 1): 5, (1, 1, 4): 6, (3, 1, 2): 7,
              (2, 1, 3): 8, (1, 1, 2): 9}

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())

    # 출력할 결과
    result = 0

    # 코드 중복 체크 방지
    dup_check = []

    # 암호코드 + 각 줄에 대한 중복 처리
    arr = list(set([input()[:m] for _ in range(n)]))

    # 각 줄에 대해서 코드 검사
    for i in range(len(arr)):
        # i번째 줄에서 검사
        ith_row = arr[i]

        # i번째 줄 16진수 문자열을 2진수 문자열로 바꾸기
        bin_row = ""

        # i번째 줄 문자열에서 문자 하나씩 떼서 2진수 문자열로
        for c in ith_row:
            c_hex_to_dec = int(c, 16)
            # 16진수 1자리는 2진수 4자리
            for j in range(3, -1, -1):
                bin_row += "1" if c_hex_to_dec & ( 1<< j) else "0"

        # i번째 문자열을 2진수로 바꿨는데 안에 1이 없어
        if "1" not in bin_row:
            # 다음 줄 검사
            continue
        else:
            # i번째 줄 안에 1이 있다 -> 뒤에서부터 암호코드 만들기 시작
            # 0과 1의 비율, 0 1 0 1 순서로 나옴~
            ratio = [0] * 4
            # ratio[0] : 맨처음 0의 비율
            # ratio[1] : 두번째 1의 비율
            # ratio[2] : 세번째 0의 비율
            # ratio[3] : 마지막 1의 비율
            
            # 모든 암호코드는 마지막이 1로 끝나니 오른쪽에 있는 "0"은 제거
            bin_row = bin_row.rstrip("0")

            # i번째에서 만든 코드 apppend 할 리스트
            code = []

            # 코드의 맨 끝이 1이니까 뒤에서부터 비율 계산
            for j in range(len(bin_row) -1, -1, -1):
                if bin_row[j] == "1" and ratio[2] == 0:
                    # 마지막 1의 비율 계산
                    ratio[3] += 1
                elif bin_row[j] == "0" and ratio[1] == 0:
                    ratio[2] += 1
                elif bin_row[j] == "1" and ratio[0] == 0:
                    ratio[1] += 1
                elif bin_row[j] == "0" and bin_row[j-1] == "1":
                    # 처음부분 0 만남. 이거는 안세도 뒤의 코드로 판별 가능
                    # 코드 변환 작업 시작!
                    min_v = min(ratio[1:4]) # 제일 작은 수 구해서 나누기

                    # 비율 계산 후 이 비율로 된 숫자가 테이블 안에 있는지 확인
                    number = table.get((ratio[1]// min_v, ratio[2]//min_v, ratio[3]//min_v))

                    # 비율 계산 끝나고 나서 비율 초기화
                    ratio = [0] * 4

                    # 숫자 하나 만든 거 코드에 이어붙이기
                    code.append(number)

                    # 만들고 나서 코드의 길이가 8이다 -> 암호코드 판별
                    if len(code) == 8: # 거꾸로 만들어서 순서 헷갈리지말기!
                        reverse_code = code[::-1]
                        # 검증코드 계산
                        odd = reverse_code[0] + reverse_code[2] + reverse_code[4] + reverse_code[6]
                        even = reverse_code[1] + reverse_code[3] + reverse_code[5] + reverse_code[7]
                        if (odd * 3 + even )% 10 == 0 and code not in dup_check:
                            # 각 자리수를 더해서 답에 누적합
                            result += odd + even

                            # 중복 방지 처리
                            dup_check.append(code)

                            code = []

    print(f"#{tc} {result}")



