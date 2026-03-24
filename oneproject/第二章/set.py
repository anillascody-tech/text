#set 自动去重
#无序(无索引),不可重复,可修改
# #实际场景:用户id 身份证号 手机号,不可重复
# s1 = {1,2,6,6,5,1,8,3}
# #定义空集合,不可以直接用{},不然是字典
# s2 = {1,2,6,11,12,13}
# s3 = set()#空集合
# #add("")添加
# #remova("")移除特定,不存在会报错
# #pop()随机删除并返回
# #clear()清空
# #difference()差集 包含在第一个,但不包含在第二个的元素
# #union()并集:s1 s2全部
# #intersection()交集,相同的部分
# s1.add(99)
# print(s1)
# s1.remove(1)
# print(s1)
# s1.pop()
# print(s1)
# s1.clear()
# print(s1)
# s1 = {1,2,6,6,5,1,8,3}
# print(s1.difference(s2))
# print(s1.union(s2))
# print(s1.intersection(s2))
#
# #& 与 求交集 intersection
#- 减 求差集 difference
#集合推导式(和列表只有括号不一样):{s for s in set_1 if}
#| 并 求并集 union

# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# 选修篮球学生名单
basketball_set = {"张铁", "圈居仁", "王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set = {"遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

# 1. 找出同时选修了法语和艺术的学生
#1.1
fa_set = french_set.intersection(art_set)
print(f"学生{fa_set}同时选修了french和art")
#1.2
fa_set2 = french_set & art_set
print(f"学生{fa_set2}同时选修了french和art")
# 2. 找出同时选修了所有四门课程的学生
#2.1
fbfa_set = french_set.intersection(football_set).intersection(basketball_set).intersection(art_set)
print(f"学生{fbfa_set}同时修了全部课程")
#2.2
fbfa_set2 = french_set & football_set & basketball_set & art_set
print(f"学生{fbfa_set2}同时修了全部课程")
# 3. 找出选修了足球，但是没有选修篮球的学生
#3.1
fb_set = football_set.difference(basketball_set)
print(f"学生{fb_set}选修了football,但是没有选修basketball")
#3.2
fb_set2 = football_set - basketball_set
print(f"学生{fb_set2}选修了football,但是没有选修basketball")
#3.3
fb_set3 = {i for i in football_set if i not in basketball_set}
print(f"学生{fb_set3}选修了football,但是没有选修basketball")
# 4. 统计每一个学生选修的课程数量
all_set = football_set | basketball_set | art_set | french_set
all_list = (*football_set, *basketball_set, *art_set, *french_set)
for i in all_set:
    print(f"学生{i}选修了{all_list.count(i)}门课程.")

