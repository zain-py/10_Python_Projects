from PyDictionary import Dictionary

while True:
    # asking for word
    word = input('\nEnter the word: ').lower()
    
    if word == '' :
        print('No word was provided. Try Again!')
        break
    else:
        
        dict = Dictionary(word, 10)
        # asking for specifics
        print('\n What would you like to find?\n\t1) Meaning\t2) Synonyms\t3) Antonyms')
        find = input('Select from above [1/2/3]: ')
        
        if find == '1':
            dict.print_meanings()
        elif find == '2':
            dict.print_synonyms()
        elif find == '3':
            dict.print_antonyms()
        else:
            print('Incorrect input! Try Again!')
            break
