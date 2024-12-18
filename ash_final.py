def activity_1():
    print(f"Hello World")
def activity_2():
    name = input ("Enter a name:")
    print ("Hi" + name )
def activity_3():
    name = input("Please input your name here ---> ")
    fname = input("Please input your fname here ---> ")
    mname = input("Please input your mname here ---> ")
    birthdate = input("Please input your birth date here ---> ")
    birthmonth = input("Please input your birthmonth here ---> ")
    birthyear = input("Please input your birthyear here ---> ")
    maritalstatus = input("Please input your maritalstatus here ---> ")
    religion = input("Please input your religion here ---> ")
    ethnicity = input("Please input your ethnicity here ---> ")
    mobile = input("Please input your mobile here ---> ")
    email = input("Please input your email here ---> ")
    gender = input("Please input your gender here ---> ")
    address = input("Please input your address here ---> ")
    age = input(" Please input your age here ---> ")


    print("\n\n\n\n\tHello, My name is,", name ,"I'm", age ,"yrs old.\n\tI identify as", gender ,"\n\tMy father's name is", fname ,"\n\tMy mother's name is", mname ,"\n\tMy Bithday is in", birthmonth , birthdate , birthyear ,"\n\tI live in", address,"\n\tI am", maritalstatus ,"\n\tI am", ethnicity ,"Citizen\n\tMy mobile number is:", mobile ,"\n\tYou may contact me in my email:", email ,"\n\tThank You!!!\n\n\n")
def activity_4():
    number1=eval(input("Enter the first number:"))
    number2=eval(input("Enter the second number:"))
    sum=number1+number2
    minus=number1-number2
    product=number1*number2
    quotient=number1/number2
    expo=number1**number2
    rem=number1%number2
    floor=number1//number2

    print("The sum of", number1,"and", number2, "is", sum)
    print("The difference of", number1, "and" ,number2, "is", minus)
    print("The product of", number1, "and", number2, "is",product)
    print("The quotient of",number1, "and", number2, "is",quotient)
    print(number1,"exponent by", number2,"is", expo)
    print("The remainder of", number1,"and", number2,"is", rem)
    print("The floor division of", number1,"and", number2, "is", floor)
def activity_5():
    x = 5

    print (x)

    x = x + 10

    print (x)

    x = x + 15

    print(x)

    x += 10

    print(x)
def activity_6():
    print("Farenheit to Celsius Converter Program")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Welcome to converter!")

    F= eval(input("Enter temperature in Farenheit:"))
    celsius=(F-32)*5/9

    print(f"The conversion of {F} degrees farenheit is {celsius} degrees Celsius")
    print(f"The conversion of {F} degrees Farenheit is {round(celsius,2)} degrees Celsius")
def activity_7():
    AA = input("What's your name, miner? ")
    print("\n")
    A = 0
    B = input("Have you mined today? ")
    print("\n")

    if B.upper() == "YES":
            C = eval(input("How many Golds did you mined? "))
            print("\n")
            D = A + C
            print("Congratulations! ",AA,"You have mined ", D," golds, today")
    elif B.upper() != "YES":
            print("\n")
            print("That's unfortunate, ",AA,"you've mined ", A, "golds today")
            print(" you should mine more efficient ", AA)
def activity_8():
    p = input("enter your password----------->")
    if p.lower() == "BsIt1c":
        print("\n")
        print("Welcome user!!")
        print("Enjoy using the system!!")
    elif p.lower() == "missnakita":
        print("\n")
        print("Welcome user!!")
        print("Enjoy using the system!!")
    else:
        print("\n")
        print("Pass Incorrect")
        print("\n")
    print("Thank you,user, for using the system!!")
def activity_9():
    A = eval(input("Enter Age ---------->"))

    if A >= 1 and A<= 7:
        print("toddler")
    elif A >= 8 and A <= 13:
        print("pre teen")
    elif A >= 14 and A <= 18:
        print("teenager")
    elif A >= 19 and A <= 31:
        print("early adulthood")
    elif A >= 32 and A <= 45:
        print("mid adulthood")
    elif A >= 46 and A <= 59:
        print("post adulthood")
    elif A >= 60 and A <= 100:
        print("senior")
    elif A >= 100:
        print("Ancient")
