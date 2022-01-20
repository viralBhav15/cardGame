import random       #importing the needed imports 

class Card(object):         #Creating the card object class
    def __init__(self, val):#initializing the class
        self.value = val

    def show(self):         #Returning the value of the card back to the terminal
        return (self.value)

class Deck(object):         #Creating the deck class which is the most important class
    def __init__(self):     #initializing the class
        self.cards = []
        self.build()

    def build(self):        #building the card and sending it to the card class
        for v in range(1, 11):
            self.cards.append(Card(v))
                
    def show(self):         #showing the card when called
        for c in self.cards:
            print(c.show())

    def shuffle(self):      #Being able to shuffle the deck of cards
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i] #creating the random shuffle formula

    def drawCard(self):     #Being able to draw the cards from the deck
        return self.cards.pop()

class Player(object):       #Creating the player class which will be used by both the player and the dealer
    def __init__(self):     #initializing the class
        self.hand = []

    def draw(self, deck):      #Being able to draw from the deck class
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):        #When called upon, it will show what cards the player and dealer are holding
        for card in self.hand:
            print (card.show())

    def sumOfHand(self):       #Adding the cards and finding the sum then returning the value into the terminal
        sum = 0
        for card in self.hand:
            #print(card.show())
            sum += card.show() 
        return sum
    
print("Welcome to BlackJack!")  #Title sentence
print()

running = True    #Creating the main loop for the game to run
while running:    #While loop to make it run
 
    #shuffling the deck
    deck = Deck()   #Creating the Deck class
    deck.shuffle()  #Shuffling the deck
    
    #getting the dealer's cards
    dealer = Player()      #Creating the dealer using the player class
    dealer.draw(deck).draw(deck)  #Drawing 2 cards from the deck
    print("The dealer has recieved their cards: ")
    #dealer.showHand()                  
    print()  #Adding extra space to make it look neat

    #getting the player's cards
    player = Player()       #Creating the player using the player class
    player.draw(deck).draw(deck)  #Drawing 2 cards from the deck
    print("You have been given these cards: ")
    player.showHand()  #Showing the player their hand
    running = False  #Ending the while loop

    sumOfDealer = dealer.sumOfHand()  #initalizing the dealer variable to keep track of the Dealer sum
    sumOfPlayer = player.sumOfHand()  #initalizing the player variable to keep track of the player sum

    if sumOfDealer <= 17:   #If the sum of dealer is less than 17, then it has to get a random card
        newRan = random.randint(1, 11)
        sumOfDealer += newRan
        #print (newRan)
        #print (sumOfDealer)

    #Creating all the If statements to see who is the winner
    if sumOfDealer == 21:     #Checking if the dealer wins
        print("Dealer has gotten 21. Dealer Wins!")
        break
    elif sumOfDealer > 21:    #Checking if the dealer has busted
        print ("The dealer now has the following cards: ")
        dealer.showHand()  #Showing which cards the dealer has 
        print (newRan)
        print("The dealer has busted! You win!")
        break

    while sumOfPlayer < 21:  #Letting the player choose if they want to "hit" or "stay"
        userInput = str(input("Do you want to hit or stay? (hit, stay) ").lower())  #Creating the userInput
        if userInput == "hit":  #When the player chooses "Hit"
            print("You now have the following cards: ")
            player.showHand()       #Showing the player's hand
            playerRan = random.randint(1, 11)
            sumOfPlayer += playerRan
            print (playerRan)
            if sumOfPlayer > 21:  #Checking if player sum goes over 21
                print ("Your total was " + str(sumOfPlayer) + ".")
                print("You busted. The dealer wins.")
                break
            elif sumOfPlayer == 21:  #Checking if the player has gotten blackjack
                print ("That's BLACKJACK!!! You win!")
                break
        
        elif sumOfPlayer == sumOfDealer:  #Checking if there has been a tie
            print("The dealer had a total of " + str(sumOfDealer) + ".")
            print("You had a total of " + str(sumOfPlayer) + ".")
            print("It's a Tie! No one wins!")
            break

        else:  #When the player does not choose "Hit"
            print ("The dealer has a total of " + str(sumOfDealer) + ".")  #Showing the total sum of the dealer
            print ("You have a total of "+ str(sumOfPlayer) + ".")         #Showing the total sum of the player
            if sumOfDealer > sumOfPlayer:   #Checking if the dealer wins
                print ("Dealer wins. Nice try.")
                break
            else:
                print ("You win!!! Good job!")  #When the player wins
                break

print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
'''playAgain = input("Would you like to play again? (y,n) ").lower()
if playAgain == "y":
    running = True
else:'''
print ("Thank you for playing!")

 

    





