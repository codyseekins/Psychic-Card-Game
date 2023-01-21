import random
#Card class
class Card:

    #Card Attribute Initialization function
    def __init__(self):
        #types of card symbols
        card_list = ["Star", "Circle", "Square", "3 Wavy Lines", "Cross"]
        self.card_list_length = len(card_list)
        #is the card face up?
        self.is_face_up = False
        self.cards = card_list
        #random card selected from card symbol list
        self.random_card = random.choice(self.cards)
        #specific symbol of instance card
        self.symbol = self.random_card
    
    #Card Methods Below:

    #draws a card to instantiate a card object
    def draw_card(self):
        print("Card Drawn.  Can you guess it?")
        return self.random_card
    
    #returns the Card card_list 
    def card_list(self):
        return self.card_list_length
    
    #representation function describing instance of Card
    def __repr__(self):
        rep = "New Card Drawn. Card symbol is {}.".format(self.random_card)
        return rep
    
#Player Class
class Player:

    #Player Attributes for class instance
    def __init__(self,name):
        self.name = name
        self.list = []
        #will assign name
        self.user_input = ""
        #will determine choice to continue or quit
        self.try_again = ""
        #announces player instance:
        print("Player {} entered the room".format(self.name))
        #Has the player made a guess?
        self.made_a_guess = False
        #mystery card to be guessed:
        self.mystery_card = ""
        self.real_card = ""
        #number of correct answers:
        self.correct_answers = 0
        #number of wrong ansers:
        self.wrong_answers = 0
        #total guesses:
        self.total_guesses = 0
        #percent of correct guesses:
        self.percent_correct = 0
        self.statistical_average_correct = 0
        
        

    #Player Methods Below:

    #draws a card from Card class and stores it as a variable in Player instance
    def draw_card(self):
        #instance of Card class:
        self.real_card = Card()
        self.list = self.real_card.card_list_length
        #player instance draws mystery card from Card class and stores it as a value in Player class
        self.mystery_card = self.real_card.draw_card()
        return self.mystery_card, self.list
    
    #guessing a card function
    def guess_card(self):
        while True:
            self.user_input = input("A: Circle | B: Star | C: 3 Wavy Lines | D: Cross | E: Square  ")
                #check user answer and establish guess
            if(self.user_input.upper() == "A"):
                print("You guessed 'Circle'!")
                self.guess = "Circle"
            elif (self.user_input.upper() == "B"):
                print("You guessed 'Star'!")
                self.guess = "Star"
            elif(self.user_input.upper() == "C"):
                print("You guessed '3 Wavy Lines'!")
                self.guess = "3 Wavy Lines"
            elif(self.user_input.upper() == "D"):
                print("You guessed 'Cross'!")
                self.guess = "Cross"
            elif(self.user_input.upper() == "E"):
                print("You guessed 'Square'!")
                self.guess = "Square"
            #if guess is invalid:
            else:
                print("Make a valid guess (A. B. C. D. or E.)")
                continue

            #variable True if a guess is made, False if guess not yet made or between answered guesses
            #True here following guess input above
            self.made_a_guess = True

            #adds increment to a sum of total guesses made by player
            self.total_guesses += 1

            #checks for answers and tallies correct/wrong answers:
            if(self.guess == self.mystery_card):
                #validates correct answer
                print(self.name + ", you got it right!!!")
                #adds correct answer to correct answers by player instance
                self.correct_answers += 1
                
            else:
                #validates wrong answer
                print("Nice Try, " + self.name + " But No Cigar!  The correct answer is:  ", self.mystery_card)
                #adds wrong answer to wrong answers by player instance
                self.wrong_answers += 1

            #calculates percent of correct answers
            self.percent_correct = round((self.correct_answers / self.total_guesses) * 100, 2)

            #calculates statistical percent of correct answers likely from given list length
            self.statistical_average_correct = round((1 / self.list) *100, 2)
            
            #calculates likely amount of correct guesses based on chance alone for any given amount of guesses
            self.random_guess_number = ((self.statistical_average_correct / 100) * self.total_guesses)/ 5

            #calculates random average statistical percentage of correct answers given number of guesses
            self.random_average_percentage = (self.random_guess_number / self.total_guesses) * 100
            #prints out percent correct vs. statistical correct answers 
            print("Your percent of answers correct is: ", self.percent_correct)
            print("Number of answers correct by chance?", self.statistical_average_correct / 100)
            print("list length test:", self.list)

            #if player has made a guess
            if(self.made_a_guess):
                #ask if player wants to try again
                self.try_again = input("Try again?  Y/N | " )

            #if player chooses to try again
            if(self.try_again.upper() == "Y"):
                #draw a different card
                self.draw_card()
                #initiate another guess
                self.guess_card()
            #if player chooses to quit
            elif(self.try_again.upper() == "N"):
                print("Great effort!  Thanks for playing, " + self.name, " Here are your final stats: ")
                print("Total Guesses: ", self.total_guesses)
                print("Total Correct: ", self.correct_answers)
                print("Your percent correct: ", self.percent_correct)
                print("self.statistical_average_correct value:", self.statistical_average_correct)
                
                #if performed worse or better than chance, give result
                if(self.percent_correct > self.statistical_average_correct):
                    print("You are positively psychic!!! You performed ", round(self.percent_correct - self.statistical_average_correct, 2),  "percent better than chance alone!")
                elif(self.percent_correct < self.statistical_average_correct):
                    print("You are negatively psychic!!! You performed ", round(self.statistical_average_correct - self.percent_correct, 2), "percent worse than chance alone!")
                elif(int(self.percent_correct) == int(self.statistical_average_correct)):
                    print("You are not psychic at all!!!  You performed the same as chance alone.")
                break
            else:
                print("Choose Y/N: " )
                continue
            return self.guess
    
    #player object representation function
    def __repr__(self):
        rep = "Player named {}, who has made {} guesses, with {} correct.".format(self.name, self.total_guesses, self.percent_correct)
        return rep
    
#instance of player class, asks for name
new_player1 = Player(str(input("What is your name?")))

#new player instance draws a card
new_player1.draw_card()

#new player guesses card
new_player1.guess_card()











        
