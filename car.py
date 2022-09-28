

print('do you need any help?(yes/no)')
help1=""

while true:
    help1=(input('>').lower()
    start="start- TO start the car"
    stop="stop- To stop the car"
    quit="quit- To exit"
    start.upper()
    stop.upper()
    quit.upper()
    if help1=='yes':
           print(start)
           print(stop)
           print(quit)
           command=input('>')
    if command=='start':
        print('okay. car started')
        command2=input('>')
        if command2=='stop':
            print('okay! car stopped')
        elif command2=='quit':
            print('you have to stop the car first')
        else:
            print('sorry i dont understand that')
            command3=input('>')
            if command3=='stop':
                print('okay. car stopped')
                if command3=="quit":
                    print('okay. exiting car')
            else:
                print('sorry. i dont understand that')
                         
    elif command=='stop':
        print('ops! you have to start the car first')
    elif command=='quit':
        print('okay! exiting car')
    else:
        print('sorry i dont understand taht;(')
elif help1=='no':
    print("okay! see you around")
else:
    print('sorry i dont understand that :(')