def activity_10():
    DLL = input("Are you a student of DLL? (yes/no??) : ")

    if DLL.lower() == "yes":
        print("Good Morning Student!","\nWelcome to the DLL Scholarship Form!")

        yearlv = input("What is your current year in DLL?")
        if yearlv.lower() == "freshman":
            print("Hello Freshmen of DLL!")
        elif yearlv.lower() == "freshmen":
            print("Hello freshmen of DLL!") 
        elif yearlv.lower() == "junior":
            print("Konnichiwa Junior_kun of DLL!")
        elif yearlv.lower() == "senior":
            print("Welcome Senior of DLL!")
        else: 
                print("???")
        youNeed = input("Do you need this scholarship?? (y/n) : ")
        if youNeed.lower() == "yes":
            print ("Scholarship Granted :}")
        else:
            print("Okay thanks for using it")
def activity_11():
    for me in range (1 , 101):
        print(me, 'GOODBYE WORLD')
def activity_12():
    for cycle in range (10,0,-1):
        print(cycle)
def activity_13():
    sum = 1
    num=int(input('Enter a number: '))

    for x in range (num,0,-1):
        sum *= x
    print(f"The factorial of {num} is {sum}")
def activity_14():
    for x in range (1,6):
        for y in range(1, x + 1):
            print(" ",end = " ")
        for z in range(6, x, -1):
            print("*",end=" ")
        print()
def activity_15():
    for x in range(1,11,1):
        print(end="")
        for y in range(x,11,1):
            print(end=" ")
        print("* " * x)
        for b in range(11,x,-1):
            print(end=" ")
        print("* " * x)
def activity_16():
    t = int(input("Enter a number range: "))
    for x in range(1,t):
        for a in range(1,x,1):
            print(" ",end="  ")
        for b in range(t,x,-1):
            print("* ",end=" ")
            
def activity_17():
    col = eval(input("Enter number of columns---> "))


    for x in range (1, 11):
        for y in range (1, col + 1):
            print(f"{x} x {y} = {x*y}" ,end="\t")
        print()
def activity_18():
    A = int(input("enter a value:"))
    for x in range(1,6):
        for r in range(1,A+1):
            for y in range(1,x+1):
                print("*",end=" ")
            for z in range(x,6):
                print(" ",end=" ")
        print()
def activity_19():
    tama = True

    while tama == True:

        ask = input("Enter your name: ")
        if ask.lower() == "stop":
            break
            ask == False
def activity_20():
    import os 
    tama = True
    no = 0
    while tama == True:
        ask = input("would you like to continue? (yes/no)")
        if ask.lower() == "no":
            print(" Program Terminated")
            break
            ask == False
        else:
            os.system('cls')
            for x in range(1,6):
                no += 1
                for r in range(1,no+1):
                    for y in range(1,x+1):
                        print("*",end=" ")
                    for z in range (5,x,-1):
                        print(" ",end=" ")
                    print()
                continue
def activity_21():
    print("\n\t====================== ACTIVITY 21 ======================\n")
    tuloy = True
    nameno = 0
    while tuloy == True:
            name = input("Enter a name: ")

            if name.lower() == "stop":
                print("Okay tama na\n")
                print(f"You have entered a total of {nameno} names!")
                break

            else:
                print(f"type 'stop' if you want to terminate the program\n")
                nameno += 1
                continue
def activity_22():
    def activity22():
        def activity1():
            print("Hello World")
        activity1()
    activity22()
def activity_23():
    def factorial(number):
        """ This function's purpose is to compute/calculate the factorial of any number given """
        fact = 1
        for x in range(number, 0, -1):
            fact *= x

        return fact

    print(f"the factorial of 13 is {factorial(13)}")
def activity_24():
    from Activity23 import factorial

    print(f"the factorial of 7 is {factorial(7)} ")
def activity_25():
    courses = ["BSIT", "BSA", "BSAIS", "BTVTED", "BSSW", "BSPA", "Delete w/o index", "Delete with index"]

    courses.remove("Delete w/o index")
    courses.pop()
    courses.append("DHRS")
    courses.insert(0, "ABELS")

    print(courses)

def code_challenge1():
    print("\t\t\t\t\t\t\t\t\t*\n\n\t\t\t\t\t\t\t\t*\t*\t*\n\n\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\n\t\t\t\t\t\t*\t*\t*\t*\t*\t*\t*\n\n\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\n\t\t\t\t\t\t\t\t*\t*\t*\n\n\t\t\t\t\t\t\t\t\t*")
def code_challenge2():
    name = input ("Please enter your name --->")

    print("\t\t\t\t\t\t\t\t\t*\n\n\t\t\t\t\t\t\t\t*\t*\t*\n\n\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\n\t\t\t\t\t\t*\t\t"+("Hi!" + name)+"\t\t\t*\n\n\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\n\t\t\t\t\t\t\t\t*\t*\t*\n\n\t\t\t\t\t\t\t\t\t*")
