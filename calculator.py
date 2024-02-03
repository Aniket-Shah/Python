def runMatch():
    print("1.Addition\n2.Subtraction\n3.Multiple\n4.Divided\n")
    operationNumber = int(input("Enter your operation Number: "))
    match operationNumber:
            case 1 : 
                addition()
            case 2 : 
                subtraction()
            case 3 : 
                multiple()
            case 4 : 
                divided()
            case _ : 
                print("""You have enter the wrong operation number\n
                      Do you want to enter again""")
                resetFlag= input("Reset the Opertion the Enter Y/N")
                match resetFlag:
                        case "Y" : 
                            runMatch()
                        case "N" : 
                            print("===== Thank You  =====")
                        case _ : 
                            print("===== Thank You  =====")

def addition():
    a = float(input("Enter your first number: "))
    b = float(input("Enter your second number: "))
    print ("Total: ", a+b)

def subtraction():
    a = float(input("Enter your first number: "))
    b = float(input("Enter your second number: "))
    print ("Total: ", a-b)

def multiple():
    a = float(input("Enter your first number: "))
    b = float(input("Enter your second number: "))
    print ("Total: ", a*b)

def divided():
    a = float(input("Enter your first number: "))
    b = float(input("Enter your second number: "))
    if b == 0 :
        print ("Total: ", 0) 
    else :
        print ("Total: ", a/b)


print ("=====Welcom To Calculator=====")
runMatch()
