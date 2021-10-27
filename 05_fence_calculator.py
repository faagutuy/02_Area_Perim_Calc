# functions go here

# checks input is a number more than zero
def num_check(question):
    valid = False
    while not valid:
        
        error = "Please enter a number that is more than zero"
        
        try:
        
            # ask user to enter a number
            response = float(input(question))
            
            # checks number is more than zero
            if response > 0:
                return response
            
            # outputs error if input is invalid
            else:
                print(error)
                print()
                
        except ValueError:
            print(error)    
    


# Main Routine goes here

# Introduction / Heading print statements
print()
print("**** Fence Cost Calculator *****")
print()

# Start of calculator loop
keep_going = ""
while keep_going == "":

    width = num_check("Wdith: ")
    height = num_check ("Height: ")
    cost_per_m = num_check ("Cost per meter: ")

    # call your number checker function three times to get the 
    # width, length and cost_per_m of the fencing

    # Calulate perimeter (width + height) x 2
    perimeter = 2 * (width + height)

    # Calculate the cost of the fencing (perimeter x price / meter)
    Fencing = (perimeter * cost_per_m) 

    # Output the perimeter and cost of the fencing
    print("Perimeter: {:2f} units".format(perimeter))
    print("Fencing: {:2f} square units". format(cost_per_m))
    print ()
    (print)
    
    keep_going = input("Press <enter> to keep going or any key to quit")

    print ()
    print ("-" * 30)
    print()
    
print()
print("Thanks for using the Fencing cost calculator")

   
    
    