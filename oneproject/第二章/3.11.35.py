#随机数
#break:跳出循环
#continue,终端本次循环,直接下一次循环
# import random
# random_number = random.randint(1,100)#生成随机数
# while True:
#     a = int(input("请猜一个数字:"))
#     if a>random_number:
#         print("猜大了")
#     elif a<random_number:
#         print("猜小了")
#     elif a==random_number:
#         print("恭喜你,猜对了")
#         break
# print(f"数字是{random_number}.")
#
# #1-1000 5累加
# a = 0
# for i in range(1001):
#     a += i
# print(a)

#统计字符串
b = "hhhhhhhkk"
c = 0
for a in b:
    if a == "a" or a == "k":
        c += 1
print(c)
