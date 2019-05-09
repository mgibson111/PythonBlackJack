# 07-03-2018
import random

# initially, index 0-3 of the deck will be used for the first draw
hit_counter = 3

# Creates the shuffled deck by calling getDeck()
# then deals just two cards for the player and
# the dealer in the game of Black Jack


def main():
    gameDeck = getDeck()
    # integer position in array of first card
    playerfirstcard = gameDeck[0]
    # integer position in array of second card
    playersecondcard = gameDeck[1]
    # Similarly for dealer...
    dealerfirstcard = gameDeck[2]
    dealersecondcard = gameDeck[3]

    # initializing player and dealer hands
    playerHandValue = cardFaceVal(playerfirstcard) + cardFaceVal(playersecondcard)
    dealerHandValue = cardFaceVal(dealerfirstcard) + cardFaceVal(dealersecondcard)


    print("The player's cards are: \n" + cardName(playerfirstcard) + "\n" +
          cardName(playersecondcard))
    print("\nPlayer's hand value: " + str(playerHandValue) + "\n")
    # prompts user to hit and saves value state
    playerHandValue = hit(gameDeck, playerHandValue, hit_counter)

    print("The hit counter after the player's turn is " + str(hit_counter - 3))

    print("The dealer's cards are: \n" + cardName(dealerfirstcard) + "\n" +
          cardName(dealersecondcard))
    print("\nDealer's hand value: " + str(dealerHandValue))
    dealerHandValue = dealer_hit(gameDeck, playerHandValue, dealerHandValue, hit_counter)

    if playerHandValue > dealerHandValue:
        print("Player Wins!")
    else:
        print("Dealer Wins!")

    play_again()


def play_again():
    answer = input("Would you like to play again?")

    if answer == "yes" or answer == "y":
        main()
    else:
        exit()


def under21(handValue):

    if handValue > 21:
        print("Sorry, you lose. You went over 21")
        return False
    else:
        return True


# Dealer automatically hits unless dealer's points are equal to higher than the player's
def dealer_hit(getDeck,playerPoints, dealerPoints, counter):
    global hit_counter
    hit_counter = counter
    if dealerPoints < playerPoints:
        print("Dealer will hit")
        nextCard = getDeck[hit_counter + 1]
        print("After the hit, the dealer drew a " + cardName(nextCard))
        currentScore = dealerPoints + cardFaceVal(nextCard)
        hit_counter += 1

        if currentScore < playerPoints:
            print("Current dealer score is " + str(currentScore) + " dealer will hit again \n")
            return dealer_hit(getDeck, playerPoints, currentScore, hit_counter)
        elif under21(currentScore) == False:
            print("Dealer busts. Player wins!")
            play_again()
        else:
            return currentScore
    else:
        return dealerPoints


# Allows the player to 'hit' or draw another card
def hit(getDeck, points, counter):
    global hit_counter
    hit_counter = counter
    answer = input("Would you like to hit?")

    if answer == "yes" or answer == "y":
        nextCard = getDeck[hit_counter + 1]
        print("After the hit, the player drew a " + cardName(nextCard))
        currentScore = points + cardFaceVal(nextCard)
        hit_counter += 1

        if under21(currentScore):
            print("Current points is " + str(currentScore))
            return hit(getDeck, currentScore, hit_counter)
        else:
            print("The player busted. Dealer wins!")
            play_again()
    else:
        print("Ok, your current points remain at " + str(points))
        return points


# Returns a shuffled list of 52 integers from 0 to 51
def getDeck() -> object:
    ls = []
    ls.extend(range(52))
    random.shuffle(ls)
    return ls


# Returns a string of the suit and face of a given card
def cardName(num):
    suits = ("Hearts", "Diamonds", "Clubs", "Spades")
    faces = ("Ace", "Deuce", "Three", "Four", "Five", "Six", \
             "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", \
             "King")
    suitNum = num // 13
    faceNum = num % 13
    return faces[faceNum] + " of " + suits[suitNum]


# Returns the face value of a given card (with aces = 1)
def cardFaceVal(num):
    faceIndex = num % 13
    if faceIndex >= 10:
        return 10
    else:
        return faceIndex + 1


if __name__ == "__main__":
    main()
