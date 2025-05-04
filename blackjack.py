from cards import Deck
from rich.console import Console
from itertools import product


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
deck = BlackjackDeck()

class Player:
    players = []
    def __init__(self, name : str, hand : int = 2):
        self.hand = deck.random_cards(hand)
        self.out = False
        self.busted = False
        self.name = name
        Player.players.append(self)

    def take_go(self):
        input(f"Press any key to see {self.name}'s cards")
        self.display_hand()
        move = self.get_move()
        if move:
            new_card = deck.random_cards()
            self.hand.append(*new_card)
            print(*new_card)
            if self.bust():
                self.busted = True
                print("BUST")
        else:
            self.out = True


    def display_hand(self):
        lines = []
        display = ""
        for _ in range(len(str(self.hand[0]).splitlines())):
            lines.append("")

        for card in self.hand:
            for index, line in enumerate(str(card).splitlines()):
                lines[index] += "  " + line
        for line in lines:
            display += line + "\n"
        print(display)


    def get_move(self) -> bool:
        hit = ["hit", "h"]
        stand = ["stand", "s"]
        move = input("HIT OR STAND?").lower().strip()
        if move in hit:
            return True
        elif move in twist:
            return False
        else:
            print("Invalid.")
            return self.get_move()

    def bust(self):
        vals = []
        for card in self.hand:
            vals.append(card.value.num_vals)

        totals = [sum(combination) for combination in product(*vals)]
        for score in totals:
            if score <= 21:
                return False
        return True

    def best_score(self):
        vals = []
        for card in self.hand:
            vals.append(card.value.num_vals)

        totals = [sum(combination) for combination in product(*vals)]
        best = 0
        for t in totals:
            if t <= 21 and t >= best:
                best = t
        return best



Player("player 1")
Player("player 2")
turn_taken = True
while turn_taken == True:
    turn_taken = False
    for player in Player.players:
        if not player.out and not player.busted:
            turn_taken = True
            player.take_go()

for player in Player.players:
    if player.busted:
        print(f"{player.name} went bust")
        print("with cards:")
        player.display_hand()
    else:
        print(f"{player.name} scored {player.best_score()}")
        print("with cards:")
        player.display_hand()
