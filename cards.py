import random


CARD_VALUES = {"A": "ace",
               "1": "1",
               "2": "2",
               "3" : "3",
               "4" : "4",
               "5" : "5",
               "6" : "6",
               "7" : "7",
               "8": "8",
               "9": "9",
               "10": "10",
               "J": "jack",
               "Q": "queen",
               "K": "king"}

CARD_SUITS = {"C": "clubs",
              "S": "spades",
              "H": "hearts",
              "D": "diamonds"}



class Card:
    def __init__(self, value: str, suit: str):
        self.value = value
        self.colour = None
        self.suit = suit

    def __str__(self):
        return f"{CARD_VALUES[self.value].capitalize()} of {CARD_SUITS[self.suit].capitalize()}"

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, obj: str):
        if obj.upper() in CARD_VALUES.keys():
            self._value = obj

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, obj: str):
        if obj.upper() in CARD_SUITS.keys():
            self._suit = obj.upper()
            if "S" == self.suit == "C":
                self.colour = "B"
            else:
                self.colour = "R"
        else:
            raise TypeError(f"{obj} isn't a suit")


class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, obj: str):
        if isinstance(obj, str):
            self._name = obj

    @property
    def hand(self):
        return self._hand
    @hand.setter
    def hand(self, obj: list[Card]):
        if isinstance(obj, list[Card]):
            for card in obj:
                if not (obj.value in CARD_VALUES) and not (obj.suit in CARD_SUITS):
                    raise TypeError("{obj} has incorrect values in it")
            self._hand = obj
        else:
            raise TypeError("{obj} is not a list")



class Deck:
    def __init__(self, sf: int = 1):
        self._cards = []
        for _ in range(sf):
            for suit in CARD_SUITS.keys():
                for value in CARD_VALUES.keys():
                    self._cards.append(Card(value, suit))
        random.shuffle(self._cards)

    def shuffle(self):
        random.shuffle(self._cards)

    @property
    def cards(self):
        return self._cards


    def pick_up_cards(self, cards: int = 1):
        return_cards = []
        for _ in range(cards):
            return_cards.append(self.cards[-1])
            self._cards.pop(-1)
        return return_cards
