# creating a list []
a=[1,2,3,4,5]
# printing the list useing list function
print(a)
# accessing index using a[1], a[2], a[0]
print(a[1],a[2],a[0])
# changing the value using index
a[0]="error"
print(a)

# list slicing
b= ["RISHU","TOM","ROHAN","SAM", "DIVYA","RIYA","SOMYA","ARYAN", 45]
print(b)

print(b[0:4])

print(b[-4:])

print(b[-6:])

# sorting in list 

c=[ 1,3,4,56,7,6,8,4]
print(c)
print(type(c))
c.sort() 
print("sorted list using c.sort() = ",c)
c.reverse() 
print("reverse list using c.reverse() = ",c)
c.append("RISHU") 
print("append list using c.append() = ",c) #(adds any deseired thing at the last in the list)
c.insert(3,"RISHU") 
print("inserting RISHU at 3rd index in the list using c.insert() = ",c) #(adds any deeseired thing at the last in the list)
print("============================================================================================\n")
print(c)
c.pop(3)  #pop 3rd index in the list i.e. 'RISHU'
print(" POPED ======>>>> INDEX 3 from the list using c.pop() = ",c)
c.insert(3,"RISHU") 
print("RISHU inserted at index 3 >",c)
c.remove("RISHU") 
print("REMOVEING RISHU  list using c.remove() = ",c) # can remove the desired element list 
print(type(c))