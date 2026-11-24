popups = int(input("Please enter total popups zones on property:" ))
rotors = int(input("Please enter total rotor zones on property:"))
mprotor = int(input("Please enter total mp-rotors zones on property:"))
waterWindow = int(input("Please enter your water window:"))
# ^^^ up above are all the values that will be entered by the users
def pop ():
    return(popups * 10 / 60)
    
def rotr():
    return(rotors * 25 /60)
    
def mp():
    return(mprotor * 20 /60)
    
def totalWaterTime():
    print(int(pop() + rotr() + mp()))
totalWaterTime()