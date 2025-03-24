tuple1 = ('hi' , True , 5.65 , 5)
print(tuple1)
tuple2 = (56 , 10 , 7 ,19)
print(tuple2)
#tuple2[4]= 25 error: TypeError: 'tuple' object does not support item assignment
tuple3 = (9 , )
print(tuple3)
add = tuple2 + tuple3
print(add)
tuple4 = (4 , 5 , 2 , 4 , 4 , 4 , 4)
print(tuple4.count(4))
print(tuple4[0:3])
