# Blackjack Project
import random

cards = ["HA", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "HJ", "HQ", "HK", "SA", "S2", "S3", "S4", "S5",
         "S6", "S7", "S8", "S9", "S10", "SJ", "SQ", "SK", "CA", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10",
         "CJ", "CQ", "CK", "DA", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "DJ", "DQ", "DK"]

cards_value = {"HA": 11, "H2": 2, "H3": 3, "H4": 4, "H5": 5, "H6": 6, "H7": 7, "H8": 8, "H9": 9, "H10": 10, "HJ": 10,
               "HQ": 10, "HK": 10, "SA": 11, "S2": 2, "S3": 3, "S4": 4, "S5": 5, "S6": 6, "S7": 7, "S8": 8, "S9": 9,
               "S10": 10, "SJ": 10, "SQ": 10, "SK": 10, "CA": 11, "C2": 2, "C3": 3, "C4": 4, "C5": 5, "C6": 6, "C7": 7,
               "C8": 8, "C9": 9, "C10": 10, "CJ": 10, "CQ": 10, "CK": 10, "DA": 11, "D2": 2, "D3": 3, "D4": 4, "D5": 5,
               "D6": 6, "D7": 7, "D8": 8, "D9": 9, "D10": 10, "DJ": 10, "DQ": 10, "DK": 10}


def card_deal():
    choice = cards.pop(random.randrange(len(cards)))
    return choice


def compute_total(card1, card2):
    temp = int(cards_value[card1]) + int(cards_value[card2])
    if temp > 21:
        if card1 == "HA" or card1 == "DA" or card1 == "CA" or card1 == "SA":
            temp -= 10
            return temp
        elif card2 == "HA" or card2 == "DA" or card2 == "CA" or card2 == "SA":
            temp -= 10
            return temp
        else:
            return temp
    else:
        return temp


def a_compute_total(card3, pre_value):
    temp1 = int(cards_value[card3]) + pre_value
    if temp1 > 21:
        if card3 == "HA" or card3 == "DA" or card3 == "CA" or card3 == "SA":
            temp1 -= 10
            return temp1
        else:
            return temp1
    else:
        return temp1


def compute_card():
    user_card1 = card_deal()
    user_card2 = card_deal()
    cpu_card1 = card_deal()
    cpu_card2 = card_deal()
    print(f"User cards: {user_card1} , {user_card2}")
    print(f"Dealer Cards: __ , {cpu_card2}")
    user_value = compute_total(user_card1, user_card2)
    cpu_value = compute_total(cpu_card1, cpu_card2)
    print(f"User Points: {user_value}")
    flag_max = True

    while flag_max:
        if user_value == 21 and cpu_value == 21:
            print(f"Dealer points {cpu_value} and User points {user_value}")
            print("Draw")
            flag_max = False
        elif cpu_value == 21:
            print(f"Dealer points {cpu_value} and User points {user_value}")
            print("Dealer BlackJack")
            flag_max = False
        elif user_value == 21:
            print(f"Dealer points {cpu_value} and User points {user_value}")
            print("User won  Blacjack")
            flag_max = False
        else:
            choice = input("choose 'Hit' for newcard or 'Stand' to close the deal : ").lower()
            if choice == "hit":
                u_card3 = card_deal()
                print(f"New User card: {u_card3}")
                user_value = a_compute_total(u_card3, user_value)
                print(f"Total user points: {user_value}")
                if user_value > 21:
                    print(f"Dealer points {cpu_value} and User points {user_value}")
                    print("Game over for User,hit added value")
                    flag_max = False
                else:
                    flag_max = True
            elif choice == "stand":
                compare(user_value, cpu_value)
                flag_max = False


def compare(u_value, c_value):
    flag_bit = True
    while flag_bit:
        if c_value < 17 and c_value < u_value:
            d_card3 = card_deal()
            c_value = a_compute_total(d_card3, c_value)
            if c_value < 17:
                flag_bit = True
            else:
                flag_bit = False
        else:
            flag_bit = False

    if c_value == 21 and u_value != 21:
        print(f"Dealer points {c_value} and User points {u_value}")
        print("Dealer BlackJack")
    elif c_value < 21 and u_value == 21:
        print(f"Dealer points {c_value} and User points {u_value}")
        print("User BlackJack")
    elif c_value < 22 and u_value < 22:
        if c_value > u_value:
            print(f"Dealer points {c_value} and User points {u_value}")
            print("Dealer Won")
        elif c_value < u_value:
            print(f"Dealer points {c_value} and User points {u_value}")
            print("User won the game")
        elif c_value == u_value:
            print(f"Dealer points {c_value} and User points {u_value}")
            print("March draw")
        elif c_value > 22:
            print(f"Dealer points {c_value} and User points {u_value}")
            print("Dealer lost")
        elif u_value > 22:
            print(f"Dealer points {c_value} and User points {u_value}")
            print("User Lost the Game")
    else:
        print(f"Dealer points {c_value} and User points {u_value}")
        print("Dealer Lost the Game")


deal = True
while deal:
    shuffle_card = input("Do you want to shuffle the cards? 'yes' or 'no': ").lower()
    if shuffle_card == "yes":
        random.shuffle(cards)
        deal = True
    elif shuffle_card == "no":
        compute_card()
        deal = False


