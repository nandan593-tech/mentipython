def calroots(a,b,c):
    d=(b**2)-4*a*c
    r1=(-b+(d)**(0.5))/2*a
    r2=(-b-(d)**(0.5))/2*a
    print(f"roots:({r1}),({r2})")


a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))

calroots(a,b,c)