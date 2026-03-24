"""
可以使用
三引号
进行
多行注释
pass 空语句，语法占位作用
"""
# #三角形判断
a = int(input("请输入第一个边的边长"))
b = int(input("请输入第二个边的边长"))
c = int(input("请输入第三个边的边长"))
if a + b > c and b + c > a and c + a > b:
    if a == b and b == c:
        print("等边三角形")
    elif a == b or b == c or a == c:
        print("等腰三角形")
    else:
        print("普通三角形")
else:
    print("非三角形")

#电费计算
a = int(input("本月消耗电力为"))
if a < 2800:
    print("第一档")
elif a <= 4800:
    print("第二档")
else:
    print("第三档")