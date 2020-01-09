def fuel_for_fuel(y):
    a = int(0)
    b = int(0)

    b = y
    
    print("We need to calculate fuel needed for fuel amount: " + str(b))

    if (b//3-2 < 0):
        print("No additional fuel required")
        return 0

    while b > 0:
        print("Calculating for y: " + str(b))
        a = a + (b//3-2)
        b = b//3-2
        print("Fuel needed so far is: " + str(a) + " and remaining fuel to calculate is " + str(b))
        if (b//3-2 < 0):
            b = 0

    print("Total fuel required for " + str(y) + " is " + str(a))
    return a

f = open("AoC1_1.txt", "r")

totalfuel = int(0)
fuelforfuel = int(0)

for x in f:
    print("Calculating fuel required for:"+ x)

    newfuel = int(0)
    newfuel = int(x)//3-2

    print("Fuel required for " + str(x) + " is " + str(newfuel))

    totalfuel = totalfuel + newfuel
    print("Total fuel needed so far is: " + str(totalfuel))

    fuelforfuel = fuel_for_fuel(newfuel)

    print("Total fuel required for " + str(x) + " is " +str(fuelforfuel + newfuel))

    totalfuel = totalfuel + fuelforfuel
       
f.close()

print ("Total fuel requirement is: " + str(totalfuel))

print("End of Program")
print("End of Program")
