#def 参数名:命名函数
#基于名字调用
# lambda 参数列表:函数体(return什么)
#缺点是简单,可以作为高阶函数的参数使用
students = [("王林", 85, 92, 78), ("曾牛", 92, 88, 95)]
# 按语文排序
sorted(students, key=lambda x: x[1])
# 按数学排序
sorted(students, key=lambda x: x[2])
#按英语排序
sorted(students,key=lambda x:x[3])
# 按总分排序
sorted(students, key=lambda x: x[1] + x[2] + x[3])
#按字符个数排序
data_list = ['asd','dasdas','dasd']
result = sorted(data_list, key=lambda x:len(x), reverse=True)
print(result)
data_list.sort()