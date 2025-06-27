l=input("Enter a list of numbers separated by commas: ").split(",")
l=[int(i) for i in l]
l1=[]
for i in l:
    if i in l1:
        continue
    else:
       l1.append(i)
l1.sort()
print(f"the numbers in the list are{l1}")