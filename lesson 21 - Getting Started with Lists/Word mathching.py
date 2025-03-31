def match_words(words):
    ctr = 0
    lst =[]
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
    
    
    print('List of words with the same first and last characters')
    return ctr


input = input('Enter a few words with at least one having the same character as the last(SEPERATE WITH COMMAS!): ')
count = match_words([input])
print('The number of words having the same letter as the last is: ' , count)



