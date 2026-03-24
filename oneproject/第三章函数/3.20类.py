# #定义类
# #class 类名
# #内容
# #类名命名规范 大驼峰命名法
# #每个单词的首字母大写且没有任何分隔符
# class Circle:
#     pass
# #创建对象
# #对象名 = 类名()
# #对象名.属性名 = 属性值
# c1 = Circle()
# c1.home = "哈尔滨"
# #直接打印:类名 类型(object) at 十六进制地址(一般不用,因为看不懂)
# #print(对象名.属性名) 会输出属性值
# print(c1)
# print(c1.home)
# #__dict__,以字典输出所有属性名和属性值
# print(c1.__dict__)
# #不推荐创建完对象后动态地添加属性
# #推荐写法 def在类外是函数,在类内是方法,称呼方式不同
# #__init__ :初始化方法,创建对象后自动调用--设置对象属性
# #self:固定使用的形参名称,代表(当前创建的实例)对象
#
#
# #示例
# # class 类名:
# #     def __init__(self, c_参数列表):
# #         self.属性名 = c_参数名
# class Car:
#     def __init__(self, c_color,c_price):
#         self.color = c_color#属性名在创建类时就创建
#         self.price = c_price
# #创建对象
# #对象名 = 类名(参数列表)
# c1 = Car('red',50000)
# print(c1.__dict__)
#基于类创建对象时,会调用def__init__方法

#实例方法
# def 方法名(self,a,b)
#   return a * b
# 创建类和方法,给对象添加属性
#对象名.方法名 :调用方法

#text
#题目1
class Student:
    def __init__(self, name: str, age: int,major:str) -> None:
        self.name = name
        self.age = age
        self.major = major
    def introduce (self) -> None:
        print(f"我叫{self.name},今年{self.age}岁,专业是{self.major}")
jess = Student('jess',18,'工程管理')
john = Student('john',20,'土木工程')
print(jess.__dict__)
print(john.__dict__)
#题目2
jess.introduce()
#题目3
class BankAccount:
    def __init__(self, owner:str,balance: float=0) -> None:
        self.owner = owner
        self.balance = balance
    def deposit (self, amount: float) -> None:
        self.balance += amount
        print(f"存入{amount}元,当前余额{self.balance}元")
    def withdraw(self, amount: float) -> None:
        if amount <= self.balance:
            self.balance -= amount
            print(f"取出{amount}元,余额{self.balance}元")
        else:
            print("穷鬼,余额不足!")
#测试代码
if __name__ == '__main__':
    acc = BankAccount("Alice")
    acc.deposit(500)
    acc.withdraw(200)
    acc.withdraw(400)
