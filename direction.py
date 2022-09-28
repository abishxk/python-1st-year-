dirt = input("Enter your direction (NORTH/SOUTH/EAST/WEST):")
ang = int(input("Enter your angle (45/90/180/360) :"))
rot = input("Enter your rotation (CW-Clockwise/ACW-AntiClock wise):")

if dirt.lower()=="south" and ang == 45 and rot.lower()=="cw":
    print("Southwest")
elif dirt.lower()=="south" and ang == 45 and rot.lower()=="acw":
    print("Southeast")
elif dirt.lower()=="south" and ang == 90 and rot.lower()=="acw":
    print("East")
elif dirt.lower()=="south" and ang == 90 and rot.lower()=="cw":
    print("West")
elif dirt.lower()=="south" and ang == 180 and rot.lower()=="cw":
    print("North")
elif dirt.lower()=="south" and ang == 180 and rot.lower()=="acw":
    print("North")
elif dirt.lower()=="south" and ang == 360 and rot.lower()=="cw":
    print("South")
elif dirt.lower()=="south" and ang == 360 and rot.lower()=="acw":
    print("South")
    
elif dirt.lower()=="north" and ang == 90 and rot.lower()=="cw":
    print("East")
elif dirt.lower()=="north" and ang == 90 and rot.lower()=="acw":
    print("West")
elif dirt.lower()=="north" and ang == 45 and rot.lower()=="acw":
    print("Northwest")
elif dirt.lower()=="north" and ang == 45 and rot.lower()=="cw":
    print("Northeast")
elif dirt.lower()=="north" and ang == 180 and rot.lower()=="cw":
    print("South")
elif dirt.lower()=="north" and ang == 180 and rot.lower()=="acw":
    print("South")
elif dirt.lower()=="north" and ang == 360 and rot.lower()=="cw":
    print("North")
elif dirt.lower()=="north" and ang == 360 and rot.lower()=="acw":
    print("North")

    
elif dirt.lower()=="east" and ang == 90 and rot.lower()=="cw":
    print("South")
elif dirt.lower()=="east" and ang == 90 and rot.lower()=="acw":
    print("North")
elif dirt.lower()=="east" and ang == 45 and rot.lower()=="acw":
    print("Northeast")
elif dirt.lower()=="east" and ang == 45 and rot.lower()=="cw":
    print("Southeast")
elif dirt.lower()=="east" and ang == 180 and rot.lower()=="cw":
    print("West")
elif dirt.lower()=="east" and ang == 180 and rot.lower()=="acw":
    print("West")
elif dirt.lower()=="east" and ang == 360 and rot.lower()=="cw":
    print("East")
elif dirt.lower()=="south" and ang == 360 and rot.lower()=="acw":
    print("East")
    
elif dirt.lower()=="west" and ang == 90 and rot.lower()=="cw":
    print("North")
elif dirt.lower()=="west" and ang == 90 and rot.lower()=="acw":
    print("South")
elif dirt.lower()=="west" and ang == 45 and rot.lower()=="acw":
    print("Southwest")
elif dirt.lower()=="west" and ang == 45 and rot.lower()=="cw":
    print("Northweast")
elif dirt.lower()=="west" and ang == 180 and rot.lower()=="cw":
    print("East")
elif dirt.lower()=="west" and ang == 180 and rot.lower()=="acw":
    print("East")
elif dirt.lower()=="west" and ang == 360 and rot.lower()=="cw":
    print("West")
elif dirt.lower()=="west" and ang == 360 and rot.lower()=="acw":
    print("West")
    
else:
    print("Enter correct input")


