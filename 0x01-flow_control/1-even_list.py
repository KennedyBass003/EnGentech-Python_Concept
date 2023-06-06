lst1 = [8, 3, 9, 5]
lst2 = [2, 1, 4, 18]
lst3 = []
print(lst1)
print(lst2)
lst1.extend(lst2)
print(lst1)
for x in lst1:
    if x % 2 == 0:
        lst3.append(x)
print("even numbers =", lst3)
lst3.sort()
print("Sorted even numbers =", lst3)
