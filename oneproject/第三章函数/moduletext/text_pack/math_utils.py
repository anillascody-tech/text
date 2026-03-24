import math
def circle_area(r: float) -> float:
    return round(math.pi * r**2,4)
def is_even(n: int) -> bool:
    return n % 2 == 0
#测试函数
if __name__ == '__main__':
    print(circle_area(5))
    print(is_even(5))
    print(is_even(6))