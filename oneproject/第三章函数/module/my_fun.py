#module 一个.py就是一个模块
#自己创建的.py是自定义模块,python还有内置模块
#使用import random 导入之后才能使用
#导入模块
#可以导入一整个模块,也可以导入模块的某个功能
#improt 模块名
import random
#import 模块名 as 别名
import random as rd
from ftplib import parse227
# #from 模块名 import 功能名
# #from 模块名 import 功能名 as 别名
from random import randint as ri
# #from 模块名 import *(d导入模块所有功能)
from random import *
# *通配符号
#导入模块后,模块内的代码会自动执行
#__name__
#python的内置变量,在当前模块运行,会显示__main__,被导入到其他文件中时,会变成模块名,比如 my_fun
# 测试函数
#所以被导入时不会执行测试函数
# 也可以使用快捷方式:main
    #ctrl+y 快速删除
#all:指定*导入的功能
#__all__ = ["xxx","adc","afs"]
#在其他模块使用from name import *
#则会导入[]内的功能,所以*不一定是全部功能
__all__ =['p1','p2']
def p1():
    print("-" * 30)# - 重复三十次,字符串也可以用乘法
def p2():
    print("+" * 30)
def p3():
    print("*" * 30)
def p4():
    print("/" * 30)

#测试函数
if __name__ == '__main__':
    for i in range(5):
        print(randint(1, 100))
    for i in range(5):
        print(random.randint(1, 100))
    for i in range(5):
        print(rd.randint(1, 100))
    for i in range(5):
        print(ri(1, 100))





#自定义模块
#每个python文件都是一个模块,模块名就是文件名,所以文件名要python标识符定义,规范命名
#常量名称用全大写NAME,但python中没有严格的常量,大写表示不能修改
#包本质就是为了给多个模块进行分类而创建的文件夹
#包中还会包含一个__init__.py的文件,有该文件,证明这个文件夹是一个包
#没有init就是普通文件夹
#import 包名.模块名.功能
#from 包名 import 模块名
#from 包名 import *
#from 包名 import 功能名
#from 包名 import *
#在 包 -> 模块 -> 功能 的过程中可以用.也可以用import
#调用包的条件,包在当前文件的文件夹内
#导入包下所有模块 from module import *
#需要在__init__文件中使用__all__=[],没有定义不能导入
#即包和文件在同一目录下
#如果不在一个目录下,需要目录.包.模块