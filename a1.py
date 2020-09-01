"""
CSSE1001 Assignment 1
Semester 2, 2020
"""

from a1_support import *

# Fill these in with your details
__author__ = "{{Banghong Liang}} ({{46336873}})"
__email__ = "s4633687@student.uq.edu.au"
__date__ = "08/31/2020"


# if won: "You have guessed the word correctly. Congratulations".\
# if lost: "Your guess was wrong. The correct word was "{word}""

# word_select: A string representing a FIXED or ARBITRARY word selection.
# guess_no: An integer representing how many guesses the player has made.
# word: A string representing the word being guessed by the player.
# word_length: An integer representing the length of the word being guessed
# by the player.

# Write your code here (i.e. functions)
def select_word_at_random(word_select)-> str:
        """
        Given the word select is either “FIXED” or “ARBITRARY” this
        function will return a string randomly selected from WORDS FIXED.txt
        or WORDS ARBITRARY.txt respectively. If word select is anything other
        then the expected input then this function should return None.
        
        Parameters:
                word_select (string): string is either "FIXED" or "ARBITRARY"
        Returns:
                (string): A string randomly selected from WORDS FIXED.txt or WORDS
                ARBITRARY.txt respectively.
        """
        words_tuple = []
        if word_select != 'FIXED' and word_select != 'ARBITRARY':
                print('not fixed or arbitrary')
                return None
        else:
                words_tuple = load_words(word_select)
                word_index = random_index(load_words(word_select))
                print(words_tuple[word_index])
                return words_tuple[word_index]

        
        

def create_guess_line(guess_no, word_length)-> str:
        """
        This function returns the string representing the display corresponding to
        the guess number integer, guess no.

        Parameters:
                guess_no (int): the guess number integer
                word_length (int): the length of the word
        Returns:
                (string): the string representing the display corresponding to the
                guess number integer
        """
        if word_length == 6:
                if   guess_no == 1:
                        return 'Guess 1| * | * | - | - | - | - |'
                elif guess_no == 2:
                        return 'Guess 2| - | - | * | * | * | - |'
                elif guess_no == 3:
                        return 'Guess 3| - | - | * | * | * | - |'
                elif guess_no == 4:
                        return 'Guess 4| - | - | - | * | * | * |'
                elif guess_no == 5:
                        return 'Guess 5| - | - | * | * | * | * |'
                elif guess_no == 6:
                        return 'Guess 6| * | * | * | * | * | * |'
        elif word_length == 7:
                if   guess_no == 1:
                        return 'Guess 1| * | * | - | - | - | - | - |'
                elif guess_no == 2:
                        return 'Guess 2| - | * | * | - | - | - | - |'
                elif guess_no == 3:
                        return 'Guess 3| - | - | - | - | * | * | * |'
                elif guess_no == 4:
                        return 'Guess 4| - | - | * | * | * | * | - |'
                elif guess_no == 5:
                        return 'Guess 5| - | - | - | * | * | * | * |'
                elif guess_no == 6:
                        return 'Guess 6| - | - | * | * | * | * | * |'
                elif guess_no == 7:
                        return 'Guess 7| - | - | * | * | * | * | - |'
        elif word_length == 8:
                if   guess_no == 1:
                        return 'Guess 1| * | * | - | - | - | - | - | - |'
                elif guess_no == 2:
                        return 'Guess 2| - | * | * | * | - | - | - | - |'
                elif guess_no == 3:
                        return 'Guess 3| - | - | - | - | * | * | * | * |'
                elif guess_no == 4:
                        return 'Guess 4| - | - | - | * | * | * | - | - |'
                elif guess_no == 5:
                        return 'Guess 5| - | - | - | * | * | * | * | - |'
                elif guess_no == 6:
                        return 'Guess 6| - | - | - | - | - | * | * | * |'
                elif guess_no == 7:
                        return 'Guess 7| - | - | * | * | * | * | * | * |'
                elif guess_no == 8:
                        return 'Guess 8| * | * | * | * | * | * | * | * |'
        elif word_length == 9:
                if   guess_no == 1:
                        return 'Guess 1| * | * | - | - | - | - | - | - | - |'
                elif guess_no == 2:
                        return 'Guess 2| - | * | * | * | - | - | - | - | - |'
                elif guess_no == 3:
                        return 'Guess 3| - | - | - | - | * | * | * | * | - |'
                elif guess_no == 4:
                        return 'Guess 4| - | - | - | * | * | * | - | - | - |'
                elif guess_no == 5:
                        return 'Guess 5| - | - | - | * | * | * | * | - | - |'
                elif guess_no == 6:
                        return 'Guess 6| - | - | - | - | - | * | * | * | - |'
                elif guess_no == 7:
                        return 'Guess 7| - | - | - | * | * | * | * | * | - |'
                elif guess_no == 8:
                        return 'Guess 8| - | - | * | * | * | * | * | * | * |'
                elif guess_no == 9:
                        return 'Guess 9| * | * | * | * | * | * | * | * | * |'

        else:
                return ''
        
