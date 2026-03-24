#模式匹配
#从上往下依次匹配
#竖线  |  :  or
#_下划线:else
#可以使用条件判断
#应用场景:等值匹配

# #计算器练习
# number1 = int(input("请输入第一个数字"))
# number2 = int(input("请输入第二个数字"))
# a = input("请输入符号")
# match a:
#     case "+":
#         print(f"{number1} + {number2} = ",number1 + number2)
#     case "-":
#         print(f"{number1} - {number2} = ",number1 - number2)
#     case "*":
#         print(f"{number1} * {number2} = ",number1 * number2)
#     case "/" if number2 != 0:
#         print(f"{number1} / {number2} = ",number1 / number2)
#     case _:
#         print("你在搞什么飞机")

#游戏角色控制系统
a = input("请输入操作")
match a:
    case "上" | "w" | "W":
        print("角色向上移动")
    case "下" | "s" | "S":
        print("角色向下移动")
    case "左"|"a"|"A":
        print("角色向左移动")
    case "右"|"d"|"D":
        print("角色向右移动")
    case "跳"|" ":
        print("角色跳跃")
    case "攻击"|"J"|"j":
        print("角色发动攻击")
    case "退出"|"esc"|"ESC":
        print("角色退出游戏")
    case _:
        print("操作错误")
