#输入input与输出print(键盘录入)
#input也是一个函数,功能为获取键盘输入数据
#获取的内容一定是字符串,所以a==""必须有双引号,否则一定Flase
# a = input("请输入密码")
# if a =="123":
#     print("欢迎回家")
# else:
#     print("滚")
#
# name = input("请输入您的姓名")
# age = input("请输入您的年龄")
# print(f"你好{name},您已经{age}岁了")

#银行取钱练习，字符串转换数字int（）
# yugaku = 10000
# #输入密码
# password = input("请输入密码")
# if password == "123":
#     #输入取款金额
#     kinngaku = int(input("您想取多少钱？"))
#     if yugaku  >= kinngaku:
#         #计算余额并输出
#         print(f"取钱成功，您目前的余额为{yugaku - kinngaku}")
#     else:
#         print("取钱失败，余额不足")
# else:
#     print("密码错误")

#计算器练习
number1 = int(input("请输入数字1"))
number2 = int(input("请输入数字2"))
print(f"结算结果为{number1 + number2}")

