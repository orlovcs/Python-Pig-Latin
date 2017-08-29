def pythonpiglatin():
    pyg = 'ay'
    original = input('Enter a word:')
    if len(original) > 0 and original.isalpha():
        print('Original word is: ' + original)
        word=original.lower()
        first=word[0]
        new_word=word+first+pyg
        new_word=new_word[1:7]
        print ("Length of new word is: " + str(len(new_word)))
        print('Word in pig latin is: ' + new_word)
    else:
        print("Word is invalid")
