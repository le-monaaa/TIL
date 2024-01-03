# 패턴 매칭 알고리즘 - 고지식한 패턴 검색 알고리즘
# 두 개의 문자열 str1 str2. str2안에 str1과 일치하는 부분이 있는지 찾는 프로그램

T = int(input())
for tc in range(1, T+1):
    pattern = input() # 내가 찾고자하는 패턴 문자열
    text = input() # 여기 안에서 찾을것이다~

    # 일치하는 부분이 있으면 1, 없으면 0 출력

    # 패턴에서 비교할 문자의 위치
    pi = 0 # pattern index
    # 텍스트에서 비교할 문자의 위치
    ti = 0 # text index

    answer = 0 # 답
    # 비교 횟수가 정해져있지 x. 중간에 찾을수도 찾지 못할 수도 있음
    # pi, ti는 점점 증가. 비교가 끝나는시점? -
    while ti < len(text) and pi < len(pattern) :
        # 비교할 문자의 위치가 문자열의 길이보다 길면 X
        # 현재 위치에서부터 비교 시작
        # 현재 위치 pi에 있는 문자와 ti에 있는 문자가 같으면
        # 다음꺼 비교 pi+1 ti+1 하면서 거듭 비교 --> pi끝날때까지 or 불일치까지
        if pattern[pi] == text[ti]:
            pi += 1
            ti += 1
        else:
        # 다르면? 그 뒤엔 볼것도없다 다시 pi = 0, ti는 pi만큼 다시 앞으로 갔다가
        # 다시 비교~~~
        ti = ti - pi + 1
        pi = 0
        
        #### 이게 왜.. 어차피 pi가 0이 되면 pi를 ti에서 빼주는 의미가 없지않나
        # 내가 처음 생각했을때도 그냥 ti ++ 이었는데 왜 굳이 이렇게 쓰는거지?
        # -- 수정
        
        # 패턴 문자의위치 pi가 패턴의 길이만큼 되어버리면
        # 그전에 체크한 모든 문자가 같았다가 된다
        # 패턴발견!
        if pi == len(pattern):
            answer = 1
            break

