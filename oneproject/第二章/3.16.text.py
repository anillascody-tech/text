#教务管理系统
print("欢迎使用教务管理系统~")
students = {}
while True :
    print("""
    请输入数字,选择操作
    ######## 东北人工智能大学 #####
    #        1.添加学生信息      #
    #        2.修改学生信息      # 
    #        3.删除学生信息      # 
    #        4.查询学生信息      # 
    #        5.列出所有学生      #
    #        6.统计班级成绩      #
    #        7.退出系统         # 
    ###########################
    """)
    chooes =  input("请输入选项:")
    match chooes:
        case "1":#添加
            students_name = input("请输入学生姓名:")
            if students_name not in students:
                students_math = float(input("请输入数学成绩:"))
                students_chinese = float(input("请输入语文成绩:"))
                students_english = float(input("请输入英语成绩:"))
                students[students_name] = {'数学成绩': students_math,
                                           '语文成绩': students_chinese,
                                           '英语成绩':students_english}
            else:
                print("操作错误,请重试")
                continue
        case "2":#修改
            students_name = input("请输入学生姓名:")
            if students_name not in students:
                print("操作失败,查无此人")
                continue
            students_math = float(input("请输入数学成绩:"))
            students_chinese = float(input("请输入语文成绩:"))
            students_english = float(input("请输入英语成绩:"))
            students[students_name] = {'数学成绩': students_math,
                                       '语文成绩': students_chinese,
                                       '英语成绩': students_english}
            print("修改成功")
        case "3":#删除
            students_name = input("请输入学生姓名:")
            if students_name not in students:
                print("操作失败,查无此人!")
                continue
            else:
                del students[students_name]
                print("已经开除该学生!!")
        case "4":#查询
            students_name = input("请输入学生姓名:")
            if students_name not in students:
                print("查无此人")
                continue
            else:
                print(f"学生{students_name}的成绩如下:")
                print(f"\t\t\t数学成绩:{students[students_name]['数学成绩']}")
                print(f"\t\t\t语文成绩:{students[students_name]['语文成绩']}")
                print(f"\t\t\t英语成绩:{students[students_name]['英语成绩']}")
        case "5":#所有
            for students_name, info in students.items():
                print(f"商品名称:{students_name},数学成绩:{info['数学成绩']},语文成绩:{info['语文成绩']},英语成绩:{info['英语成绩']}")
        case "6":#统计各科成绩的平均分,最高分,最低分,以及各科最低分姓名
            math_tuple = [(name,info['数学成绩']) for name,info in students.items()]
            chinese_tuple = [(name,info['语文成绩']) for name,info in students.items()]
            english_tuple = [(name,info['英语成绩']) for name,info in students.items()]
            min(math_tuple, key=lambda x: x[1])
            lowest_name, lowest_score = min(math_tuple, key=lambda x: x[1])

        case "7":#退出
            print("好好学习,天天向上!")
            print("已退出管理系统")
            break
        case _:
            print("操作错误,请重试")