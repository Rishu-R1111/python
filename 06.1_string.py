# a=input("enter Your name = ")
# print("Good Morning, " + a )


name=input("Enter the name = ")
date=input("Enter the Date = ")
c=''' Dear NAME  YOU R SELECTED     DATE '''
          c= c.replace("DATE", date)
          c= c.replace("NAME", name)
print(c)

a= ''' DEAR NAME YOU  R SELECTED DATE'''
b=input("enter name = ")
c=input("enter date =")
a= a.replace("NAME",b)
a= a.replace("DATE",c)
print(a)
d=a.find("  ")
print(d)