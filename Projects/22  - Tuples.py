tuple1 = (4 , 3 , 2 , 2 ,-1 , 18)
print(tuple1)
tuple2 = (2 , 4 ,8 , 8 , 3 , 2 , 9 )
print(tuple2)
combine  = tuple1 + tuple2
result = 1
for num in combine:
    result *= num
print('The product of all your numbers multiplied together is: ' , result)