my_list = []

#appending my list
for item in [10, 20, 30, 40] :
    my_list.append(item)
print(my_list)

#inserting 15 in second position
my_list.insert(1,15)
print(my_list)

#extending my_list with another list
list2 = [50, 60, 70]

my_list.extend(list2)
print(my_list)

#removing the last item
del my_list[-1]
print(my_list)

#sorting my_list in ascending order
my_list.sort()
print(my_list)

# Find and print the index of the value 30 in my_list.

print("Index of 30 is:",my_list.index(30))