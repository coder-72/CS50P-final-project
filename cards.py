from __future__ import annotations

"""
:Date: 2025-05-04
:Version: 1
:Authors:
    - coder-72
    """




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



    class Suit:

        def __init__(self, name: str, symbol: str, colour: str) -> None:
            """
            initiate and create a new suit

            :param name: name of suit
            :param symbol: symbol to display suit
            :param colour: colour of suit
            """

            self.name = name
            self.symbol = symbol
            self.colour = colour

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
        def __init__(self, value: Deck.Value, suit: Deck.Suit, ascii: str = ""):
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
            self.ascii = ascii

        def __str__(self):
            return self.ascii

        @property
        def value(self) -> Deck.Value:
            return self._value

        @property
        def suit(self) -> Deck.Suit:
            return self._suit

        @value.setter
        def value(self, obj) -> None:
            if isinstance(obj, Deck.Value):
                self._value = obj
            else:
                message = f"{obj} is not of type Value"
                raise TypeError(message)

        @suit.setter
        def suit(self, obj) -> None:
            if isinstance(obj, Deck.Suit):
                self._suit = obj
            else:
                message = f"{obj} is not of type Suit"
                raise TypeError(message)




Deck()