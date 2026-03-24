# #练习一
numbers = [3, 7, 2, 9, 5]
print(len(numbers))

# #练习二
numbers = [10, 20, 30, 40, 50]
print(numbers[0])
print(numbers[-1])
#
# #练习三
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(total)

#四
numbers = [8, 3, 15, 6, 2]
total = 0
for num in numbers:
    for num2 in numbers:
        if num < num2:
            break
        else:
            print(num)
#五
numbers = [1, 4, 6, 7, 9, 10]
count = 0
for i in numbers:
    if i % 2 == 0:
        count += 1
print(count)

#六
numbers = [10, 20, 30, 40, 50]
print(numbers[:2])
print(numbers[-2:])

#7
numbers = [1, 2, 3, 4, 5]
print(numbers[::-1])
#-1 改变方向

#8
numbers = [10, 20, 30, 40, 50]
del numbers[0]
del numbers[-1]

