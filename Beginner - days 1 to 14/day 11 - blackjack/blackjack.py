import os
import deck
import art

class Player:
    
    def __init__(self) -> None:
        self.hand = []
        self.score = 0
        self.aces = 0
    
    def get_card(self, card):
        self.hand.append(card)
        self.score += card.value
        if card.rank == "Ace":
            self.aces += 1
        if self.score > 21 and self.aces > 0:
            self.score -= 10
            self.aces -= 1
    
class Dealer(Player):
    
    def __init__(self) -> None:
        super().__init__()
        self.is_hidden = False
        self.visible_score = 0
        self.deck = deck.Deck()
        self.deck.shuffle_deck()
    
    def deal_hand(self, player):
        player.get_card(self.deck.cards.pop())
        player.get_card(self.deck.cards.pop())
    
    def deal_card(self, player):
        player.get_card(self.deck.cards.pop())
        


def clear_screen():
    os.system("cls")
    print(art.logo)


def show_cards(dealer, player, flip_card:bool = False):
    space = "\t               \t"*(len(dealer.hand))
    print(f"Dealer's hand:{space}Your hand:")
    rows = []
    if flip_card:
        dealer.is_hidden = not dealer.is_hidden
        dealer.hand[1].card_front, dealer.hand[1].card_back = dealer.hand[1].card_back, dealer.hand[1].card_front
    player_rows = []
    for i, line in enumerate(player.hand[0].card_front):
        row = ""
        for card in player.hand:
            row += f"{card.card_front[i]}\t"
        player_rows.append(row)
    dealer_rows = []
    for i, line in enumerate(dealer.hand[0].card_front):
        row = ""
        for card in dealer.hand:
            row += f"{card.card_front[i]}\t"
        dealer_rows.append(row)
    
    for i, line in enumerate(dealer_rows):
        rows.append(f"{line}|\t{player_rows[i]}")
    for row in rows:
        print(row)
    if dealer.is_hidden:
        print(f"Dealer's score: {dealer.hand[0].value}{space}Your score: {player.score}")
    else:
        print(f"Dealer's score: {dealer.score}{space}Your score: {player.score}")
        

def is_blackjack(player):
    if player.score == 21:
        return True
    else:
        return False


def play_again():
    play_again = input("Do you want to play again? Type 'y' or 'n': ").lower()
    if play_again == "y":
        play_blackjack()
    else:
        exit()


def check_game_status(dealer, player):
    if player.score > 21:
        print("Bust! You lose!")
    elif player.score == 21:
        print("Blackjack! You win!")
    elif not dealer.is_hidden:
        if dealer.score > 21:
            print("Dealer bust! You win!")
        elif dealer.score == 21:
            print("Dealer blackjack! You lose!")
        else:
            return
    else:
        return
    play_again()


def play_blackjack():
    dealer = Dealer()
    player = Player()
    dealer.deal_hand(player)
    dealer.deal_hand(dealer)
    clear_screen()
    show_cards(dealer, player, True)
    check_game_status(dealer, player)    
    hit = input("Do you want to hit? Type 'y' or 'n': ")    
    while hit == "y":
        clear_screen()
        dealer.deal_card(player)
        show_cards(dealer, player, False)
        check_game_status(dealer, player)
        hit = input("Do you want to hit again? Type 'y' or 'n': ")
    
    input("Press enter to let the dealer play.")
    clear_screen()
    show_cards(dealer, player, True)
    
    input("dealer's turn. Press enter to continue.")
    while dealer.score < 17:
        clear_screen()
        dealer.deal_card(dealer)
        show_cards(dealer, player, False)
        check_game_status(dealer, player)
    if dealer.score > player.score:
        print("Dealer wins!")
    elif dealer.score < player.score:
        print("You win!")
    else:
        print("It's a tie!")
    play_again()
            

if __name__ == "__main__":
    os.system("cls")
    print(art.logo)
    input("Press enter to play blackjack.")
    play_blackjack()