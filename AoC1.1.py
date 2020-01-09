import logging

# Setup logging parameters
logging.basicConfig(
    level=logging.DEBUG,
    filename='AOC1.log',
    filemode= 'w',
    format='%(name)s - %(levelname)s - %(message)s')

def calculate_fuel_for_fuel(y):
    a = int(0)
    b = int(0)

    b = y
    
    logging.debug("We need to calculate fuel needed for fuel amount: " + str(b))

    if (b//3-2 < 0):
        logging.debug("No additional fuel required")
        return 0

    while b > 0:
        logging.debug("Calculating for y: " + str(b))
        a = a + (b//3-2)
        b = b//3-2
        logging.debug("Fuel needed so far is: " + str(a) + " and remaining fuel to calculate is " + str(b))
        if (b//3-2 < 0):
            b = 0

    logging.debug("Total fuel required for " + str(y) + " is " + str(a))
    return a

# Open the file of input data
fuel_input_data = open("AoC1_1.txt", "r")

# Declare variables
total_fuel = int(0)       # Stores total fuel required
fuel_for_fuel = int(0)     # Stores fuel requirements for the fuel payload

# For each input value, calculate the fuel required, then calculate the fuel required to support the fuel itself
for distance in fuel_input_data:
    logging.debug("Calculating fuel required for:" + distance.rstrip())

    fuel = int(0)
    new_fuel = int(distance)//3-2

    logging.debug("Fuel required for " + distance.rstrip() + " is " + str(new_fuel))

    total_fuel = total_fuel + new_fuel
    logging.debug("Total fuel needed so far is: " + str(total_fuel))

    fuel_for_fuel = calculate_fuel_for_fuel(new_fuel)

    logging.debug("Total fuel required for " + distance.rstrip() + " is " + str(fuel_for_fuel + new_fuel))
    logging.debug("===================================================================")

    total_fuel = total_fuel + fuel_for_fuel
       
fuel_input_data.close()

logging.debug("Total fuel requirement is: " + str(total_fuel).rstrip())
