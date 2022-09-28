def sortallwords (given_string):
    words=given_string.split()
    words.sort()

    print('sorted string words are:')

    for word in words:
        print(word," ")
    

stri=input('enter a string:')
sortallwords(stri)

    
