l=input("Enter a list of numbers separated by commas: ").split(",")
l=[int(i) for i in l]
s=set(l)
l1=list(s)
print(f"the numbers in the list are{l1}")