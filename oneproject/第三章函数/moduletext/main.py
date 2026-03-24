from math_utils import circle_area, is_even, get_fortune, sign_in
from random import randint, choice, shuffle
from datetime import datetime
#题目1
print(randint(1,100))
print(choice(["优秀","良好","及格","加油"]))
data = [1,2,3,4,5]
shuffle(data)
print(data)
#题目2
print(circle_area(8))
print(is_even(7))
print(is_even(8))
#题目3
now = datetime.now()
print(now.strftime("%Y年%m月%d日"))
weekday_map = {
    'Monday': "星期一",
    'Tuesday': "星期二",
    'Wednesday': "星期三",
    'Thursday': "星期四",
    'Friday': "星期五",
    'Saturday': "星期六",
    'Sunday': "星期日"
}
print(weekday_map[now.strftime("%A")])
#题目4
print(sign_in("高硕"))


