import sys
# Main block of code that excutes once beforee the main
print("Welcome to My  Simple program!")
def main():
 while True:
    try:
        print("Please kindly Answer few questions as Asked")  
        name= str(input("Enter your name"))      
        age = int (input("Enter your Age"))
        if age >=40:
            print( name + " ! your and Adult")
        elif age >=20 and age <40:
            print(name + "! your a young Adult or better known as a youth") 
            
        else:
            print (name + "! your a child")   
        
        
        # Check for termination condition
        user_input = input("Do you want to exit the program? (y/n): ")
        if user_input.lower() == "y":
            exit_program()
        # Continue  and call  the main function
        else:
            main()       
     # catch exception if user inputs wrong input   
    except Exception as e:
        print(f"An error occurred: {e}")
       # exit_program()
        main()     

def exit_program():
    print("Exiting the program...")
    sys.exit(0)
#if running script, call main function while using command line eor Terminal
if __name__ == "__main__":
    main()