def code_challenge3():
    fullname=input("Name:")
    age=input("Age:")
    birthdate=input("Date of Birth:")
    birthplace=input("Place of Birth:")
    dialect=input("Dialect:")
    address=input("Address:")
    origin=input("Nationality")
    religion=input("Religion:")
    status=input("Civil Status:")
    sex=input("Sex:")
    father=input("Father's Name:")
    mother=input("Mother's Name:")
    email=input("Email:")
    phone=input("Phone No.:")

    print("\n\n\nConclusion:\n Hi! my name is"+ fullname +",I am",age,"years old,And I was born on",birthdate,"at" ,birthplace,".My nationality is"+ origin +",My father's name is"+ father +"and my mother's name is"+ mother +". I live in" + address,",you can contact me on", email ,"or at", phone,".")
def code_challenge4():
    number1=eval(input("Enter the first number:"))
    number2=eval(input("Enter the second number:"))
    sum=number1+number2
    minus=number1-number2
    product=number1*number2
    quotient=number1/number2
    expo=number1**number2
    rem=number1%number2
    floor=number1//number2

    print("The sum of", number1,"and", number2, "is", sum)
    print("The difference of", number1, "and" ,number2, "is", minus)
    print("The product of", number1, "and", number2, "is",product)
    print("The quotient of",number1, "and", number2, "is",quotient)
    print(number1,"exponent by", number2,"is", expo)
    print("The remainder of", number1,"and", number2,"is", rem)
    print("The floor division of", number1,"and", number2, "is", floor)
def code_challenge5():
    print("Welcome to AJ's Bank Deposit PH")
    print("----------------------------------------------------------------------------------------------------------------------------------")
    money = eval(input("Please enter your deposit amount:"))

    print (f"Your deposit amount is {money}")

    th = money//1000
    fh = money - (th*1000)
    fh2 = fh//500
    toh = fh - (fh2*500)
    toh2 = toh//200
    oh = toh - (toh2*200)
    oh2 = oh//100
    ff = oh -(oh2*100)
    ff2 = ff//50
    to = ff - (ff2*50)
    to2 = to//20
    ten = to - (to2*20)
    ten2 = ten//10
    five = ten - (ten2*10)
    five2 = five//5
    one = five - (five2*5)
    one2 = one//1


    print ("The denomination of your deposit is:")

    print (th,"- 1000")
    print (fh2,"- 500")
    print (toh2,"- 200")
    print (oh2,"- 100")
    print (ff2,"- 50")
    print (to2,"- 20")
    print (ten2,"- 10")
    print (five2,"- 5")
    print (one2,"- 1")
def code_challenge6():
    print ("Please fill up the following to get your Final Grades")

    prelim = eval(input("Prelim Grade:"))
    midterm = eval(input("Midterm Grade:"))
    sfinals = eval(input("Semi-Finals Grade:"))
    finals = eval(input("Finals Grade:"))
    quiz = eval(input("Quiz Grade:"))
    project = eval(input("Project Grade:"))

    if (prelim >=65 and prelim <=100) and (midterm >=65 and midterm <=100) and (sfinals >=65 and sfinals <=100) and (finals >=65 and finals <=100) and (quiz >=65 and quiz <=100) and (project >=65 and project <=100):
        FG = (prelim * 0.15) + (midterm * 0.15) + (sfinals * 0.15) + (finals * 0.15) + (quiz * 0.15) + (project * 0.15)
        if FG >= 75:
            print (" Congratulations, you passed the course/subject ")
        else:
            print (" Sorry, better luck next time ")

    else:
        print ("INVALID GRADE")
def code_challenge7():
    isBuy = input("Do you want make a grocery purchase (yes/no): ")

    if isBuy.lower() == "yes" :
        item_name = input("Enter the item name: ")
        item_price = eval(input("Enter the price of the item: "))
        age = eval(input("Enter your age: "))
        cash = eval(input("Enter the amount of cash you have given: "))
        
        discount_amount = round(item_price * 0.060, 4)
        discount_price = round(item_price - discount_amount, 4)
        tax_amount = round(item_price * 0.155, 4)
        tax_price = round(item_price + tax_amount)
        
        if age >= 60:
            print(f"\nHi, our dear customer, you purchased a/an {item_name}, that costs {item_price}Php plus a 5.2% discount {discount_amount}Php to your total purchase. ")
            print(f"Total: {round(item_price - discount_amount, 4)} ")
            print(f"Change: {round(cash - discount_price, 4)} ")
            print("Thank  you for shopping, see you next time! ")

        elif age >=18:
            print(f"\nHello!, you have purchased {item_name}, that costs {item_price}Php plus a 14.3% tax {tax_amount}Php to your total purchase. ")
            print(f"Total: {round(item_price + tax_amount, 4)} ")
            print(f"Change: {round(cash - tax_price, 4)} ")
            print("Thank you for shopping,Hope to see you  next time! ")
        
        else:
            print()
            
    else:
        print("\nThank you for shopping with us! we hope to see you again.")
