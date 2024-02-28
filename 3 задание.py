def leap(y):
    if (y%4==0 and y%100!=0) or (y%400==0):
         return (f'{y}'' is leap')
    else:
        return (f'{y}'' is not leap')
y = int(input('enter year:'))
print(leap(y))