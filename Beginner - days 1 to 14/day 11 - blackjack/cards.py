import time
import art

suits = {
    "Hearts": "♥",
    "Diamonds": "♦",
    "Spades": "♠",
    "Clubs": "♣"
}
ranks = {
    "Ace": {
        "symbol": "A",
        "value": 11,
        "number": 1
    },
    "Two": {
        "symbol": "2", 
        "value": 2,
        "number": 2
    },
    "Three": {
        "symbol": "3",
        "value": 3,
        "number": 3
    },
    "Four": {
        "symbol": "4",
        "value": 4,
        "number": 4
    },
    "Five": {
        "symbol": "5",
        "value": 5,
        "number": 5
    },
    "Six": {
        "symbol": "6",
        "value": 6,
        "number": 6
    },
    "Seven": {
        "symbol": "7",
        "value": 7,
        "number": 7
    },
    "Eight": {
        "symbol": "8",
        "value": 8,
        "number": 8
    },
    "Nine": {
        "symbol": "9",
        "value": 9,
        "number": 9
    },
    "Ten": {
        "symbol": "10",
        "value": 10,
        "number": 10
    },
    "Jack": {
        "symbol": "J",
        "value": 10,
        "number": 11
    },
    "Queen": {
        "symbol": "Q",
        "value": 10,
        "number": 12
    },
    "King": {
        "symbol": "K",
        "value": 10,
        "number": 13
    }
}


class Card:
  
    def __init__(self, rank, suit) -> None:
        self.suit = suit
        self.suit_symbol = suits[self.suit]
        self.rank = rank
        self.number = ranks[self.rank]["number"]
        self.value = ranks[self.rank]["value"]
        self.rank_symbol = ranks[self.rank]["symbol"]
        self.card_front = self.__create_card_art()
        self.card_back = art.cards["back"]
        
    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"
    
    def __create_card_art(self):
        card_art = art.cards[self.rank_symbol]
        card_art = [line.replace("#", self.suit_symbol) for line in card_art]
        return card_art
      
    def __repr__(self) -> str:
        output = f"{self.rank} of {self.suit}: Value: {self.value}, Number: {self.number}, Rank Symbol: {self.rank_symbol}, Suit: {self.suit_symbol}{self.suit}"
        return output
    
    def print_card(self):
        for i,line in enumerate(self.card_front):
            print(f"{line}\t{self.card_back[i]}")

if __name__ == "__main__":
    card = Card("Queen", "Hearts")
    for i,line in enumerate(card.card_front):
        print(f"{line}\t{card.card_back[i]}")
        time.sleep(0.01)
    print(card)
    print(card.value)
    print(card.number)
    print(card.rank_symbol)
    print(card.suit_symbol)
    print(card.suit)
    print(card.rank)
    print(repr(card))
    
    