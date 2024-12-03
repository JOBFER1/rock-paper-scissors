def validate_input(user_input):
    valid_choices = ['rock', 'paper', 'scissors']
    if user_input.lower() in valid_choices:
        return True
    return False

def display_result(user_choice, computer_choice, winner):
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == 'user':
        print("You win!")
    elif winner == 'computer':
        print("Computer wins!")
    else:
        print("It's a tie!")