from art import logo
import random
import os
import platform

def deal_cards():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You + the computer went over. You lose 😤"
    
    if user_score == computer_score:
        return "It's a draw 🙃"
    elif computer_score == 0:
        return "You lose. The computer has Blackjack 😱"
    elif user_score == 0:
        return "You win with Blackjack 😎"
    elif user_score > 21:
        return "You lose 😭"
    elif computer_score > 21 and user_score <= 21:
        return "You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"
    
