import random
import sys


def run():
    try:
        winning_scores = int(input("Enter the Maximum Score:> "))
    except ValueError:
        print("Enter a Number Only")
        sys.exit()
    valid = ["S", "P", "Sc", "s", "p", "sc"]
    try:
        while winning_scores != 0:
            ran = random.choice(valid)
            us = str(input("Enter your choice:> "))
            if us == valid[0] or us == valid[3]:
                if ran == valid[1] or ran == valid[4]:
                    print("You Lose.")
                    print("Opponent Choose: "+"Paper")
                elif ran == valid[2] or ran == valid[5]:
                    print("You Won.")
                    print("Opponent Choose: "+"Scissors")
                elif ran == valid[0] or ran == valid[3]:
                    print("It's a Draw.")
                    print("Opponent Choose: "+"Stone")
            elif us == valid[1] or us == valid[4]:
                if ran == valid[0] or ran == valid[3]:
                    print("You Won.")
                    print("Opponent Choose: "+"Stone")
                elif ran == valid[2] or ran == valid[5]:
                    print("You Lose.")
                    print("Opponent Choose: "+"Scissors")
                elif ran == valid[1] or ran == valid[3]:
                    print("It's a Draw.")
                    print("Opponent Choose: "+"Paper")
            elif us == valid[2] or us == valid[5]:
                if ran == valid[0] or ran == valid[3]:
                    print("You Lose.")
                    print("Opponent Choose: "+"Stone")
                elif ran == valid[1] or ran == valid[3]:
                    print("You Won.")
                    print("Opponent Choose: "+"Paper")
                elif ran == valid[2] or ran == valid[5]:
                    print("It's a Draw.")
                    print("Opponent Choose: "+"Scissors")
            else:
                print("I think you are out of your mind.")
                break
            winning_scores -= 1
    except ValueError:
        print("Enter A Valid Choice.")
        sys.exit()
