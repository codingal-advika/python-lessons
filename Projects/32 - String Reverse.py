class Reverse:
    def __init__(self, word):
        self.word = word

    def get_reversed(self):
        return self.word[::-1]

user_input = input('Enter a word: ')
reverse_instance = Reverse(user_input)
print('The word you entered backwords is:', reverse_instance.get_reversed())