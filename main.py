les 2
a=input("enter seat number:")
a=int(a)
if a%2==0 and a<37:
    print('upper coupe bed')
if a%2!=0 and a<37:
    print('bottom coupe bed')
if a%2==0 and a>37:
    print('upper side bed')
if a%2!=0 and a>=37:
    print("bottom side bed")
if a>52:
    print("you have bed in the next cab")