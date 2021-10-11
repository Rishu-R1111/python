# creating a tuple using ()

t= (1,2,3,4,55,5,5,5,5,56,77,7,788)
print(t)
print(type(t))
# printing the elements of a tuple
print(t[0])
# cannot update the value of tuple
# t[0]=2344 #wrong way to assisgn a tuple

t1 = ()#empty tuple
print("it is an empty tuple = " ,t1,type(t1))
t2 = (1)#wrong way to dreclear a tuple
print("wrong way to declear a single elemnt tuple = " ,t2, type(t2))
t3 = (1,)#correct way to dreclear a tuple
print("correct way to declear a single elemnt tuple = ",t3,type(t3))

a= t.count(5)
print(a)

b= t.index(1)
print(b)
