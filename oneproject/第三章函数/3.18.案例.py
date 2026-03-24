def factorial(f):
    if f > 1:
        return f * factorial(f - 1)
    else:
        return 1
#自己调用自己 递归调用,一定要有终结点
print(factorial(5))

#订单计算器
def calc_order_cost(*args: tuple[str,int,int],coupon: int=0,score: int=0,express: float=0) -> float:
    """
    :param args: 商品名 价格 数量
    :param coupon: 优惠券,当前价格大于5000且大于优惠金额可使用,
    :param score: 积分,当前价格大于5000且大于优惠金额可使用,每整100抵扣1元
    :param express: 运费
    :return: 实际支付价格
    """
    price = sum(s[1] * s[2] for s in args)
    if price > 5000 and price > coupon:
        price -= coupon
    if price > 5000 and price > (score // 100):
        price -= (score // 100)
    price += express
    return price
print(calc_order_cost(("手机",5000,3),coupon=50000,score=1000,express=15))

