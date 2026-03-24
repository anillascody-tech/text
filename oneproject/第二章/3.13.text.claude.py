#1
raw = "   Admin@Example.COM   "
mail = raw.strip().lower()
print(mail)

#2
s = "今天天气真好，我要去打篮球，打球真开心"
print(s.count("打"))
replace_s = s.replace('打','***')
print(replace_s)

#3
sentence = "  Hello World, I love Python and Python loves me.  "
sentence = sentence.strip()
print(sentence)
print(sentence.count("o") + sentence.count("O"))
print(sentence.find("Python"))
print(sentence.startswith("Hello"))
sentence_list =  sentence.split(" ")
print(sentence_list)

#4
s = "Hello-Python-World"
print(s[6:12])
print(s[-5:])
print(s[:5])
print(s[::-1])
print(s[::2])

#5
account = input("请输入用户名")
account = account.strip()
if  len(account) < 6 or len(account) > 12:
    print("错误")
elif account[0].isdigit():
    print("错误")
elif account.count("_") < 1 and account.count("-") <1 :
    print("错误")
else:
    print(account.lower())