test_dict = {'codingal': 3, 'is': 2, 'best': 2, 'coding': 1}
print(test_dict)
letter = input('Enter the letter you want to check from the dictionary above: ')
frequency = sum(key.count(letter) for key in test_dict)
print(f'The letter {letter} has been repeated {frequency} times.')

