popups = int(input("Please enter total popups zones on property: " )) #each type of sprinkler type is different and with each one a diffent set of rules 
ptime= int(input("How long do you want pop-ups to run? ")) # with ptime, mtime, rtime I allow users to adjuest total watering time of each zone so they can fine tune all zones to what they think will work best for their properties 
rotors = int(input("Please enter total rotor zones on property: "))
rtime= int(input("How long do you want rotors to run? "))
mprotor = int(input("Please enter total mp-rotors zones on property: "))
mtime= int(input("How long do you want mp-rotors to run? "))

waterWindow = int(input("Please enter your water window: ")) # this will be used as a hard block that users will enter it will later let users know if they are over their water window and have to do more steps to get it in restrictions
multiRun = int(input("How many zones can you run at once? ")) # some properties allow users to run more than one zone at a time this variable was added so that it can allow users to see total wtaering time if they ran more than one zone at a time

# ^^^ up above are all the values that will be entered by the users

# function 1
def pop ():
    return(float(popups * ptime / 60 / multiRun))
pop()

# function2    
def rotr():
    return(float(rotors * rtime /60 / multiRun))
rotr()

# function 3    
def mp():
    return(float(mprotor * mtime /60 / multiRun))
mp()

# function 4     
def totalWaterTime():
    return(float(pop() + rotr() + mp()))
totalWaterTime()
# ^^^ above are all my functions that i can test individually each one takes multiple inputs from the user to use in the math and will spit out a number that funstion 4 will use to calculate total watering time.
while True:

    while totalWaterTime() > waterWindow:
        print("Your total watering time",totalWaterTime(),"hrs is over the water window, ",waterWindow, "hrs." "You will have to adjust your watering times or apply for a watering variance if they water window is set by your local governemt.")
        ptime= int(input("How long do you want pop-ups to run? "))
        rtime= int(input("How long do you want rotors to run? "))
        mtime= int(input("How long do you want mp-rotors to run? "))

    if totalWaterTime() <= waterWindow > 0:
        print("You can water safely within the water window. Your total water time is: ", totalWaterTime(), "hrs.")

    newProperty = input("Do you want to enter a new property? (y/n): ") .strip() .lower()
    if newProperty!= "y":
            print("Bye!")
            break