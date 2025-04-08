numbers = input('Enter a list of numbers: ')
number = list(numbers)
squared_numbers = []
for num in number:
    squared_numbers.append(int(num) ** 2)
print(squared_numbers)
even_num = []
odd_num = []
# Check if even or odd

for n in squared_numbers:
    if n % 2 == 0:
        even_num.append (n)
        # print('The squared number is even ') 
    else:
        odd_num.append(n)
        # print('The squared number is odd!')

print('The even numbers are: ' , even_num)
print('The odd numbers are: ' , odd_num)