#变量的作用域
#参数详解
#匿名函数

#变量的作用域
#全局变量
#整个代码都可以使用,通常定义在顶部
#函数内部叫局部变量,函数执行完毕后会自动销毁

num = 100
def circle_area(r):
     pi = 3.14159
     area = pi * (r ** 2)
     print(num)
     return area
c_area = circle_area(num)
print(c_area)
#global num
#使用全局变量而不是局部变量
#先声明再使用
#
#传参方式
#位置传参:按顺序对应实参和形参
#关键词传参:name = "高硕",age = 22
#可以位置 关键字混合传参.但是必须先位置后关键字
#参数少,不易混淆,位置参数
#参数多,易混淆 关键字参数
#想想半年后能不能看出含义,不能就关键字
def reg_stu(name,age,gender,city):
    return {"name":name,"age":age,"gender":gender,"city":city}
#位置传参
print (reg_stu("高硕",18,"男","南昌"))
#关键字传参
print(reg_stu(name="高硕",city="大连",age=55,gender="男"))
#混合传参
print(reg_stu("王思雨",18,city="上海",gender="女"))

#默认参数/缺省参数,可以缺少省去,使用默认值的参数
#形式:在定义函数时 形参 = 默认值
#默认参数必须放后面
#
def reg_stu2(age,city,name="高硕",gender="男"):
    return {"name":name,"age":age,"gender":gender,"city":city}
print(reg_stu2(18,"苏州",gender="未知",name="张六"))
print(reg_stu(55,"含杭州","王思雨","女"))

#不定长参数
#参数个数不确定时使用
#位置不定长参数
def calc_data(*args,**kwargs):
    """
    :param args: 数据
    :param kwargs: 决定平均数保留小数位数
    :return: 最小值最大值平均值
    """
    avg_data = sum(args) / len(args)
    if kwargs.get('round') is not None:
        avg_data = round(avg_data,kwargs.get('round'))
    return min(args), max(args),avg_data
# args是元组
#不一定是args,但一般这么写
*a,b = calc_data(11,20,38,421.3,round=0,count=8)
print(a)
print(b)
#关键词传参
#**kwargs
#使用key=values形式传递,会存入字典

#参数类型
#普通参数:数字,布尔,数据容器
#特殊参数:函数,使用oper 代表函数
def add(a,b):
    return 2*(a+b)
def calc(x,y,oper):
    return oper(x,y)
result = calc(1,2,oper=add)
print(result)

