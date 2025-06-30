import random
import gv_die

# Read random seed to support testing (do not alter) and starting credits
seed = int(input())
random.seed(seed)

# Initial credits
credits = int(input())

# Create two GVDie objects
die1 = gv_die.GVDie()
die2 = gv_die.GVDie()

# Round counter
rounds = 0

# Game loop
while credits > 0:
    rounds += 1

    # Step 1: First roll
    die1.roll()
    die2.roll()
    total = die1.get_value() + die2.get_value()
    print(f'Dice total: {total}')

    # Determine outcome of first roll
    if total in (7, 11):
        credits += 1
        goal = -1
    elif total in (2, 3, 12):
        credits -= 1
        goal = -1
    else:
        goal = total

    # Step 2: Follow-up rolls until 7 (lose) or goal (win)
    while goal != -1:
        die1.roll()
        die2.roll()
        total = die1.get_value() + die2.get_value()
        print(f'Dice total: {total}')

        if total == 7:
            credits -= 1
            goal = -1
        elif total == goal:
            credits += 1
            goal = -1

    # Output credits after each round
    print(f'Credits: {credits}')

# Final output
print(f'Rounds: {rounds}')