def code_challenge8():
    odd = 0
    even = 0
    sum = 0
    for x in range(1, 11):
        num = eval(input(f"Enter #{x} :"))
        sum += num
        if num % 2 == 0:
            even += num
        else:
            odd += num

    print(f"the sum of all the numbers given is {sum}")
    print(f"the sum of all the numbers given is {odd}")
    print(f"the sum of all the numbers given is {even}")
def code_challenge9():
    for x in range(1,6):
        for y in range(1, x + 1):
            print("*",end=" ")
        print()
def code_challenge10():
    for x in range(1,6):
        for y in range(6, x, -1):
            print(" ", end = " ")
        for z in range(0,x):
            print("*", end= " ")
        for a in range(x, 6, -1):
            print("*",end =" ")
        for j in range(0, x):
            print("*", end= " ")
        print()

    for x in range(1,6):
        for y in range(1, x + 1):
            print(" ", end = " ")
        for z in range(6, x, -1):
            print("*",end=" ")
        for a in range(6, x, -1):
            print("*",end=" ")
        print()
def code_challenge11():
    for x in range(1,7):
        for y in range(6, x, -1):
            print("", end="")
        for z in range(x, 1, -1):
            print(z, end="")
        for a in range(1, x + 1):
            print(a, end="")
        print()

    for x in range(5, 0, -1):
        for y in range(6, x, -1):
            print("", end="")
        for z in range(x, 1, -1):
            print(z, end="")
        for a in range(1, x + 1):
            print(a, end="")
        print()
def code_challenge12():
    for x in range(1,5):
        for y in range(5, x, -1):
            print("", end="")
        for z in range(1, x):
            print("*", end="")
        for a in range(1,x):
            print("*", end="")
        print()

    for i in range(x):
        for j in range(x-1):
            print("", end="")
        print("* * *")
def code_challenge13():
    for x in range(1,7):
        for y in range(6, x, -1):
            print(" ",end="")
        for z in range(x, 1, -1):
            print(z, end="")
        for a in range(1, x + 1):
            print(a, end="")
        print()
def code_challenge14():
    dang = True
    bilang = 0

    while dang == True:
        num = eval(input("Write a number:   "))

        if num == 0:
            print("Loop has terminated")
            print(f"The sum of all numbers given is {bilang}")
            break
            
        else:
            bilang += num
            continue
def code_challenge15():
    import os

    ting = True
    nut = 0

    while ting == True:
        ilan = input("\nDo you wish to create more triangle (yes/no) ? ")

        if ilan.lower() == "no":
            os.system("cls")
            print("Program terminated")
            break

        elif ilan.lower() == "yes":
            os.system("cls")
            nut += 1
            for x in range(1,6):
                for y in range(1,nut+1):
                    for z in range(1,x+1):
                        print("*", end= " ")
                    for a in range(5,x,-1):
                        print(" ", end= " ")
                    print( end= " ")
                print()
                continue
        else:
            os.system
            print("\nInvalid input, Please enter 'yes' or 'no' only")
            continue
def code_challenge16():
    def denomination() : pass
    def account() : pass
    def deposit() : pass
    def withdraw() : pass
    def balance() : pass
    def main() : pass
    while True:
        print("banking system")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("commands (1 - 5)")
        print("1 ---- Create Account")
        print("2 ---- Deposit")
        print("3 ---- Withdrawal")
        print("4 ---- Check balance")
        print("5 ---- Exit")

        coms = input("enter a command")
        if coms == "1":
            pass
        elif coms == "2":
            pass
        elif coms == "3":
            pass
        elif coms == "4":
            pass
        elif coms == "5":
            break
        else:
            pass
        print("")
        print("")    

