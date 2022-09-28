secret_num = 7
#guess_count
i=0
#guess_limit=3

while i<3:
    guess=int(input('guess the number:'))
    i+=1
    if guess==secret_num:
        print('yay! you won.')
        break
else:
    print('you failed :(')
