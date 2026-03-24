#1
scores = [65, 88, 72, 90, 55, 100, 67, 88]
print(max(scores))
print(min(scores))
print(sum(scores) / len(scores))
Quantity = 0
for score in scores:
    if score >= 60:
        Quantity += 1
print(Quantity)

#2
nums = [3,5,2,5,7,2,9,3,1]
nums2 = []
for num in nums:
    if num not in nums2:
        nums2.append(num)
print(nums2)

#3.1
nums = [1,2,3,4,5,6,7,8]
nums2 = []
for num in nums:
    if num % 2 == 0:
        nums2.append(num ** 2)
print(nums2)

#3.2
nums = [1,2,3,4,5,6,7,8]
nums2 = [num ** 2 for num in nums if num % 2 == 0]

#4
prices = [23,45,12,67,34,89,15]
print("商品总价格为:",sum(prices))
print("商品最高价格为:",max(prices))
print("最便宜的商品价格为:",min(prices))
Quantity = 0
for price in prices:
    if price >= 50:
        Quantity += 1
print("价格大于50的商品数量为:",Quantity)

#5
nums = [12,5,77,23,77,45,99,12]
nums2 = []
for num in nums:
    if num not in nums2:
        nums2.append(num)
nums2.sort()
print("第二大的数字为:",nums2[-2])

#题太多,直接挑战难题9
nums = [1,2,3,4,5,6,7,8,9]
odd = []
even = []
for num in nums:
    if num % 2 == 0:
        odd.append(num)
    else:
        even.append(num)
print(odd)
print(even)

#10
nums = [1,2,3,4,5]
nums.pop(4)
nums.insert(0,5)

