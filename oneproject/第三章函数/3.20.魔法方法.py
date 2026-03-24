#魔法方法:双下划线,比如__init__,用于定义类的特殊行为
#不需要手动调用,会自动调用
#__init__ :初始化方法
#__str__ :字符串表示的方法
#__eq__ :对象是否相等

#__lt/le/gt/ge__
# 小于(less than),         小于等于(less than or equal)
# 大于(greater than),      大于等于(greater than or equal)

#基于对象内存地址进行对比大小
#在类的方法处添加魔法方法,然后指定比较方式,后续在使用中就可以使用">","=="等符号
# 对象 = 类的时候 类会运行吗

#text
class Car:
    def __init__(self,brand :str,price :int,color :str):
        self.brand = brand
        self.price = price
        self.color = color
    def __str__(self):
        return f"{self.brand} {self.price} {self.color}"
    def __eq__(self,other):
        return self.brand == other.brand and self.price == other.price and self.color == other.color
    def __lt__(self,other):
        return self.price < other.price
#测试函数
if __name__ == '__main__':
    c1 = Car ("奔驰", 50, "white")
    c2 = Car ("奔驰", 50, "white")
    print(c1 == c2)
    print(c1 < c2)
#属性
#实例属性:对象自己的 添加方式:__init__ 对象.属性
#类属性:所有对象共享
class Car:
    wheel = 4
    tax_rate = 0.1
    #wheel和tax就是类属性,放在__init__上面
    def __init__(self,brand :str,price :int,color :str):
        self.brand = brand
        self.price = price
        self.color = color
#查找顺序:先实例属性,后类属性
#也可以通过类名访问类属性 Car.tax

