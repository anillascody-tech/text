#python的内置函数基于c语言开发
#1 三角形面积函数
def triangle_area (a,h):
    """
    :param a:三角形的底长
    :param h: 三角形的高
    :return: 三角形公式
    """
    return a * h / 2
print("长3高4三角形的面积为",triangle_area(3,4))
#2 计算元音字母数量
def vowels_num (v):
    total = 0
    for a in v:
        if a in 'aeiouAEIOU':
            total += 1
    return total
print("helloword,im'gaoshuo的元音数量为",vowels_num("helloword,im'gaoshuo"))
#3计算列表分数
def scores (s):
    max_s = max(s)
    min_s = min(s)
    avg_s = round(sum(s) / len(s),1)
    return max_s, min_s, avg_s
score = [550,221,244,588,670,740]
max_score, min_score, avg_score = scores(score)
print(f"最高分为{max_score}, 最低分为{min_score}, 平均分为{avg_score}")
