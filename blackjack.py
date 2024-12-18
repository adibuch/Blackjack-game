import random
from logo import logo


def take_card():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif u_score == 0:
        return "You win!"
    elif c_score == 0:
        return "You lose:("
    elif u_score > 21:
        return "You lose:("
    elif c_score > 21:
        return "You win!"
    elif u_score > c_score:
        return "You win!"
    else:
        return "You lose:("


def play_game():
    print(logo)
    your_card = []
    computer_card = []
    computer_score = -1
    your_score = -1
    game_is_over = False

    for _ in range(2):
        your_card.append(take_card())
        computer_card.append(take_card())

    while not game_is_over:

        your_score = calculate_score(your_card)
        computer_score = calculate_score(computer_card)
        print(f"Your card: {your_card},current score: {your_score}")
        print(f"Computer first card: {computer_card[0]}")
        if your_score == 0 or computer_score == 0 or your_score > 21:
            game_is_over = True
        else:
            choice = input("Do you want to take another card? enter 'y' to yes and 'n' to no.")
            if choice == 'y':
                your_card.append(take_card())
            else:
                game_is_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(take_card())
        computer_score = calculate_score(computer_card)
    print(f"Your card:{your_card},Your score: {your_score}")
    print(f"Computer cards: {computer_card}, Computer score: {computer_score}")
    print(compare(your_score, computer_score))


while input("Do you want play Blackjack? Enter 'y' and 'n' to no.") == 'y':
    print('\n' * 20)
    play_game()
