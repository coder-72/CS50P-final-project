from cards import Player, Card, Deck

PLAYER_MAX=10
PLAYER_MIN=2

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
        name = input("Player {numbers}'s name: ")
        players.append(Player(name))
    return players

def setup_hands(players, deck, start_card_num: int = 2):
    for player in players:
        cards = deck.pick_up_cards(cards=start_card_num)
        for card in cards:
            player.hand.append(card)
    return players

def game(players):
    players_to_play = players
    while True:
        for

