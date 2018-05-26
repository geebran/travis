known_users = ["khalil","tosin","sunkanmi","yusuf","haji","ridwan","abu","gbenga"]

while True:
    print("Hi! My name is Travis")
    name = input("What is your name?: ").strip().lower()

    if name in known_users:
        print("HELLO {}!".format(name))
        remove = input("Would you like to be removed from the system (y/n)?: ").strip().lower()
        if remove =="y":
            known_users.remove(name)
        elif remove == "n":
            print("no problem. i did'nt want you to leave anyway!")
        
            
    else:
        print("hmmmm i don't think i have met you yet {}".format(name))
        add_me = input("would you like to be added to the system (y/n)?: ").strip().lower()
        if add_me == "y":
            known_users.append(name)
        elif add_me == "n":
            print("no worries, see you around.")
    
   













   
   
