#函数:可重复使用的代码片段
#max min len input,print等是python内置函数
#
# def 函数名(形式参数):
#     函数体
#     .....
#     return 返回值
#
# #调用函数
# 函数名(参数)
# def out_line():
#     print("-------------")
#     print("天上天下唯我独尊")
#     print("-------------")
# def out_line2():
#     out_line()
#     out_line()
#     out_line()
# def out_line3():
#     out_line2()
#     out_line2()
#     out_line2()
# out_line3()
#return必须在末尾
def circle_area_len(m,n):
    return m * n,m + n
area,len = circle_area_len(10,20)
print(area)
print(len)
#a,b形式参数,只能在函数内使用(局部变量),且有顺序
#10,20实际参数
#返回多个值.逗号分隔
# round(对象,几位小数)


