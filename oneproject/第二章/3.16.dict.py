#字典dict
#根据某个字,查找对应的解释
#可变 键唯一不可变
#(key:value)
#根据key找value
#dictionary
#字典也是{},但是有:
# dict1 = {1:500,2:8686}
#key不能重复,有序,不能为可变类型
#空字典
# a  =  {}
# b = dict()
# #查找用[]方括号
# c = dict1[1]
#重复时会用后值覆盖前值
#添加
#字典名称[key] = value
#删除
#字典名称.pop(key)  删除并接收
#del 字典名称[key]
#修改
#字典名称[key] = value
#查询
#字典名称[key]()    获取值
#字典名称.get[key]()获取值
#字典名称.key()     获取所有键
#字典名称.values()  获取所有值
#字典名称.items()   键值所有对

# dict1[3] = 700
# print(dict1)
# dict1[1] = 800
# print(dict1)
# del dict1[1]
# print(dict1)
# a = dict1.pop(2)
# print(a)
# dict1[5] = 46
# dict1[6] = 800
# b = dict1.keys()
# print(b)

# #key遍历
# for k in dict1.keys():
#     print(f"{k}: {dict1[k]}")
# #items遍历
# for k,v in dict1.items():
#     print(f"{k}: {v}")

#购物车案例
print("欢迎使用购物车系统~")
shopping_cart = {}
while True :
    print("""
    请输入数字,选择操作
    ########## 硕的网店 ########
    #        1.添加购物车      #
    #        2.修改购物车      # 
    #        3.删除购物车      # 
    #        4.查询购物车      # 
    #        5.退出购物车      # 
    ##########################
    """)
    chooes =  input("请输入选项:")
    match chooes:
        case "1":
            goods_name = input("请输入商品名称:")
            if goods_name not in shopping_cart:
                goods_price = input("请输入商品价格:")
                goods_num = input("请输入商品数量:")
                shopping_cart[goods_name] = {'price':goods_price,'num':goods_num}
            else:
                print("操作错误,请重试")
                continue
        case "2":
            name = input("请输入商品名称:")
            if name not in shopping_cart:
                print("操作失败,购物车中没有此商品!")
                continue
            price = input("请输入商品价格:")
            num = input("请输入商品数量:")
            shopping_cart[name] = {'price':price, 'num':num}
            print("修改成功")
        case "3":
            name = input("请输入商品名称:")
            if name not in shopping_cart:
                print("操作失败,购物车中没有此商品!")
                continue
            else:
                del shopping_cart[name]
                print("删除成功!!")
        case "4":
            for name,info in shopping_cart.items():
                print(f"商品名称:{name},商品价格:{info['price']},商品数量:{info['num']}")
        case"5":
            print("欢迎下次光临")
            break
        case _ :
            print("操作错误,请重试")



