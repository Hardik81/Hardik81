import random
'''welcome to our game we will throw a dice twice then we will add those two numbers
we get from the dice now you have to guess the weather the sum of the numbers is in which of
the given range if you select the right you will get 100 points if you get it wrong
you will loose 50 points if you select 7 and the sum of those 2 numbers is also 7 then you get
150 points here you go you are credited 100 points already'''
a=1
k=100
while a==1 :
    c=random.randint(1,6)
    d=random.randint(1,6)
    print("select your range a)(2 to 6)","/","b)(7)","/","c)(8 to 12)")
    b=input("enter your choice")
    if b=="a":
        if c+d<=6 :
            print("the numbers are",c,",",d,"the sum is",c+d)
            print("congratulations !")
            k+=100
        else:
            print("the numbers are",c,",",d,"the sum is",c+d)
            print("oops you lost")
            k-=50
    elif b=="b":
        if c+d==7 :
            print("the numbers are",c,",",d,"the sum is",c+d)
            print("congratulations !")
            k+=150
        else:
            print("the numbers are",c,",",d,"the sum is",c+d)
            print("oops you lost")
            k-=50
    elif b=="c":
        if c+d>7 :
            print("the numbers are",c,",",d,"the sum is",c+d)
            print("congratulations !")
            k+=100
        else:
            print("the numbers are",c,",",d,"the sum is",c+d)
            print("oops you lost")
            k-=50
    else:
        print("choose right option")
        k=k
    print("your score is",k)
    m=input("do you want to continue the game yes/no:")
    if m!="yes" and m!="no":
        a=3
        print("wrong input")
    elif m=="no":
        a=2
        print("thanks for playing")
