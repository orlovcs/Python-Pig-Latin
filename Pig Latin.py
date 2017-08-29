def pythonpiglatin():
    pyg = 'ay'
    original = input('Enter a word:')
    if len(original) > 0 and original.isalpha():
        print(original)
        word=original.lower()
        first=word[0]
        new_word=word+first+pyg
        print(len(new_word))
        new_word=new_word[1:7]
        print(new_word)
    else:
        print("empty")
    print(first)
