import art
import data
import random
import os

def get_random_account():
    return random.choice(data.data)

def compare_followers(account_a, account_b):
    if account_a["follower_count"] > account_b["follower_count"]:
        return "a"
    else:
        return "b"

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def game():
    global score
    os.system("cls")
    print(art.logo)
    if score > 0:
        print(f"You're right! Current score: {score}.")
    elif score == -1:
        print(f"Sorry, that's wrong. Final score: {score}.")
        input("Press enter to exit.")
        return
    account_a = get_random_account()
    account_b = get_random_account()
    higher_follower = compare_followers(account_a, account_b)
    print(f"Compare A: {format_data(account_a)}.")
    print(art.vs)
    print(f"Against B: {format_data(account_b)}.")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if guess == higher_follower:
        score += 1
        game()
    else:
        score = -1
        game()
    
if __name__ == "__main__":
    score = 0
    game()