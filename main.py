from cards import Player, Card, Deck

PLAYER_MAX=10
PLAYER_MIN=2
BLACK_JACK_CARD_VALUE = {
    "A" : [1, 11],
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10,
    "J" : 10,
    "Q" : 10,
    "K" : 10
}


def main():
    deck = Deck()
    players = get_players()
    players = setup_hands(players, deck, start_card_num=2)



def get_players() -> list[Player]:
    while True:
        try:
            player_num = int(input("Number of players: "))
            if PLAYER_MIN <= player_num <= PLAYER_MAX:
                break
        except TypeError as e:
            print(e)

    players = []
    for number in range(player_num):
        while True:
            name = input("Player {numbers}'s name: ")
            if not name in [player.name for player in players]:
                players.append(Player(name))
                break
            else:
                print("players can't have the same name")
    return players

def setup_hands(players, deck, start_card_num: int = 2):
    for player in players:
        cards = deck.pick_up_cards(cards=start_card_num)
        for card in cards:
            player.hand.append(card)
    return players

def game(players, deck):
    players_to_play = players
    while True:
        for place, player in enumerate(players_to_play):
            player, players_to_play = turn(player, players_to_play, deck, place)
            players[players.index(player)] = player



def turn(player, players_to_play, deck, place):
    while True:
        choice = input("Hit or stand (H/S): ")
        if choice.lower() == "h":
            player.hand.append(*deck.pick_up_cards())
            break
        elif choice.lower() == "s":
            players_to_play.pop(place)
            break

    bestscore = None
    currentscore = 0
    for index in [-1, 1]:
        for card in player.hand:
            currentscore += BLACK_JACK_CARD_VALUE[card.value][index]
        if bestscore == None or (bestscore != None and currentscore > bestscore and currentscore <=21):
            bestscore = currentscore

    if bestscore == None or bestscore > 21:
        print(f"{player.name} went BUST!!")
        players_to_play.pop(place)
    else:
        players_to_play[place] = player
    return player, players_to_play




