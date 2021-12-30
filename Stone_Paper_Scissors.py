import sys
import mind_behind
# S -> Stone
# P -> Paper
# Sc -> Scissors

print("Type help/Help here for valid commands.")
try:
    command = str(input("> "))
    if command == "help" or command == "Help":
        print("S/s == Stone")
        print("P/p == Paper")
        print("Sc/sc == Scissors")
        mind_behind.run()
    else:
        print("I think You Don't Read it carefully.")
        sys.exit()
except ValueError:
    print("Read the Instruction Carefully.")
    sys.exit()
