## 영어문장 내에서 특정 문자열 개수 반환

for tc in range(1, 11):
    _ = input()
    pa = input()
    where = input()

    cnt = 0
    for i in range(len(where) - 1):
        if where[i:i+len(pa)] == pa:
            cnt += 1

    print(f"#{tc} {cnt}")