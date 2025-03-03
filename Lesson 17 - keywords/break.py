word = input('Enter a word: ')
chr = 'a'
for i in word:
    if chr == i :
        print('A found in ' , word)
        break
    else:
        print('A not found in ' , word)
