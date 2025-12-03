import random

print("🎮 Rock Paper Scissors Game 🎮")

choices = ["rock", "paper", "scissors"]

while True:
    user = input("\nEnter your choice (rock/paper/scissors): ").lower()

    if user not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print("You chose:", user)
    print("🤖 chose:", computer)

    
    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("🎉 You win!")
    else:
        print("🤖 Computer wins!")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! 👋")
        break
