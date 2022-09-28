n1=int(input("enter a number:"))

n2=int(input("enter another number:"))

print('operations:','addition,','subtraction,','multiplication,','division.')

operation=input("choose an operation:")

if (operation=="addition"):
    print ("answer is", n1+n2)
elif (operation=="subtraction"):
    print ("answer is", n1-n2)
elif (operation=="multiplication"):
    print ("answer is", n1*n2)
elif (operation=="division"):
    print ("answer is", n1/n2)

else: print("invalid")
