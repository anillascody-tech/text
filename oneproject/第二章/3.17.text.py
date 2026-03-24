
# 电商平台数据
#1
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

reviews = [
    "  Great Product!! very HAPPY with my purchase  ",
    "  BAD quality...will NOT buy again...  ",
    "  amazing deal-HIGHLY recommended-buy now  ",
    "  poor customer SERVICE...very DISAPPOINTED  ",
    "  EXCELLENT product,fast shipping,great price  ",
]
order_ids = [i[0] for i in orders]
prices = [i[-2] for i in orders]
print(f"最高价为:{max(prices)},最低价为:{min(prices)},平均价为:{sum(prices) / len(prices)}")

#2
reviews2 = [i.strip().lower().replace("...","，").replace("-"," ") for i in reviews]
print(reviews2)
for i in reviews2:
    print(i)
    words = i.split(" ")
    print(len(words))

#3
customer_total = {}
for s in orders:
    customer_total[s[1]] = customer_total.get(s[1],0) + s[3] * s[4]
print(customer_total)
max_price = 0
for name,prices in customer_total.items():
    if prices > max_price:
        max_price = prices
        max_name = name
print(f"全场消费最高的是{max_name},共消费{max_price}元")

#4
phone_buyers = set()
earphone_buyers = set()
for i in orders:
    if i[2] == "手机" :
        phone_buyers.add(i[1])
    elif i[2] == "耳机":
        earphone_buyers.add(i[1])
ep_buyers = phone_buyers & earphone_buyers
only_p_buyers = phone_buyers - ep_buyers
e_or_p_buyers = only_p_buyers | ep_buyers
print(f"同时买了手机和耳机：{ep_buyers}")
print(f"只买了手机：{only_p_buyers}")
print(f"买了手机或耳机：{e_or_p_buyers}")

#5
report = {"总订单数":0,"总销售额":0,"商品销量":{},"所有顾客":set(),"订单号列表":[]}
for s in orders:
    report["总订单数"] += 1
    report["总销售额"] += s[3] * s[4]
    report["商品销量"][s[2]] = report["商品销量"].get(s[2],0) + s[4]
    report["所有顾客"].add(s[1])
    report["订单号列表"].append(s[0])
print(f"总订单数为{report["总订单数"]},总销售额:{ report["总销售额"]},商品销量:{report["商品销量"]},所有顾客:{report["所有顾客"]},订单号列表:{report["订单号列表"]}")

records = [
    ("2024-01", "王林",   "销售部", 12500.0),
    ("2024-01", "曾牛",   "技术部", 15000.0),
    ("2024-01", "韩立",   "销售部",  9800.0),
    ("2024-02", "王林",   "销售部", 13200.0),
    ("2024-02", "厉飞雨", "技术部", 14500.0),
    ("2024-02", "曾牛",   "技术部", 15000.0),
    ("2024-03", "韩立",   "销售部", 11000.0),
    ("2024-03", "王林",   "销售部", 13800.0),
    ("2024-03", "厉飞雨", "技术部", 14500.0),
    ("2024-03", "遁天",   "人事部",  9500.0),
]
#1
employee_total = {}
dept_total = {}
month_total = {}
for i in records:
    employee_total [i[1]] = employee_total.get(i[1],0) + i[3]
    dept_total [i[2]] = dept_total.get(s[2],0) + i[3]
    month_total [i[0]] = month_total.get(i[0],0) + i[3]
for name,total in employee_total.items():
    print(f"员工{name}的总工资为{total}")







