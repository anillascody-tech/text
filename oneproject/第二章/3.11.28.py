#循环while for
# while 条件判断ture则执行语句1:
#     语句1
# 执行语句后回到判断,直到false
# else:(非必要)
#     循环结束后执行
#ture循环 for退出

# a = 0
# while a < 5:
#     print("人生苦短,我用python~")
#     a += 1
# else:
#     print("执行完毕")

# # 练习:1-100之间所有偶数的累加之和
# a = 2
# b = 0
# while a <= 100:
#     b += a
#     a += 2
#
# print(b)
#
# c = 1
# d = 0
# while c <= 100 :
#     if c % 2 == 0 :
#         d += c
#     c += 1
#
# print(d)

#for循环
#while是条件循环,for是逐个处理
# for 元素 in 数据集
# 在数据集中逐个寻找某个元素,并进行处理
#while 循环次数未知
#for s :把字符全选出来
#for i :把数字全选

#计算1-100 奇数之和
#range(x)0到x 不含x
#range(x,y)x到y 不含y
#range(x,y,z)x+z,一直到y,不含y
#range:找字符串,拎出数字

#一
# a = 0
# for i in range(1,101) :
#     if i % 2 == 1:
#         a += i
# print(a)

#二
a = 0
for i in range(1,101,2) :
    a += i
print(a)
#
b = 0
for i in range(100,501) :
    if i % 3 == 0:
        b += i
print(b)


