#Return the largest item from the given list. l=[11,45,2,67,32,68,88,1,7] also find odd numbers from given list

l=[11,45,2,67,32,68,88,1,7]
print("Largest Number from list:",max(l))
l=[odd for odd in l if odd%2!=0]
print("Odd Number from List:",l)

**********************************OR********************************************

larg_list=[11,45,2,67,32,68,88,1,7]
larg_list.sort()
#print(larg_list)
print("largest element from list is:",larg_list[-1])
larg_list=[odd for odd in l if odd%2!=0]
print("Odd Number from List:",larg_list)

**********************************OR********************************************

larg_list=[11,45,2,67,32,68,88,1,7]
larg_num=0
for i in range(0,len(larg_list)):
    if larg_list[i]>larg_num:
        larg_num=larg_list[i]
print(larg_num)
