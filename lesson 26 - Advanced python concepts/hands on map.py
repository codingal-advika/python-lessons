num1 = [1 ,2 ,3]
num2 = [4 ,5 ,6]
result = map(lambda x ,y : x + y,num1 , num2 )
print(list(result))

#Using map syntax
def cube(n):
    return n*n*n

list1 = [1 , 2 , 3 , 4 , 5]
res = map(cube , list1)
print(list(res))