def display_guess_matrix(guess_no, word_length, scores)-> None:
        """
        This function prints the progress of the game. This includes all line strings
        for guesses up to guess_no with their corresponding scores (a tuple containing
        all previous scores), and the line string for guess no (without a score)

        Parameters:
                guess_no (int): the guess number integer
                word_length (int): the length of the word
                scores (tuple<str>):  a tuple containing all previous scores
        Returns:
                (None): prints the progress of the game
        """
        # First two lines
        if   word_length == 6:
                print('       | 1 | 2 | 3 | 4 | 5 | 6 |\n---------------------------------')
        elif word_length == 7:
                print('       | 1 | 2 | 3 | 4 | 5 | 6 | 7 |\n-------------------------------------')
        elif word_length == 8:
                print('       | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |\n-----------------------------------------')
        elif word_length == 9:
                print('       | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |\n---------------------------------------------')

        i = 0
        cur_line = ''
        for i in range(guess_no):
                cur_line = create_guess_line(i+1, word_length)
                if i+1 != guess_no:
                        cur_line += "  " + str(scores[i]) + " Points"
                cur_line += string_To(word_length)
                
                print(cur_line)


def string_To(word_length):
        
        if word_length == 6:
                return '\n---------------------------------'
        elif word_length == 7:
                return '\n-------------------------------------'
        elif word_length == 8:
                return '\n-----------------------------------------'
        elif word_length == 9:
                return '\n---------------------------------------------'
        


def compute_value_for_guess(word, start_index, end_index, guess)-> int:
        """
        This function prints the progress of the game. This includes all line strings
        for guesses up to guess no with their corresponding scores (a tuple containing
        all previous scores), and the line string for guess no (without a score)

        Parameters:
                word (str): a string representing the word the player has to guess
                start_index (int): the start index of the substring
                end_index (int): the end index of the substring
                guess (str): a string representing the guess attempt the player has made
        Returns:
                (int): Return the score, an integer, the player is awarded for a specific
                guess.
        """
        
        guess_str = word[start_index:end_index + 1]
        guess_score = 0
        
        #print(guess_str)
        
        for i in range(len(guess_str)):
                if guess[i] == guess_str[i] and guess[i] in VOWELS:
                        guess_score += 14
                elif guess[i] == guess_str[i] and guess[i] in CONSONANTS:
                        guess_score += 12
                else:
                        if guess[i] in guess_str:
                                guess_score += 5

        return guess_score

def use_actions(actions):

        while actions != 's' or actions != 'h' or actions != 'q':
                print("""
Please enter a valid command.
""")
                actions =  input("""
Enter an input action. Choices are:
s - start game
h - get help on game rules
q - quit game: 
""")
                if actions == 's':
                        action_s()
                        return True
                elif actions == 'h':
                        action_h()
                        return True
                elif actions == 'q':
                        action_q()
                        return True
        
def action_s():
        start_game = input("""Do you want a 'FIXED' or 'ARBITRARY' length word?: """)

        if start_game == 'FIXED':
                print('Now try and guess the word, step by step!!')
                select_word_at_random('FIXED')
                return True
        elif start_game == 'ARBITRARY':
                print('Now try and guess the word, step by step!!')
                select_word_at_random('ARBITRARY')
                return True
        else:
                action_s()
def action_h():
        print("""
Game rules - You have to guess letters in place of the asterixis. 
Each vowel guessed in the correct position gets 14 points. 
Each consonant guessed in the correct position gets 12 points. 
Each letter guessed correctly but in the wrong position gets 5 points. 
If the true letters were "dog", say, and you guessed "hod", 
you would score 14 points for guessing the vowel, "o", in the correct 
position and 5 points for guessing "d" correctly, but in the 
incorrect position. Your score would therefore be 19 points.
""")
        action_s()
        
def action_q():
        """
        (None): Quit the game by returning False
        """
        return False
        
def main():
        
        """
	Handles top-level interaction with user.

	At the start of the game the player should be greeted with the Welcome message.
	Once the guessing sequence commences the game should loop for the correct number
	of rounds until either the player wins by guessing the correct word or loses by
	guessing the incorrect word.
	
	"""
	# Write the code for your main function here
        print("""
Welcome to the Criss-Cross Multi-Step Word Guessing Game!
""")
        actions =  input("""
Enter an input action. Choices are:
s - start game
h - get help on game rules
q - quit game: 
""")       
        if actions == 's': # s - start game
                action_s() 
        elif actions == 'h':# h - get help on game rules
                action_h() 
        elif actions == 'q':# q - quit game
                action_q() 
        else:
                use_actions(actions)
        
        
        

if __name__ == "__main__":
	main()
