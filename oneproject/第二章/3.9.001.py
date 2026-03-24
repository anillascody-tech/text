#第一题
from collections.abc import async_generator

a,b,c,d,e = 100,3.14,"你好python",True,None
print(a)
print(b)
print(c)
print(d)
print(e)

#第二题
a,b = 10,20
print(a + b)
print(a * b)

#第三题
score = 60
score = score + 15
print(score)

#第四题第五题重复,第六题
name = "python"
age = 10
price = 19.9
flag = True
print(type(name))
print(type(age))
print(type(price))
print(type(flag))

#第七题
num = 10
print(isinstance(num,int))

#第八题
text = "你好\n我叫python\n很高兴认识你"

#第九题
text = '他说:\"python很好学\"'

#第十题
name = "Tom"
age = 20
city = "Tokyo"
print("姓名:" + name)
print("年龄:" + age)
print("城市:" + city)

#加分题
name = "python"
if isinstance(name,str):
    print("这是字符串")
else:
    print("不是字符串")