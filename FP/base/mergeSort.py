A = [69, 10, 30, 2, 16, 8, 31, 22]


# 병합 함수
def merge(left, right):
    result = []  # 왼쪽과 오른쪽을 합친 결과

    # i, j :
    # i => 왼쪽 리스트에서 원소를 꺼낼 위치
    # j => 오른쪽 리스트에서 원소를 꺼낼 위치

    # 왼쪽과 오른쪽 둘중 하나라도 원소가 남아있으면 진행
    while len(left) > 0 or len(right) > 0:
        # 둘다 원소가 남아있으면 누구를 꺼내올건지 비교
        if len(left) > 0 and len(right) > 0:
            # 왼쪽의 맨 앞 원소가 오른쪽 맨앞 원소보다 작으면 왼쪽 맨앞 넣기
            if left[0] <= right[0]:
                result.append(left.pop(0))
            # 그게 아니면 오른쪽 맨앞 넣기
            else:
                result.append(right.pop(0))
        # 왼쪽만 남아있으면 왼쪽 남은거 다추가
        elif len(left) > 0:
            result.append(left.pop(0))
        # 오른쪽만 남아있으면 오른쪽 남은거 다추가
        elif len(right) > 0:
            result.append(right.pop(0))

    return result


# lst : 정렬할 리스트
def mergeSort(lst):
    m = len(lst)

    # 종료 조건 (더이상 분할 못할때 까지)
    if m == 1:
        return lst

    # 분할
    mid = m // 2
    left, right = lst[:mid], lst[mid:]  # 얕은 복사

    # 정복
    left = mergeSort(left)  # 왼쪽 정렬
    right = mergeSort(right)  # 오른쪽 정렬

    # 병합
    return merge(left, right)


print(mergeSort(A))