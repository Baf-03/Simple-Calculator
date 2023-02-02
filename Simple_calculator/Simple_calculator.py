# Program make a simple calculator
c=0
d=0
u="n"



while True:
    
    print("\t\tSelect operation.")
    print("\t\t1.Add  +")
    print("\t\t2.Subtract  -")
    print("\t\t3.Multiply  * ")
    print("\t\t4.Divide  /")
    
    
    
    # take input from the user
    choice = input("Enter choice(1,2,3,4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        if u=="y":
            num1=d
        
        else:
            num1 = float(input("Enter first number: "))
        u="n"
        
        
        num2 = float(input("Enter second number: "))
        

        if choice == '1':
            c=c+(num1 +num2)
            print(num1, "+", num2, "=", c)

        elif choice == '2':
            c=c+(num1 - num2)
            print(num1, "-", num2, "=", c)
            

        elif choice == '3':
            
            c=c + (num1 * num2)

            print(num1, "*", num2, "=",c)
            
        elif choice == '4':
            c=c + (num1 / num2)
            print(num1, "/", num2, "=",c)
            
        
        # check if user wants another calculation
        # break the while loop if answer is no
        d=c
        next_calculation = input("Let's do new calculation? (y/n): ")
        if next_calculation == "n":
            u=input("if u want to cont previous calculation(y/n)")
            if u=="y":
                c=0
            else:
                exit=input("do u want to exit calculator(y/n): ")
                if exit=="y":
                    print("\n\t\tBYE")
                    break
                
        elif next_calculation == "yes":
            c=0
