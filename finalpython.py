popups = int(input("Please enter total popups zones on property:" ))
rotors = int(input("Please enter total rotor zones on property:"))
mprotor = int(input("Please enter total mp-rotors zones on property:"))
waterWindow = 16

def pop ():
    print(popups * 10 / 60)
    return pop()

def rotr():
    print(rotors * 25 /60)
    return rotr()

def mp():
    print(mprotor * 20 /60)
    return mp()

def totalWaterTime():
    waterTime= pop() + rotr() + mp()
    return (waterTime)


