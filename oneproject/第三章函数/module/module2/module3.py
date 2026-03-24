import random as rd
from random import *
from random import randint as ri

def p1():
    print("-" * 30)# - 重复三十次,字符串也可以用乘法
def p2():
    print("+" * 30)
def p3():
    print("*" * 30)
def p4():
    print("/" * 30)
NAME = "高硕"
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