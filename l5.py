l=input("Enter a list of numbers separated by commas: ").split(",")
l=[int(i) for i in l]
n=int(input("Enter the number to be searched: "))
c=0
for i in l:
    if n == i:
        c+=1
print(f"the number {n} is present in the list {c} times")    