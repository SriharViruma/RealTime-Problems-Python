while True:
        #input values will be stored in integer variables
        b3 = int(input("Enter B3: "))
        b2 = int(input("Enter B2: "))   
        b1 = int(input("Enter B1: "))
        b0 = int(input("Enter B0: "))

        vref = 5   #5volt
        rf= 10000  #10k
        r = 10000  #10k

        #Formula For Volatge Present at its non - inventing input terminal
        vo = -(vref*rf)/r * (b3/(2**0)+b2/(2**1)+b1/(2**2)+b0/(2**3))

        #Displaying the calculated value stored in Vo
        print(vo)

        #To Break Loop
        continue_program = input("Do you want to continue? (y/n): ")
        if continue_program.lower() != "y":
            break