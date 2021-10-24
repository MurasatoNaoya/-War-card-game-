
from random import shuffle # This will be used later for our shuffle method. 

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14} 
suits = ('Hearts', 'Clubs', 'Spades', 'Diamonds')
kinds = ('Two','Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King','Ace')

# The global variables of 'suits' and 'kinds' are not needed for your Card class, but will be needed for when defining all of the cards within our deck; determined by our Deck class. 
# This class definies the cards that we will have in our deck - 
class Card(): # We are not inheriting any methods, so in theory the brackets are not needed, but you can use them if you want. 
    def __init__(self,kind,suit): # Each card will have 3 attributes, but only 2 need to definied when calling an instance of the class, due to our dictionary look-up. 
        self.kind = kind
        self.suit = suit
        self.value = values[kind] # The kind of card will correspond to a key-value pair in our dictionary. 
        # One key point about the dictionary lookup is that the 'kind' definied the instance has to be EXACT to the key; otherwise we will get a key error. 

    def __str__(self):
        return '{} of {}'.format(self.kind, self.suit)
        # This string method is just here for convinience, so that when try to print our instance, we don't just get a data location. 


two_of_hearts = Card('Two', 'Hearts')
print(Card('Four','Diamonds')) # This would produce a data location if you didn't define a __str__ method. 

print(two_of_hearts)
print(two_of_hearts.kind)
print(two_of_hearts.suit)

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14} 
# This is our values dictionry, global variables should always be at the top of your code, but I have also put one here, to remind and emphasise its usage. 
values[two_of_hearts.kind]

# The next class we have to define, is the Deck class. 
# Unlike what we have deal with before, each variable within the Deck class will in themselves be instances of the Card class we ahev defined before, each with their own particular attributes. 

# Alright, we want our Deck class to be able to create 52 cards, each with their own unique attributes, to have a shuffle function and to able to take cards that have been drawn out of the deck pool. 
# Just to reiterate, the key point is that the Deck class will be using our own Card object we have defined, instead of in-built objects like strings we have been working with before. 

class Deck():
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for kind in kinds:
                created_card = Card(kind,suit) # Make sure that the order of your inputs, matches up to the order you defined in your Card class. 
                self.all_cards.append(created_card) # You can stack attributes and .methods on top of each other, in this case they are .all_cards and .append. 
                

    

# Now we can check that the creation of our deck is correct. 
new_deck = Deck()

top_card = new_deck.all_cards[0]
print(top_card)

bottom_card = new_deck.all_cards[-1] # Using the -1 index is useful in cases that you don't know, or it is difficult to find out what the last index value is. 
print(bottom_card)

for card in new_deck.all_cards:
    print(card)

# Currently our all_cards decklist is prefectly ordered, corresponding to kind and suit. This will be unrealisitic in a real game, making the idea of a shuffle method a good idea.     

class Deck():
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for kind in kinds:
                created_card = Card(kind,suit) # Make sure that the order of your inputs, matches up to the order you defined in your Card class. 
                self.all_cards.append(created_card) # You can stack attributes and .methods on top of each other, in this case they are .all_cards and .append. 
    
    def shuffle_deck(self):
        shuffle(self.all_cards)
        
another_new_deck = Deck() # Now we are creating another instance of our Deck class, this time one we will shuffle. 
another_new_deck.shuffle_deck()
print(another_new_deck.all_cards[0]) # Note that the bottom two print statements will produce different outputs that the ordered ones above, proving our shuffle methods works. 
print(another_new_deck.all_cards[-1]) # It is important to understand that shuffle does not return anything, but changes the definition of your list. We would have to reassign a lot of things otherwise.  

# When you are actually playing the game however, there will be cards taken from the main deck, this has to be accounted for.    

class Deck():
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for kind in kinds:
                created_card = Card(kind,suit) 
                self.all_cards.append(created_card) 
    
    def shuffle_deck(self):
        shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop(0) # pop provdies the very last value from a list, removing it from the list. Bear in mind that it doesn't return the remaining list, just the one item that is popped off. 

# It is important to note that your shuffle method does not return anything, due to shuffle only acting in place and affecting your inputted variable. 
# Meaning even if you return and assigning it to something you will get a NoneType, as the only change that has occured was with the inputed variable. 

yet_another_new_deck = Deck()
yet_another_new_deck.shuffle_deck()
dealt_card = yet_another_new_deck.deal_one()
print(dealt_card)
print(len(yet_another_new_deck.all_cards)) # As you can see, after dealing one card, the length of the total card list goes down by one as expected. 

class Player():
        def __init__(self,name):
            self.name = name 
            self.hand = []
        
        def remove_one(self):
            return self.hand.pop(0)

        def add_cards(self,new_cards):
            if type(new_cards) == type([]): # ([]) can just be an easy way to demonstrate a list type. 
                self.hand.extend(new_cards) # It is very important to use .extend() as opposed to .append(), otherwise you would create a nested list, as opposed to just adding on some cards. 
            else:
                self.hand.append(new_cards) # In this case using .append() is fine, because you're not appending a list, but just a single item. There is no need to seperate a list of value into unquie singular items like .extend. 

        def __str__(self):
            return '{} currently has {} cards in hand'.format(self.name, len(self.hand))

    


new_player = Player('Andrew')
print(new_player)

# How we can use out add_cards method to give card(s) to the player! 

new_player.add_cards(dealt_card) # In this case, it'd be adding the top card of the shuffled deck to the player Andrew's hand. 
print(new_player)

# The above case was using the else append() variant of our add_cards variant where only one item is concerned, we can of course add multiple cards at once in the form of a list with the extend portion too. 
new_player.add_cards([dealt_card,dealt_card,dealt_card]) # In this case we are adding the next 3 cards on top of the deck, after the inital dealt card. 
print(new_player)

# We can also check if our remove method works too, remember that it takes the top card in the players hand only.   
new_player.remove_one()
print(new_player)



# Now we have to set out our game logic, normally you will be managing your logic first-hand, then creating the classes you think would be necessary for your game logic to work. 

player_one = Player('One')
player_two = Player('Two')

game_deck = Deck()
game_deck.shuffle_deck()

for _ in range(26):
    player_one.add_cards(game_deck.deal_one()) # This line adds a card to player 1's hand from our game deck, while also popping off the to account for the -1 in the deck. 
    player_two.add_cards(game_deck.deal_one()) # You have to make sure you call your class methods, otherwise you'll get data locations and not actualy string values. 


print(len(player_one.hand))
print(player_one.hand[0])

game_on = True 

round_num = 0 
while game_on: # You could say, while game_on == True, but this statement means the same thing. 
    round_num += 1 
    print(f'Round {round_num}')

    if len(player_one.hand) == 0:
        print('Player One is out of cards! Player Two wins!')
        game_on = False
        break 
    elif len(player_two.hand) == 0:
        print('Player Two has run out of cards! The game goes to Player Two!')
        game_on == False
        break 
    
    # Start of another round - 
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())


    # While at_war 

    at_war = True 

    while at_war:
        if  player_one_cards[-1].value > player_two_cards[-1].value:
            
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False

        elif  player_two_cards[-1].value > player_one_cards[-1].value:
            
            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)

            at_war = False     
        
        else: 
            print('You are at WAR!')
            if len(player_one.hand) < 5:
                print('Player One is unable to declare war.')
                print('Player Two wins the game.')
                game_on = False
                break
            
            elif len(player_two.hand) < 5:
                print('Player Two is unable to declare war.')
                print('Player One wins the game.')
                game_on = False
                break

            else: 
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())