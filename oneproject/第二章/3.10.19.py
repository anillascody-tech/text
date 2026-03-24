#赋值运算符
# += -= *= /= //= %= **=
# x += 1：x = x + 1
# x //= 2：x = x // 2
#以此类推
###进行除法运算后，会有小数点

#题目7
money =1000
money += 500
money -= 200
money += 300
print(money)

#题目8
exp = 0
#击杀哥布林
exp += 50
print("击杀哥布林，目前经验值为",exp)
#击杀哥布林
exp += 30
print("击杀哥布林，目前经验值为",exp)
#击杀哥布林
exp += 20
print("击杀哥布林，目前经验值为",exp)

#题目9
temp = 25
temp += 3
temp -= 5
temp += 2

#AI工程小练习
area = 1
a = int(input("请输入存款"))
b = int(input("请输入收入"))
c = int(input("请输入支出"))
a += b
a -= c
print("您的余额为",a)

