from card import Card


class Director:
    """This Class will manage the flow of the game
    and the update of the score in screen
    """

    def __init__(self):
        """ This is the constructor of class
        declaring the attributes to use in the game
        """
        self.score = 300
        self.is_playing = True
        self.card_1 = 0
        self.card_2 = 0
        self.user_guess = ""
        self.card = Card()

    def start_game(self):
        """This Method will manage the flow of the 
        game
        """
        while self.is_playing:

            self.update_screen()
            self.update_score()
            self.play_again()

    def update_screen(self):
        """This Method will be printing on screen the
        output for the game and the update during the game.
        """

        self.card_1 = self.card.roll_card()
        self.card_2 = self.card.roll_card()
        print(f"The first card is: {self.card_1}")
        self.user_guess = input(" Higher or Lower? [h/l] ")
        print(f"The next card is: {self.card_2}")

    def update_score(self):
        """This Method will update the score for
        the player and the total score
        """

        if self.user_guess.lower() == "h":
            # higher
            if self.card_1 <= self.card_2:
                self.score += 100
                print(f"Correct! Your score is {self.score}")
            elif self.card_1 > self.card_2:
                self.score -= 75
                print(f"Wrong! Your score is {self.score}")
                if self.score <= 0:
                    print("Game Over")
                    print(f"Your score is {self.score}")
                    self.is_playing = False
        elif self.user_guess.lower() == "l":
            # lower
            if self.card_1 >= self.card_2:
                self.score += 100
                print(f"Correct! Your score is {self.score}")
            elif self.card_1 > self.card_2:
                self.score -= 75
                print(f"Wrong! Your score is {self.score}")
                if self.score <= 0:
                    print("Game Over")
                    print(f"Your score is {self.score}")
                    self.is_playing = False

    def play_again(self):
        """ Get User input for continue game
        Args:
            Director: Class
        Returns:
            nothing
        """
        # self.next_game = input("Would you like to play again? [y/n] ")
        # self.is_playing = (self.next_game.lower() == 'y')

        self.ask_user = input("Would you like to play again? [y/n] ")
        while self.ask_user.lower() == "y":
            if self.ask_user == "y":
                return
            elif self.ask_user == "n":
                print("Game Over!")
