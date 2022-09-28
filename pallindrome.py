word=input('enter a string:')

while True:
    reverse=word[::-1]
    if word==reverse:
        print(f"the given string '{word}' is a pallindrome")
        break
    else:
        print(f"the given string '{word}' is not a pallindrome")
        break 
