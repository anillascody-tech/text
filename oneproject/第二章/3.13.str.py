#不可变\有序\尅迭代
#可迭代:可以遍历出来(list也可以)
#index和list一样
#可切片
# s[开始:结束:步长]
s = "hello-python"
print(s[-2])
#无法单个重新赋值,没有insert
print(s[6:])
print(s[-1::-1])
#重点是不可变,有序

#s.find()查找
#s.count()数量
#s.upper大写
#s.lower小写
#s.split('')分成列表
#s.strip/s.trip('*')删除两端
#s.replace('H','C')替换
#s.start with('P')是否开始于

#演示
s = '  Hello-python-Hello-world!  '
#s.find()查找
inedx = s.find("p")
print(inedx)
#s.count()数量
num = s.count("o")
print(num)
#s.upper大写
upper1 = s.upper()
print(upper1)
#s.lower小写
lower1 = s.lower()
print(lower1)
#s.split('') 切成列表
list1 = s.split("o")
print(list1)
#s.strip/s.strip('*')删除
strip1 = s.strip()
print(strip1)
strip2 = s.strip("-")
print(strip2)
#s.replace('H','C')替换
replce1 = s.replace("o", "!!")
print(replce1)
#s.start with/end with('P')是否开始于
print(s.startswith("Hello"))


#练习
mail = input("请输入邮箱")
if mail.count(".") >= 1 and mail.count("@") == 1:
    print('邮箱格式正确')
else:
    print("邮箱格式错误")
#replace可以用来删除,strip只对两端生效

#练习
user = input("请输入字符")
reversed_user = user[::-1]
if user == reversed_user:
    print("字符串为回文")

#练习
user = input("请输入十个字符")
reversed_user = user[::-1]
upper_user = reversed_user.upper()
for item in upper_user:
    print(item)
















