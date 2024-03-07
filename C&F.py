
def celsius_to_fahrenheit(celsius):  #function that changes temporature from Celsius to Fahrenheit
    fahrenheit = (celsius * 9/5) + 32
    print(fahrenheit)

def fahrenheit_to_celsius(fahrenheit): #function that changes temporature from Fahrenheit to Celsius
    celsius = (fahrenheit - 32) * 5/9
    print(celsius)

print("Hello, welcome!")


while True:
        greeting = input("type <continue> to continue or <exit> to exit: ")
    
        if greeting == "exit":
            break
        elif greeting != "continue":
            print("Not valid input, please try again.")
            continue
 
        print("""choose number between these options:
              1)Fahrenheit to Celsius
              2)Celsius to Fahrenheit""")
        try:
            choice = input("Enter  your choice: ")
        except ValueError:
             print("Not valid input, please try again.")
    
        if choice == "1":
            f_input = float(input("Enter temporature in fahrenheit: "))
            fahrenheit_to_celsius(f_input)                 
        elif choice == "2":
            c_input = float(input("Enter temporature in celsius: "))
            celsius_to_fahrenheit(c_input)
        elif choice == "exit":
             break  
        else:
            print("Not valid input, please try again.")          

if "exit" in greeting:
     exit()
            
            
        
        
