def finreducedfraction (var1,var2):
    temp1 = var1
    temp2 = var2 
    while var1 != var2:
        if var1 > var2:
            var1 = var1 - var2
        else:
            var2 = var2 - var1
        n3 = temp1 / var1
        n4 = temp2 / var2 
    print(n3," : ",n4)

print("Welcome to the program which can help you with Trigonometery! ")
print("I can do many things... ")
print("I can show you all the formulas... ")
print("standard angle table... ")
print("and much much more \n")
print("1 - for the Standard Angles ")
print("2 - for General formulas of sin, cos, tan, etc ")
option_1 = int(input())
if option_1 == 1:
    print("What do you want? - sin, cos, tan, cot, sec, cosec")
    choice = input()
    choice = choice.lower().strip()

    print("Enter angle of \u0398")
    angle_1 = input()
    angle_1 = angle_1.lower().strip()
    var3 = choice + angle_1

    if var3 == "sin0"or var3=="cos90"or var3=="tan0"or var3=="cot90":
        print("0")
    
    elif var3=="sin30"or var3=="cos60":
        print("1/2")
    
    elif var3=="sin90"or var3=="tan45"or var3=="cot45"or var3=="sec0"or var3=="cosec90":
        print("1")
    
    elif var3=="tan90"or var3=="cot0"or var3=="sec90"or var3=="cosec0":
        print("Not defined ")
    
    elif var3=="sin45"or var3=="cos45":
        print("1/\u221A 2 ")
    
    elif var3=="tan30"or var3=="cot60":
        print("1 / \u221A 3")

    elif var3=="sin60"or var3=="cos60":
        print("\u221A 3 / 2 ")

    elif var3=="sec30"or var3=="cosec60":
        print("2 / \u221A 3")

    elif var3=="sec45"or var3=="cosec45":
        print("\u221A 2")

    elif var3=="cot30"or var3=="tan60":
        print("\u221A 3")

    elif var3=="cosec30"or var3=="sec60":
        print("2")

    else:
        print("Error! Please enter correct values. ")

elif option_1 == 2:
        
    print("In the trinagle, ")

    print("Enter length of Hypotenuse: ")
    hypotenuse_2 = float (input())

    print("Enter length of Adjacent ")
    adjacent = float (input())

    print("Enter length of Opposite ")
    opposite = float (input())

    if (hypotenuse_2*hypotenuse_2) == (opposite*opposite) + (adjacent*adjacent):
        #AB hyp BC opp AC adj

        print("Sin \u0398")
        finreducedfraction(opposite,hypotenuse_2)

        print("\ncos \u0398")
        finreducedfraction(adjacent, hypotenuse_2)

        print("\ntan \u0398")
        finreducedfraction(opposite, adjacent)

        print("\ncot \u0398")
        finreducedfraction(adjacent, opposite)

        print("\nsec \u0398")
        finreducedfraction(hypotenuse_2, adjacent)

        print("\ncosec \u0398")
        finreducedfraction(hypotenuse_2, opposite)
    else:
        print("Enter correct values: ")
else:
    print("Error!! Enter correct values ")