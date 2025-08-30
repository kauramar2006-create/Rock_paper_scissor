import random   # Importing random module to let computer choose randomly

print("\nRock-Paper-Scissor Game")   # Title of the game

# Available choices for the game
choices = ['rock', 'paper', 'scissor']

# Ask the user how many points are required to win
target = int(input("\nEnter the points required to win : "))

# Initialize scores
user_score = 0
computer_score = 0

# Run the loop until either the user or computer reaches the target score
while user_score != target and computer_score != target:

    # Take user input and convert it to lowercase for consistency
    user = input("\nEnter your choice: (rock, paper, scissor) or press q to quit: ").lower()

    # Quit option
    if user == 'q':
        print("You quit the game!")
        print(f"You scored : {user_score}/{target}")
        print(f"Computer scored : {computer_score}/{target}")
        break

    # Validate user input
    if user not in choices:
        print(" Invalid choice! Please enter rock, paper, or scissor.")
        continue   # Skip rest of loop and ask again

    # Computer makes a random choice
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    # Check all possible outcomes
    if user == computer:
        # It's a tie → no points awarded
        pass

    # User winning conditions
    elif (user == 'paper' and computer == 'rock') or \
         (user == 'scissor' and computer == 'paper') or \
         (user == 'rock' and computer == 'scissor'):
        user_score += 1
    
    # Otherwise computer wins
    else:
        computer_score += 1

    # Print current score after each round
    print(f"\nScore -> User : {user_score} | Computer : {computer_score}")
    
# The while loop ends when either user_score == target or computer_score == target
else:
    if user_score == target:
        print("\n🎉 Congratulations! You won the game 🎉")
    else:
        print("\n💻 Computer won the game! Better luck next time")
