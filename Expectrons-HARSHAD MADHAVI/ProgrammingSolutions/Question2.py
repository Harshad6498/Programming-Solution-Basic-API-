# Input is treated different for small alphabets and capital alphabets so 'h' is not 'H'
list1 = input("Enter the First list: ")
list2 = input("Enter the Second list: ")
list1 = list1.strip()
list2 = list2.strip()
list1 = list1.split()
list2 = list2.split()
list3 = list1+list2
counts = dict()
output = list()
for val in list3:
    counts[val] = counts.get(val,0)+1
for x in counts:
    output.append(x)
print(output)