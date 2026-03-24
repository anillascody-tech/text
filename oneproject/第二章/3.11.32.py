#嵌套循环
#先看内层循环
#执行一次外层循环,执行一套内层循环

# #长方形打印练习
# m = int(input("请输入行数:"))
# n = int(input("请输入列数:"))
# for j in range(m) :
#     for i in range(n) :
#         print("*",end=" ")
#     print("")
# #end=""每次输出时,以什么结束,默认是\n
#
# # #练习 九九乘法表
# for i in range(1,10):
#     for j in range(1,i + 1):
#         print(f"{j}*{i}={i * j}",end="\t")
#     print()
#
# #练习等腰直角三角形
# s = int(input("请输入边长"))
# for i in range(1,s + 1):
#     for j in range(1,i + 1):
#         print("*",end="\t")
#     print()
#
# # #练习:数字金字塔
# a = int(input("请输入数字"))
# for i in range(1,a + 1):
#     for j in range(1,i + 1):
#         print(j,end="\t")
#     print()
#
# #国际象棋练习,奇数黑偶数白
# for i in range(1,9):
#     for j in range(1,9):
#        if (i + j) % 2 == 0:
#             print("黑",end="\t")
#        else:
#            print("白", end="\t")
#     print()

#登录练习
#break:跳出循环
#continue,终端本次循环,直接下一次循环

while True:
    account = input("请输入账号")
    password = input("请输入密码")
    if account == "" or password == "":
        print("不能为空")
        continue

    if account == "admin" and password == "666888":
        print("登陆成功")
        break
    elif account == "zhangsan" and password == "123456":
        print("登陆成功")
        break
    elif account == "taoge" and password == "888666":
        print("登陆成功")
        break
    else:
        print("登陆失败,请重试")

for i in range(5):
    account = input("请输入账号")
    password = input("请输入密码")
    if account == "" or password == "":
        print("不能为空")
        continue

    if account == "admin" and password == "666888":
        print("登陆成功")
        break
    elif account == "zhangsan" and password == "123456":
        print("登陆成功")
        break
    elif account == "taoge" and password == "888666":
        print("登陆成功")
        break
    else:
        print("登陆失败")