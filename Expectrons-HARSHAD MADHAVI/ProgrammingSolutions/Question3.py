students = [['Harry',37.21],['Berry',37.21],['Tina',37.2],['Akriti',41],['Harsh',39]]
all_stud = list()
for student in students:
    all_stud+=student
all_stud = {all_stud[i]: all_stud[i+1] for i in range(0, len(all_stud),2)}
#print(all_stud)
m_list = []
n_list = []

for x in all_stud.values():
    m_list.append(x)

m_list.sort()
val = m_list[1]
#print(val)
for n,m in all_stud.items():
    if m == val:
        n_list.append(n)
n_list.sort()
for name in n_list:
    print(name)