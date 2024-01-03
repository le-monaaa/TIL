# SWEA 1926 간단한 369게임
# 박수 대신 - 출력. 369 갯수만큼.
# N

N = int(input())
nums = list(map(str, [i for i in range(1, N+1)]))
n = len(nums)
for i in range(n):
    for k in range(len(nums[i])):
        if nums[i][k] in "369":
            nums[i] = nums[i][:k] + "-" + nums[i][k+1:]
    if "-" in list(nums[i]):
        if len(nums[i]) != nums[i].count("-"):
            nums[i] = "-"

print(*nums)