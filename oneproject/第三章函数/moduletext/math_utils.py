import math
import random
import datetime
def circle_area(r: float) -> float:
    return round(math.pi * r**2,4)
def is_even(n: int) -> bool:
    return n % 2 == 0
def get_fortune() -> str:
    return random.choice(['大吉','吉','中吉','小吉','末吉','凶'])
def sign_in(name: str) -> None:
    now = datetime.datetime.now()
    print(f"""
===========每日签到===========
姓名:{name}
日期:{now.strftime("%Y年%m月%d日")}
今日运势:{get_fortune()}
============================"""
    )
#测试函数
if __name__ == '__main__':
    print(circle_area(5))
    print(is_even(5))
    print(is_even(6))
    print(get_fortune())
    print(sign_in("王思雨"))