def menu():
    tuloy = True
    while tuloy == True:
        print("\n\t\t\t\t\t############################################################\n")
        print("\t\t\t\t\t\t\tWelcome to my program! ")
        print("\n\t\t\t\t\t############################################################\n")
        print("\n\t\t\t\t\t#######################| Activities |#######################\n")
        print("\t\t\t\t\t|| A1 - activity 1                       A14 - activity 14 ||")
        print("\t\t\t\t\t|| A2 - activity 2                       A15 - activity 15 ||")
        print("\t\t\t\t\t|| A3 - activity 3                       A16 - activity 16 ||")
        print("\t\t\t\t\t|| A4 - activity 4                       A17 - activity 17 ||")
        print("\t\t\t\t\t|| A5 - activity 5                       A18 - activity 18 ||")
        print("\t\t\t\t\t|| A6 - activity 6  13 - Actactivity 13  A19 - activity 19 ||")
        print("\t\t\t\t\t|| A7 - activity 7                       A20 - activity 20 ||")
        print("\t\t\t\t\t|| A8 - activity 8                       A21 - activity 21 ||")
        print("\t\t\t\t\t|| A9 - activity 9                       A22 - activity 22 ||")
        print("\t\t\t\t\t|| A10 - activity 10                     A23 - activity 23 ||")
        print("\t\t\t\t\t|| A11 - activity 11                     A24 - activity 24 ||")
        print("\t\t\t\t\t|| A12 - activity 12                     A25 - activity 25 ||")
        print("\n\t\t\t\t\t##########################################################\n\n")


        print("\n\t\t\t\t\t#######################| Code Challenges |#######################\n")
        print("\t\t\t\t\t|| C_1 - Code Challenge 1               C_9 - Code Challenge 9   ||")
        print("\t\t\t\t\t|| C_2 - Code Challenge 2               C_10 - Code Challenge 10 ||")
        print("\t\t\t\t\t|| C_3 - Code Challenge 3               C_11 - Code Challenge 11 ||")
        print("\t\t\t\t\t|| C_4 - Code Challenge 4               C_12 - Code Challenge 12 ||")
        print("\t\t\t\t\t|| C_5 - Code Challenge 5               C_13 - Code Challenge 13 ||")
        print("\t\t\t\t\t|| C_6 - Code Challenge 6               C_14 - Code Challenge 14 ||")
        print("\t\t\t\t\t|| C_7 - Code Challenge 7               C_15 - Code Challenge 15 ||")
        print("\t\t\t\t\t|| C_8 - Code Challenge 8               C_16 - Code Challenge 16 ||")
        print("\n\n\t\t\t\t\t\t\t\t\t\t\t0 - Exit")
        print("\n\t\t\t\t\t###############################################################\n\n")

        ash = input ("Enter a number:")
        if ash == "Exit" or ash == "0":
            break
        elif ash != "Exit":
            if ash == "A1":
                activity_1 ()
                continue
            elif ash == "A2":
                activity_2()
                continue
            elif ash == "A3":
                activity_3()
                continue
            elif ash == "A4":
                activity_4()
                continue
            elif ash == "A5":
                activity_5()
                continue
            elif ash == "A6":
                activity_6()
                continue
            elif ash == "A7":
                activity_7()
                continue
            elif ash == "A8":
                activity_8()
                continue
            elif ash == "A9":
                activity_9()
                continue
            elif ash == "A10":
                activity_10()
                continue
            elif ash == "A11":
                activity_11()
                continue
            elif ash == "A12":
                activity_12()
                continue
            elif ash == "A13":
                activity_13()
                continue
            elif ash == "A14":
                activity_14()
                continue
            elif ash == "A15":
                activity_15()
                continue
            elif ash == "A16":
                activity_16()
                continue
            elif ash == "A17":
                activity_17()
                continue
            elif ash == "A18":
                activity_18()
                continue
            elif ash == "A19":
                activity_19()
                continue
            elif ash == "A20":
                activity_20()
                continue
            elif ash == "A21":
                activity_21()
                continue
            elif ash == "A22":
                activity_22()
                continue
            elif ash == "A23":
                activity_23()
                continue
            elif ash == "A24":
                activity_24()
                continue
            elif ash == "A25":
                activity_25()
                continue
            elif ash == "C_1":
                code_challenge1()
                continue
            elif ash == "C_2":
                code_challenge2()
                continue
            elif ash == "C_3":
                code_challenge3()
                continue
            elif ash == "C_4":
                code_challenge4()
                continue
            elif ash == "C_5":
                code_challenge5()
                continue
            elif ash == "C_6":
                code_challenge6()
                continue
            elif ash == "C_7":
                code_challenge7()
                continue
            elif ash == "C_8":
                code_challenge8()
                continue
            elif ash == "C_9":
                code_challenge9()
                continue
            elif ash == "C_10":
                code_challenge10()
                continue
            elif ash == "C_11":
                code_challenge11()
                continue
            elif ash == "C_12":
                code_challenge12()
                continue
            elif ash == "C_13":
                code_challenge13()
                continue
            elif ash == "C_14":
                code_challenge14()
                continue
            elif ash == "C_15":
                code_challenge15()
                continue
            elif ash == "C_16":
                code_challenge16()
                continue

menu ()