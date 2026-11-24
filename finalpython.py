popups = int(input("Please enter total popups zones on property:" ))
ptime= int(input("How long do you want pop-ups to run?"))
rotors = int(input("Please enter total rotor zones on property:"))
rtime= int(input("How long do you want rotors to run?"))
mprotor = int(input("Please enter total mp-rotors zones on property:"))
mtime= int(input("How long do you want mp-rotors to run?"))

waterWindow = int(input("Please enter your water window:"))

# ^^^ up above are all the values that will be entered by the users
def pop ():
    return(popups * ptime / 60)
    
def rotr():
    return(rotors * rtime /60)
    
def mp():
    return(mprotor * mtime /60)
    
def totalWaterTime():
    print(int(pop() + rotr() + mp()))
totalWaterTime()
# ^^^ above are all my functions that i can test individually each one takes an input from the user to use in the math and will spit out a number that funstion 4 will use to calculate total watering time