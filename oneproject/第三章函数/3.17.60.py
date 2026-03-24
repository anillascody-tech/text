#函数说明文档
def circle_area_len(m,n):
    """
    :param m: 长方形的长度
    :param n: 长方形的宽度
    :return:先计算长乘宽得出长方形面积
    再计算长宽相加得出周长
    """
    return m * n,m + n
circle_area,area = circle_area_len(10,20)
help(circle_area_len)
#直接放置鼠标
# help内只要有函数名,不用括号
#按住ctrl,左键点击函数
print(area)

#嵌套调用
#栈结构:lifo,先进的后出
#就像羽毛球筒,后放进去的先出来
#abcba
#f7进入函数
#或者在函数处打点

def a():
    print('a')
    b()
    print("a")
def b():
    print('b')
    c()
    print("b")
def c():
    print('c')
a()
print("执行完毕")