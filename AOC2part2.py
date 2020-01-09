# Advent of Code Day 2 - https://adventofcode.com/2019/day/2

# Libraries required

def process_code(input_list, position):


    operand_a = input_list[position + 1]
    operand_b = input_list[position + 2]
    target_location = input_list[position + 3]

    #if target_location > len(input_list):
        # Abort with invalid target location
        #print("Aborting... Invalid target location of: " + str(target_location))
        #return input_list

    if input_list[position] == 1:

        #print("Addition operator")
        #print("Operand a is: " + str(operand_a))
        #print("Operand b is: " + str(operand_b))
        #print("Target location is: " + str(target_location))

        input_list[target_location] = input_list[operand_a] + input_list[operand_b]

    elif input_list[position] == 2:
        
        #print("Multiplication operator")
        #print("Operand a is: " + str(operand_a))
        #print("Operand b is: " + str(operand_b))
        #print("Target location is: " + str(target_location))
        
        input_list[target_location] = input_list[operand_a] * input_list[operand_b]

    #print("New value for position: " + str(target_location) + " is " + str(input_list[target_location]))

    return input_list

# Main()

# Open the file of values
f = open("AOC2.test.txt", "r")

# Convert the list into integer-based list
for x in f:
    code_list = [int(x) for x in x.split (",")]

# Loop through possible values to determine what verb & noun is required
verb = 0
noun = 0
perfect_verb = int()
perfect_noun = int()
solution = int()

while noun < 100:
    while verb < 100:
        #print ("Verb:" + str(verb) + "; Noun: " + str(noun))

        # copy the original list and replace the first 2 values
        new_list = code_list.copy()
        new_list[1] = noun
        new_list[2] = verb
        position = 0

        #print("Starting copy of the list is: " + str(new_list))

        while position < len(new_list):
            #print("Processing position: " + str(position) + " which is: " + str(new_list[position]))
            if new_list[position] == 99:
                #print("Reached 99 code exit command")
                break

            #print("Calling process_code()")
            new_list = process_code(new_list, position)
            position = position + 4
        
        #print("Verb was: " + str(verb) + "; Noun was: " + str(noun) +"; Address[0] was: " + str(new_list[0]))
        #print("Ending copy of the list is: " + str(new_list))

        if new_list[0] == 19690720:
            print("Value of position [0] is 19690720 when verb = " + str(verb) + " and noun = " + str(noun))
            perfect_verb = verb
            perfect_noun = noun

        verb += 1
    verb = 0
    noun +=1

print("Perfect verb is: " + str(perfect_verb))
print("Perfect noun is: " + str(perfect_noun))

solution = (100 * perfect_noun) + perfect_verb

print("Solution is: " + str(solution))













