#对象(物品)方法(功能)
#一切都是对象
# #列表的常见方法
# #append()尾部追加元素
# #insert(_index:,_object:)索引处插入元素,剩余元素往后挪一个
# #remove()元素删除,第一个 不是索引而是逐个
# #pop()索引删除 索引位置的元素 默认最后一个,删除后还会返回,可以用容器接收
# #sort()排序(所有元素类型一致)
# #reverse()反转
# # ?.方法()
# #
# s = [1,16,68,161,88,12]
# s.append()
# s.insert(0,1)
# s.remove()
# s.pop()
# # s.sort()从小到大
# s.reverse()
#
# # sum() 求和
# # len()求长度/总数
# # min()最小值
# # max()最大值
#

num_list = []
for i in range(10):
    num = int(input("请输入数字"))
    num_list.append(num)
num_list.sort()
print(num_list)
print(num_list[0])
print(num_list[-1])
print(sum(num_list) / len(num_list))

num_list1 = [12,55,66,40,73,44,75,13,489,66,88]
num_list2 = [11,5,55,40,75,10]
for num in num_list2:
    num_list1.append(num)
num_list3 = [*num_list1, *num_list2]
num_list3.sort()
print(num_list3)
# for 元素 in 列表:
#判断元素是否存在列表中,存在则Ture
new_num_list = []
for num in num_list1:
    if num in new_num_list:
        pass
    else:new_num_list.append(num)
new_num_list.sort()
print(new_num_list)

new_num_list = []
for num in num_list3:
    if num not in new_num_list:
        new_num_list.append(num)
new_num_list.sort()
print(new_num_list)

#合并列表
#解包:将容器解开成独立元素
#*
#组包:将多个值合并
#num_list3 = [num_list1 + num_list2]
#num_list3 = [*num_list1, *num_list2]

num_list = []
for i in range(21):
    num_list.append(i ** 2)
print(num_list)
#列表推导式:按规则快速生成列表
#[要插入的值 for i in 列表 ]
# num_list2 = [i ** 2 for i in range(21)]

#[要插入的值 for i in 列表 if 条件]
num_list4 = [22,16,13,49,67,616,49,23,497,10]
# num_list3 = [i ** 2 for i in num_list4 if i % 2 == 0]
print(num_list3)
num_list5 = []
for i in num_list4:
    if i % 2 == 0:
        num_list5.append(i ** 2)
print(num_list5)

#练习
list1 = ["a", "b", "c"]
list2 = ["d", "e", "f"]
list3 = ["a", "e", "i"]
list4 = [list1 + list2 + list3]
list5 = []
#list5 = [i for i in list4 if i not in list5 ]
for i in list4:
    if i not in list5:
        list5.append(i)
print(list5)

#练习
list1 = [1,2,3,4,5.6,7,8,9,10]
list2 = [i ** 2 for i in list1 if i % 3 ==0 or i % 5 == 0 ]
print(list2)

#练习
list1 = [1,-1,2,8,6,-465,-6,4,11,-4]
list2 = [i for i in list if i > 0]
print(list2)

