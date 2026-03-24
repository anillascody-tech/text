#算数运算符
# +  -  *   /   //   %   **
# 加 减 乘   除  整除  取余 幂指数
#除结果为小数，整除结果为整数，取余结果为余数。
#幂指数：10 ** 3：10的3次方。计算次方
print(10 // 3)

#算术运算符的优先级
#()
# **
# * / // %
# + -

# #float包含int但是会加上。0
# x = float(input("请输入x"))
# y = float(input("请输入y"))
# print("x + y =",x + y)
# print("x - y =",x - y)
# #0.5-0.4=0.099999998
#因为二进制无法准确表示小数，所以可能会出错

#练习一，计算三个数的平均数
x = float(input("请输入x"))
y = float(input("请输入y"))
z = float(input("请输入z"))
print("x，y，z的平均数为",(x + y + z)/3)

#练习二，计算梯形面积
x = float(input("请输入上底长度"))
y = float(input("请输入下底长度"))
z = float(input("请输入高度"))
print("梯形的面积为",((x + y) * z)/2)

#练习三，计算圆的周长和面积
r = float(input("请输入半径"))
print("圆的周长为",2 * 3.14 * r)
print("圆的面积为",3.14 * r ** 2)

#练习四，计算BMI
x = float(input("请输入体重（kg）"))
y = float(input("请输入身高（m）"))
print("您的BMI为",x / (y ** 2))