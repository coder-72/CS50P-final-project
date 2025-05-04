from cards import Deck

class BlackjackDeck(Deck):
    def __init__(self):
        super().__init__()
        self.suits.update({"H" : self.Suit("Hearts", "H", "r", chr(9829),2)})
        self.suits.update({"D": self.Suit("Diamonds", "D", "r", chr(9830), 4)})
        self.suits.update({"C": self.Suit("Clubs", "C", "b", chr(9827),6)})
        self.suits.update({"S": self.Suit("Spades", "S", "b", chr(9824), 8)})

        self.values.update({"A" : self.Value("A", "Ace", [1, 11])})
        self.values.update({"2": self.Value("2", "Two", [2])})
        self.values.update({"3": self.Value("3", "Three", [3])})
        self.values.update({"4": self.Value("4", "Four", [4])})
        self.values.update({"5": self.Value("5", "Five", [5])})
        self.values.update({"6": self.Value("6", "Six", [6])})
        self.values.update({"7": self.Value("7", "Seven", [7])})
        self.values.update({"8": self.Value("8", "Eight", [8])})
        self.values.update({"9": self.Value("9", "Nine", [9])})
        self.values.update({"10": self.Value("10", "Ten", [10])})
        self.values.update({"J": self.Value("J", "Jack", [10])})
        self.values.update({"Q": self.Value("K", "Queen", [10])})
        self.values.update({"K": self.Value("Q", "King", [10])})
        #self.values.update({"#": self.Value("#", "Joker", [10])})

        for deck in range(self.decks):
            for suit in self.suits.values():
                for value in self.values.values():
                    self.cards.append(self.Card(value, suit))


class GenericDeck(Deck):
    def __init__(self):
        super().__init__()
        self.suits.update({"H" : self.Suit("Hearts", "H", "r", chr(9829),2)})
        self.suits.update({"D": self.Suit("Diamonds", "D", "r", chr(9830), 4)})
        self.suits.update({"C": self.Suit("Clubs", "C", "b", chr(9827),6)})
        self.suits.update({"S": self.Suit("Spades", "S", "b", chr(9824), 8)})

        self.values.update({"A" : self.Value("A", "Ace", [1, 14])})
        self.values.update({"2": self.Value("2", "Two", [2])})
        self.values.update({"3": self.Value("3", "Three", [3])})
        self.values.update({"4": self.Value("4", "Four", [4])})
        self.values.update({"5": self.Value("5", "Five", [5])})
        self.values.update({"6": self.Value("6", "Six", [6])})
        self.values.update({"7": self.Value("7", "Seven", [7])})
        self.values.update({"8": self.Value("8", "Eight", [8])})
        self.values.update({"9": self.Value("9", "Nine", [9])})
        self.values.update({"10": self.Value("10", "Ten", [10])})
        self.values.update({"J": self.Value("J", "Jack", [11])})
        self.values.update({"Q": self.Value("K", "Queen", [12])})
        self.values.update({"K": self.Value("Q", "King", [13])})
        self.values.update({"#": self.Value("#", "Joker", [num for num in range(15)])})

        for deck in range(self.decks):
            for suit in self.suits.values():
                for value in self.values.values():
                    self.cards.append(self.Card(value, suit))
