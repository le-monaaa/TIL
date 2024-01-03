# t : target 비교하려는 원래 문자열 (젤 긴거)
# t_idx : target의 인덱스
# p : pattern 찾으려는 문자열 (일치하는 문자열) (짧은거)
# p_idx : pattern 의 인덱스


def my_len(arr):
    count = 0
    for a in arr:
        count += 1
    return count

# target 에서 pattern이 일치하는 t_idx의 시작점을 반환하는 함수
def brute_force(target, pattern):
    # 시작 점 부터 비교
    t_idx = 0
    p_idx = 0

    t_len = my_len(target)  # or len(target)
    p_len = my_len(pattern)
    # while 문으로 비교
    # while 종료 조건
    # target의 끝까지 비교하거나 pattern의 끝까지 비교한 경우 stop
    while (t_idx < t_len) and (p_idx < p_len):
        # 문자열을 비교한다!
        if target[t_idx] == pattern[p_idx]:  # 만약 같다면?
            # 다음 번째의 문자를 비교하자!!
            t_idx += 1
            p_idx += 1
        else:   # 만약 문자가 같지 않다면?!
            # 다음 비교 문자 index 위치 선정  (현재위치(target) - 비교한위치(pattern) + 1)
            t_idx = t_idx - p_idx + 1  # p_idx => 여태 비교한 문자열의 인덱스
            p_idx = 0  # 패턴은 항상 처음부터 비교를 하기에 0으로 변경

    if p_idx == p_len:  # pattern을 끝까지 순회했다. == 일치하는 문자열이 있더라
        # 자 그럼 일치하는 target의 시작점을 리턴하자!
        return t_idx - p_idx
    else:               # 찾지 못했다면
        return -1

target = 'This is a Book'
pattern = 'is'

result = brute_force(target, pattern)
print(result)