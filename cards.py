from __future__ import annotations
import random
from typing import Callable

"""
:Date: 2025-05-04
:Version: 1
:Authors:
    - coder-72
    """

def sort_key(item : Deck.Card) -> int:
    return item.value.num_vals[0] * 10 + item.suit.priority


class Deck:
    def __init__(self, decks : int = 1) -> None:
        """
        initiates deck

        :param decks: how many repeats of each card (e.g. 2 means 2 of each card)
        :type decks: int, optional
        """
        self.decks = decks
        self.cards = []
        self.suits = {}
        self.values = {}
    def shuffle(self) -> None:
        """
        shuffles deck of cards

        :return: None
        """
        #shuffle cards using random module
        random.shuffle(self.cards)

    def random_cards(self, num : int = 1) -> list:
        """

        :param num: number of cards to pick
        :return: list of cards
        :rtype: list[Deck.Card]
        """
        cards = []
        for i in range(0, num):
            pos = random.randrange(0, len(self.cards))
            cards.append(self.cards[pos])
            self.cards.pop(pos)
        return cards

    def sort(self, key : Callable[[Card], int] = sort_key) -> None:
        """

        :param key: function to assign value to each card in order to sort
        :return: None
        """
        self.cards.sort(key=key)



    class Suit:

        def __init__(self, name: str, symbol: str, colour: str, asciistr : str, priority : int = 0) -> None:
            """
            initiate and create a new suit

            :param name: name of suit
            :type name: str
            :param symbol: symbol to display suit
            :type symbol: str
            :param colour: colour of suit
            :type colour: str
            :param asciistr: symbol in ascii for suit
            :type asciistr: str
            :param priority: priority of suit when using sort function
            :type priority: int, optional
            """

            self.name = name
            self.symbol = symbol
            self.colour = colour
            self.priority = priority
            self.ascii = asciistr

        def __str__(self) -> str:
            """
            called when suit is printed etc.

            :return: suit information
            """
            return str(f"colour: {self.colour}, name: {self.name}")

        @property
        def colour(self) -> str:
            """
            returns self._colour instead of self.colour when accessing it

            :return: the suit colour
            """
            return self._colour

        @colour.setter
        def colour(self, obj) -> None:
            """
            makes sure value assigning to self.colour is valid and assigns it to private variable self._colour

            :param obj: obj you are assigning colour to
            :raise TypeError: when obj is an invalid colour (not red or black)
            """
            # TODO: change this to something more generic
            if isinstance(obj, str) and obj.replace(" ", "").lower() in ["black", "b"]:
                self._colour = "b"
            elif isinstance(obj, str) and obj.replace(" ", "").lower() in ["red", "r"]:
                self._colour = "r"
            else:
                raise TypeError(f"{obj} is an invalid colour")

    class Value:

        def __init__(self, symbol: str, name: str, num_vals: list) -> None:
            """
            instanciate a value

            :param symbol: visual symbol of card
            :param num_vals: list of numerical value cards can hold
            """
            self.symbol = symbol
            self.name = name
            self.num_vals = num_vals

        def __str__(self) -> str:
            return self.symbol


    class Card:
        def __init__(self, value: Deck.Value, suit: Deck.Suit):
            """
            Instanciate a new card

            :param value: value of card (e.g. queen)
            :type value: Value
            :param suit: suit of card (e.g. spades)
            :type suit: Suit
            :param ascii: ascii representation of card
            :type ascii: str, optional
            """
            self.value = value
            self.suit = suit

        def get_ascii(self):
            """
            creates ascii art for card object

            :return: ascii art form of card
            :rtype: str
            """
            ascii = """
 ____ 
|{2:<2}  |
| {1:<2} |
|__{0:<2}|
""".format("_" + self.value.symbol  if len(self.value.symbol) < 2 else self.value.symbol, self.suit.ascii, self.value.symbol)
            return ascii

        def __str__(self) -> str:
            """

            :return: string for obj e.g. when printing so human readable
            :rtype: str
            """
            return self.get_ascii()

        @property
        def value(self) -> Deck.Value:
            """
            when trying to access value attribute returns private value attribute instead

            :return: value object of card
            :rtype: Deck.Value
            """
            return self._value

        @property
        def suit(self) -> Deck.Suit:
            """
            when accessing suit attribute returns private attribute suit attribute instead

            :return: suit object for card
            :rtype: Deck.Suit
            """
            return self._suit

        @value.setter
        def value(self, obj) -> None:
            """
            checks obj is of type Deck.Value

            :param obj: object assigning value to
            :return: None
            """
            if isinstance(obj, Deck.Value):
                self._value = obj
            else:
                message = f"{obj} is not of type Value"
                raise TypeError(message)

        @suit.setter
        def suit(self, obj) -> None:
            """
            checks obj is of type Deck.Suit

            :param obj: object setting suit to
            :return:
            """
            if isinstance(obj, Deck.Suit):
                self._suit = obj
            else:
                message = f"{obj} is not of type Suit"
                raise TypeError(message)

