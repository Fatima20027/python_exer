def My_car():
    car = input("> ")
    if "start" in car :
        print("car starts moving")
        
    elif car == "stop" :
        print("car has stopped moving")
     
    elif car == "help" :
        print("Type:", end = "\n\n")
        print("-start: moving the car", end = "\n\n")
        print("-stop: stopping the car", end = "\n\n")
        print("-quit: quitting the car", end = "\n\n")
    elif car == "quit" :
        print("quitting the car")
        return
    
    else :
        print("this command not found")
        print("type --help for more")
    My_car()
My_car()

   



