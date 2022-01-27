import random    
from typing import List


class Hangman:
    """
    The hangman game class with his methods
    """

    def __init__(self):   
        """ set up attributes to start the game:
        lives int: Number of times to attempt
        possible_words: A list of possible words
        word_to_find: The word to be found. It's selected from possible_words
        correctly_guessed_letters: A list contains correctly letters
        wrongly_guessed_letters: A list contains wrongly letters
        turn_count int: Number of round that game has run
        error_count int: Number of error that player makes
        """
        self.lives: int=5
        self.possible_words: List[str] = ['becode','funny','learning','mathematics','sessions','running','sunlight', 'game', 'tofu']
        self.word_to_find: List[str] =[c for c in random.choice(self.possible_words)]
        self.correctly_guessed_letters: List[str] = ["_"] * len(self.word_to_find)
        self.wrongly_guessed_letters: List[str] = []
        self.turn_count: int =0
        self.error_count: int =0
        
        

    def play(self):
        """ This method asks player to enter a letter. 
            It checks if user input matches with the letter in word_to_find list.
            It adds this letter to correctly_guessed_letters.
            It counts number of error_count and lives."""

        while True:
            user_input = input(" Please enter a letter: ").upper()
            if user_input.isalpha() and len(user_input) == 1:
                if user_input in self.word_to_find:
                    print("It's corret!")
                    for i, c in enumerate(self.word_to_find):
                        if c == user_input:
                            self.correctly_guessed_letters[i] = user_input
                else:
                    print("Wrong guess!")
                    self.wrongly_guessed_letter.append(user_input)
                    self.error_count +=1
                    self.lives -=1
                break

    def start_game(self):
        """This method starts the game.
        It checks if the player still has lives or the word is found.
        It increases turn_count when play function is called and display the info about the current
        situation of the game."""
        while True:
            self.play()
            self.turn_count +=1
            print(self.correctly_guessed_letters)
            print(self.wrongly_guessed_letters)
            print(self.lives)
            print(self.error_count)
            print(self.turn_count)
            if self.correctly_guessed_letters == self.word_to_find:
                self.well_played()
                break
            elif self.lives == 0:
                self.game_over()
                break


    def well_played(self):
        """This method will show the correct result when player wins the game"""
        print("You found the word: {} in {} turns with {} errors.".format(self.word_to_find, self.turn_count, self.error_count))
    
    def game_over(self):
        """ This method will show when player lose this game. """
        print("Sorry, you lost!")


    






