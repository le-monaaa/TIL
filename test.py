print(sum) # built in function
print(sum(range(3))) # 정상적으로 작동

sum = 5 # global scope에서 사용

print(sum) # int type 5
# print(sum(range(3))) # type error

del sum

print(sum(range(4)))