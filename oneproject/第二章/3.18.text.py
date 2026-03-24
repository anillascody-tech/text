from idlelib.autocomplete import FORCE

orders = [
    ("ORD001", "王林",   "手机",   3999.0, 2),
    ("ORD002", "曾牛",   "耳机",    299.0, 1),
    ("ORD003", "王林",   "平板",   2999.0, 1),
    ("ORD004", "韩立",   "手机",   3999.0, 3),
    ("ORD005", "厉飞雨", "键盘",    399.0, 2),
    ("ORD006", "曾牛",   "手机",   3999.0, 1),
    ("ORD007", "韩立",   "耳机",    299.0, 4),
    ("ORD008", "厉飞雨", "平板",   2999.0, 2),
    ("ORD009", "王林",   "键盘",    399.0, 3),
    ("ORD010", "遁天",   "耳机",    299.0, 2),
]
#1
def calc_subtotal (a: tuple[str,str,str,float,int]) -> float:
    """
    :param a: 单条订单元组
    :return:订单的小计金额
    """
    return a[3]*a[4]
#2
def filter_orders(name: str,order: list[tuple[str,str,str,float,int]]) -> list[tuple[str,str,str,float,int]]:
    """
    :param order:orders
    :param name:商品名称
    :return:所有订单列表。
    """
    return [s for s in order if s[2] == name]
#3
def customer_report(name: str,order: list[tuple[str,str,str,float,int]]) -> tuple[int,int,list[str]]:
    order_num = 0
    total_cost = 0
    goods = set()
    for s in order:
        if s[1] == name:
            order_num += 1
            goods.add(s[1])
            total_cost += calc_subtotal(s)
    return order_num,total_cost,list(goods)
#4
def sort_orders (order: list[tuple[str,str,str,float,int]],by: str) -> list[tuple[str,str,str,float,int]]:
    match by:
        case "price":
            report = sorted(order,key=lambda x:x[3],reverse=True)
        case "quantity":
            report = sorted(order,key=lambda x:x[4],reverse=True)
        case "subtotal":
            report = sorted(order,key=lambda x:calc_subtotal(x),reverse=True)
        case _:
            print("错误!!!")
            return []
    return report
#5
def order_summary (*args: tuple[str,str,str,float,int],discount: int=1,top: int=1) -> dict[str, float | list[tuple[str,str,str,float,int]]]:
    total_cost    = sum(calc_subtotal(s) for s in args)
    discount_cost = total_cost * discount
    top_list      = sorted(args,key=lambda x:calc_subtotal(x),reverse=True )[:top]
    return {"总金额:":total_cost,"折后金额:":discount_cost,"TOP订单:":top_list}









