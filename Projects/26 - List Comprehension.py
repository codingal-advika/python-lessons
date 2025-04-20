input_value = int(input('Enter a number: '))
numbers_list = list(range(input_value))
odd_numbers_list = [num for num in numbers_list if num % 2 != 0]
print('List of all numbers between the number you have entered is:', numbers_list)
print("List of odd numbers:", odd_numbers_list)
#2) Create a list of fruits
fruits = ['apple', 'banana', 'cherry', 'date', 'fig']
print(fruits)
print('Now lets convert the starting letter off these fruits to a capital letter')
updated_fruits = [fruit.capitalize() for fruit in fruits]
print('Updated list of fruits:', updated_fruits)

