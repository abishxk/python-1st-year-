def input1(current_balance):
    input1=int(input("do you want to continue?(yes:1/no:2):"))
    if input1==1:
        choice(current_balance)
    elif input1==2:
        print("thank you for banking")
    else:
        print('invalid input... try again :(')
        input1(current_balance)
def balance_enquiry(current_balance):
    print("your current balance is ",current_balance)
    input1(current_balance)
        
def withdraw(current_balance):
    print("your current balance is ",current_balance)
    withdraw_amt=int(input("enter amount to withdraw:"))
    current_balance-=withdraw_amt
    print("your balance after withdraw is",current_balance)
    input1(current_balance)

def deposit(current_balance):
    print("your current balance is ",current_balance)
    deposit_amt=int(input("enter amount to deposit:"))
    current_balance=current_balance+deposit_amt
    print("your balance after deposit is",current_balance)
    input1(current_balance)
    
def choice(current_balance):
    ch=int(input('''choose an option:
    1.balance enquiry
    2.withdrawl
    3.deposit
    >'''))
    if (ch==1):
        balance_enquiry(current_balance)
    elif (ch==2):
        withdraw(current_balance)
    elif (ch==3):
        deposit(current_balance)
    else:
        print('invalid input... try again :(')
        choice(current_balance)


current_balance= float(input('enter your current balance:'))
choice(current_balance)

