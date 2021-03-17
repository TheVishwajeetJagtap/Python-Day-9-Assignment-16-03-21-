#Generate a Python list of all the even numbers between 4 to 30

print(list( range(4, 30, 2)))


*********************************OR*************************************

even_list=[]
for i in range(4,31):
    if i%2==0:
        even_list.append(i)
print(even_list)
