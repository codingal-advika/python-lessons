s1  ={2 , 3 , 1}
s2 = {'b' , 'a' , 'c'}
s3 = list(zip(s1, s2))
print(s3)
list1 = [1 , 2 , 3 , 4 , 5]
list2 = [50 , 40 , 30 , 20 , 10]
for x ,y in zip(list1 , list2[::-1]):
    print(x ,y)

stocks = ['Shorts' , 'Shirts' , 'Shoes' , 'Socks']
prices = [21 , 15  , 150 , 5]
new_dict = {stocks:prices for stocks,
            prices in zip(stocks , prices)}
print(format(new_dict))