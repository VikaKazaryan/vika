Task 1
a=input('enter password:')
b=input('confirm password:')
if a==b:
    print('password is correct')
else:
    print('incorrect password')

Task 2
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

Task 3
def leap(y):
    if (y%4==0 and y%100!=0) or (y%400==0):
         return (f'{y}'' is leap')
    else:
        return (f'{y}'' is not leap')
y = int(input('enter year:'))
print(leap(y))

Task 4
a= input('set collor:')
if a=='red blue':
    print('purpule')
if a=='red yellow':
    print('orange')
if a=='blue yellow':
    print('green')
else:
    print('error occured')