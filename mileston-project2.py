import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True


class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        pass

    def __str__(self):
       return self.rank + ' of ' + self.suit


class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        is_deck = ' '
        for card in self.deck:
            is_deck += '\n'+ card.__str__()
        return 'the deck has:'+is_deck



    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == "Ace":
            self.aces += 1
    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

class Chips:

    def __init__(self,total=100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(player_hand):

    while True:

        try:
            player_hand.bet = int(input("please how many chips do you want to bet? :  "))
        except:
            print("Sorry this is not int!!")
        else:
            if player_hand.bet > player_hand.total:
                print("Sorry you don't have enough chips, you have {}".format(player_hand.total))
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop

    while True:
        x = input("Hit or Stand ? enter h or s. ")

        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print('Player stand, dealer turn')
            playing = False
        else:
            print('sorry , you should choose h or s ')
            continue
        break
    pass


def show_some(player, dealer):
    print("\n Dealers hand: ")
    print("First card is hidden.")
    print(dealer.cards[1])

    print("\n player's hand: ")
    for card in player.cards:
        print(card)

def show_all(player, dealer):


    print("\n dealer hands: ")
    for card in dealer.cards:
        print(card)
    # value of the dealer hand
    print(f'value of Dealer hand {dealer.value}')

    print("\n player's hand: ")
    for card in player.cards:
        print(card)
    print(f'value of Dealer hand {player.value}')


def player_busts(player , dealer ,chips):
    print("BUST PLAYER!")
    chips.lose_bet()



def player_wins(player , dealer ,chips):
    print("PLAYER WINS")
    chips.win_bet()


def dealer_busts(player , dealer ,chips):
    print("Player Win ,Dealer BUSTED")
    chips.win_bet()
    pass


def dealer_wins(player , dealer ,chips):
    print('DEALER WINS')
    chips.lose_bet()


def push(player , dealer):
    print('Dealer and players tie!')


while True:
    # Print an opening statement
    print("Welcome to the big event of the year , now is bleck jack time!!!")
    # Create & shuffle the deck, deal two cards to each player
    new_deck = Deck()
    new_deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()
    for x in range(2):
        player_hand.add_card(new_deck.deal())
        dealer_hand.add_card(new_deck.deal())


    # Set up the Player's chips
    player_chips = Chips()
    # Prompt the Player for their bet
    take_bet(player_chips)
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(new_deck,player_hand)
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value> 21:
            player_busts(player_hand,dealer_hand,player_chips)

            break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player_hand.value <=  21:
            while dealer_hand.value < 17:
                hit_or_stand(new_deck,dealer_hand)

        # Show all cards
        show_all(player_hand,dealer_hand)
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)




        # Inform Player of their chips total
        print(f'\n player you have total chips : {player_chips.total}')

        # Ask to play again
        new_game = input("would you like to play another hand : enter y or n ")
        if new_game[0].lower() == 'y':
            playing = True
            continue
        else:
            print('Thank you , have a good day.')
            playing = False
            break

