#Headline
print()
print('==========')
print('Calculator')
print('==========')
print()

#menu
def menu():
    print("[1] +")
    print("[2] -")
    print("[3] *")
    print("[4] /")
    print("[5] ^")
    print("[6] √")
    print('[7] Binary')
    print('[8] Octal')
    print('[9] Hexadecimal')
    print('[10] parallel resistance')
    print('[11] leg')
    print('[12] hypotenuse')
    print('[13] Circle area (radius)')
    print('[14] Circle scope (radius)')
    print('[15] Electricity(Q/T) (I)')
    print('[16] Electricity(U/R) (I)')
    print('[17] Charge(I*T) (Q)')
    print('[18] Charge(n*q) (Q)')
    print('[19] acceleration (a)')
    print('[20] current density (j)')
    print('[21] Resistance (R)')
    print('[22] tension (U)')
    print('[23] conductance (G)')

    print("[0] Exit ")

#first input
menu()
print()
option = int(input("Enter Option:"))
print()

#options
while option !=0:
    if option == 1:
      #do option 1
        print('plus')
        print()
        a = int(input('First Number:'))
        b = int(input('Second Number:'))
        q = (a + b)
        print()
        print(q)
        print()
        print('==========')

    elif option == 2:
        #do option 2
        print('minus')
        print()
        a = int(input('First Number:'))
        b = int(input('Second Number:'))
        q = (a - b)
        print()
        print(q)
        print()
        print('==========')

    elif option == 3:
        #option 3
        print('times')
        print()
        a = int(input('First Number:'))
        b = int(input('Second Number:'))
        q = (a * b)
        print()
        print(q)
        print()
        print('==========')

    elif option == 4:
        #option 4
        print('divide')
        print()
        a = int(input('First Number:'))
        b = int(input('Second Number:'))
        q = (a / b)
        print()
        print(q)
        print()
        print('==========')

    elif option == 5:
        #option 5
        print('potentiate')
        print()
        a = int(input('First Number:'))
        b = int(input('Second Number:'))
        q = (a**b)
        print()
        print(q)
        print()
        print('==========')

    elif option == 6:
        #option 6
        print('root')
        print()
        a = int(input('Enter Number:'))
        q = (a**(1/2))
        print()
        print(q)
        print()
        print('==========')

    elif option == 7:
        #option 7
        print('Binary')
        print()
        a = int(input('Number:'))
        print()
        print('in Binary:', bin(a))
        print()
        print('==========')
    
    elif option == 8:
        #option 8
        print('Octal')
        print()
        a = int(input('Number:'))
        print()
        print('in Octal:', oct(a))
        print()
        print('==========')

    elif option == 9:
        #option 9
        print('Hexadecimal')
        print()
        a = int(input('Number:'))
        print()
        print('in Hexadecimal:', hex(a))
        print()
        print('==========')

    elif option == 10:
        #option 10
        print('parallel resistance')
        print()
        a = int(input("1. resistance: "))
        b = int(input("2. resistance: "))
        print()
        q = (a*b)/(a+b)
        print(q)
        print()
        print('==========')

    elif option == 11:
        #option 11
        print('leg')
        print()
        a = int(input('leg a or b: '))
        c = int(input('hypotenuse: '))
        print()
        b = ((c**2 - a**2)**(1/2))
        print(b)
        print()
        print('==========')

    elif option == 12:
        #option 12
        print('hypotenuse')
        print()
        a = int(input('a: '))
        b = int(input('b: '))
        print()
        c = ((a**2 + b**2)**(1/2))
        print(c)
        print()
        print('==========')

    elif option == 13:
        #option 13
        print('circle area')
        print()
        r = int(input('Radius: '))
        print()
        q = (r**2 * 3.14159265359)
        print(q)
        print()
        print('==========')

    elif option == 14:
        #option 14
        print('circle scope')
        print()
        r = int(input('Radius: '))
        print()
        q = ((2 * 3.14159265359) * r)
        print(q)
        print()
        print('===========')

    elif option == 15:
        #option 15
        print('Electricity')
        print()
        Q = int(input('Q: '))
        t = int(input('t: '))
        print()
        I = (Q / t)
        print(I)
        print()
        print('==========')

    elif option == 16:
        #option 16
        print('Electricity')
        print()
        u = int(input('U: '))
        R = int(input('R: '))
        print()
        I = (u / R)
        print(I)
        print()
        print('==========')

    elif option == 17:
        #option 17
        print('Charge')
        print()
        I = int(input('I: '))
        t = int(input('t: '))
        print()
        Q = (I * t)
        print(Q)
        print()
        print('==========')

    elif option == 18:
        #option 18
        print('Charge')
        print()
        n = int(input('n: '))
        print()
        Q = (n * 1,602E-19)
        print(Q)
        print()
        print('==========')

    elif option == 19:
        #option 19
        print('acceleration')
        print()
        m = int(input('m: '))
        s = int(input('s: '))
        print()
        a = (m / s**2)
        print(a)
        print()
        print('==========')

    elif option == 20:
        #option 20
        print('current density')
        print()
        I = int(input('I: '))
        A = int(input('A: '))
        print()
        j = (I / A)
        print(j)
        print()
        print('==========')

    elif option == 21:
        #option 21
        print('Resistance')
        print()
        U = int(input('U: '))
        I = int(input('I: '))
        print()
        R = (U / I)
        print()
        print('==========')

    elif option == 22:
        #option 22
        print('Tension')
        print()
        R = int(input('R: '))
        I = int(input('I: '))
        print()
        U = (R * I)
        print()
        print('==========')

    elif option == 23:
        #option 23
        print('Conductance')
        print()
        I = int(input('I: '))
        U = int(input('U: '))
        print()
        G = (I / U)
        print(G)
        print()
        print('==========')

    else:
        #no option with entered number
        print()
        print("invalid Option")
        print()
        print('==========')

    #stop loop 
    print()
    menu()
    print()
    option = int(input("Enter Option:"))
    print()
#if number 0 => END
print('Still in Development')
print()