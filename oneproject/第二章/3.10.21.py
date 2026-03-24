#tab是四个空格
#条件判断
# a = int(input("高考分数"))
# if a >= 680:
#     print("读清华")
#     print("啦啦啦")
# else:
#     print("卖地瓜")
# print("--------------------------")


# #练习
# #初始账号密码
# account = "188"
# password = "688"
# #接收用户的账号密码
# a = input("请输入账号：")
# b = input("请输入密码：")
# #结果反馈
# if a != account:
#     print("账号错误")
# elif b != password:
#     print("密码错误")
# else:
#     print("登陆成功")
#     print("登陆成功")

# #平年闰年练习
# a = int(input("请输入年份:"))
# if (a % 100 != 0 and a % 4 ==0) or a % 400 == 0:
#     print("闰年")
# else:
#     print("非闰年")
#
# #奇数偶数判断
# a = int(input())
# if a % 2 == 0:
#     print("偶数")
# else:
#     print("奇数")
#
# #成年判断
# a = int(input())
# if a >= 18:
#     print("成年")
# else:
#     print("未成年")
#
# #正负判断
# a = int(input())
# if a > 0:
#     print("正数")
# else:
#     print("负数")
#
# #及格判断
# a = int(input())
# if a >= 60:
#     print("及格")
# else:
#     print("不及格")

#先if，不行就elif，Ture则继续elif，直到最后else
account = input()
password = input()
if account == "admin" and password == "666888":
    print("登录成功")
elif account == "root" and password == "547527":
    print("登录成功")
elif account == "gaoshuo" and password == "123456":
    print("登录成功")
else:
    print("滚")

#成绩练习
seiseki = int(input("你考了多少分？"))
if seiseki >= 85:
    print("优秀")
elif seiseki >= 60:
    print("及格")
else:
    print("不及格")

#折扣计算
kinngaku = int(input("商品总价"))
if kinngaku >= 500:
    print("8折")
elif 300 <= kinngaku <500:
    print("9折")
elif 100 <= kinngaku <300:
    print("95折")
else:
    print("10折")