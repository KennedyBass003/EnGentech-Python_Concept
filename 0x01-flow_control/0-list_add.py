def Sum(*nums):
    total = 0
    for x in nums:
        total += x
    print(total)


lst1 = [8, 3, 9, 5]
lst2 = [2, 1, 4, 18]
print(lst1)
print(lst2)
lst1.extend(lst2)
print(lst1)
print("The sum of all the values in the list is =", sum(lst1))
