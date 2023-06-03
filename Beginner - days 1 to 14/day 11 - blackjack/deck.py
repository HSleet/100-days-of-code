import cards
import random

class Deck:
    
    def __init__(self) -> None:
        self.cards = []
        self.__create_deck()
    
    def __create_deck(self):
        for suit in cards.suits:
            for rank in cards.ranks:
                self.cards.append(cards.Card(rank, suit))
    
    def shuffle_deck(self):
        random.shuffle(self.cards)


if __name__ == "__main__":
    new_deck = Deck()
    print("New deck:")
    for card in new_deck.cards:
        print(repr(card))
    new_deck.shuffle_deck()
    print("\nShuffled deck:")
    for card in new_deck.cards:
        print(repr(card))
