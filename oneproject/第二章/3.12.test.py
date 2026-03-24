#11
num = int(input("请输入数字:"))
if num % 2 == 0:
    print("偶数")
elif num % 2 == 1 :
    print("奇数")
else:
    "错误"

#15
total = 0
for i in range(1, 101):
    total += i
print(total)

#20
n = int(input("请输入一个数字:"))
total = 0
for i in range(1, n + 1):
    total += i
print(total)
