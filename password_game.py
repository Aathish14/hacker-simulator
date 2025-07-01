from utils import generate_password, generate_hint

def play_game():
    print("\n🕶️  Welcome to Hacker Simulator v1.0")
    difficulty = input("Choose difficulty (easy / medium / hard): ").lower()
    if difficulty not in ["easy", "medium", "hard"]:
        print("Invalid input! Defaulting to 'medium'.")
        difficulty = "medium"

    password = generate_password(difficulty)
    attempts = 5 if difficulty == "easy" else 7

    print("\n🔐 Password generated!")
    print("💡 Here are some hints:")
    for hint in generate_hint(password):
        print("  ➤", hint)

    for i in range(1, attempts + 1):
        guess = input(f"\n🧠 Attempt {i}/{attempts} - Enter your guess: ")
        if guess == password:
            print("🎉 Access Granted! You've guessed the password correctly.")
            break
        else:
            print("❌ Access Denied.")
    else:
        print(f"\n💀 All attempts used. The password was: {password}")

    again = input("\n🔁 Play again? (y/n): ").lower()
    if again == 'y':
        play_game()
    else:
        print("🔒 Exiting Hacker Simulator. Stay stealthy!")

if __name__ == "__main__":
    play_game()