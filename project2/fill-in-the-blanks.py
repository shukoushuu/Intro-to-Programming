# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/

easy_quiz = ''' A common first thing to do in a language is display
'Hello __1__!'  In __2__ this is particularly easy; all you have to do
is type in:
__3__ "Hello __1__!"
Of course, that isn't a very useful thing to do. However, it is an
example of how to output to the user using the __3__ command, and
produces a program which does something, so it is useful in that capacity.

It may seem a bit odd to do something in a Turing complete language that
can be done even more easily with an __4__ file in a browser, but it's
a step in learning __2__ syntax, and that's really its purpose.'''
easy_answer = ['world', 'Python', 'print', 'HTML']

medium_quiz = ''' A __1__ is created with the def keyword.  You specify the inputs a
__1__ takes by adding __2__ separated by commas between the parentheses.
__1__s by default returns __3__ if you don't specify the value to retrun.
__2__ can be standard data types such as string, integer, dictionary, tuple,
and __4__ or can be more complicated such as objects and lambda functions.'''
medium_answer = ['function', 'arguments', 'none', 'list']

hard_quiz = '''The World Wide Web is mainly composed of __1__ documents. __1__ represents 
Hypertext Markup Language, which is used by the __2__ to parse the webpage. The major pieces 
of the World Wide Web include __3__, __4__ and __5__. And __3__ interact with __5__ with HTTP.'''
hard_answer = ['HTML', 'browsers', 'clients', 'Internet', 'servers']

def select_level():
	"""The function prompts the user to select a game difficulty level from easy, medium, and hard.

    Args:
        Takes no inputs.

    Returns:
        difficulty (str): The selected difficulty level.

    """
	print "Please select a game difficulty by typing it in!\n"
	choices = ['easy', 'medium', 'hard']
	while True:
		difficulty = raw_input("Possible choices include easy, medium, and hard.\n")
		if difficulty in choices:
			print "You've chosen " + difficulty + "!\n"
			break
		else:
			print "That's not an option!"
	return difficulty

def set_guess_num():
	"""The function prompts the user to set how many wrong guesses one can make for each blank before lose.

    Args:
        Takes no inputs.

    Returns:
        int: The number of guesses you can try for each blank.

    """
	guess_num = raw_input("Set how many wrong guesses you can make before you lose.\n")
	print "You will get " + guess_num + " guesses per problem\n"
	return int(guess_num)

def initialize_game():
	"""The function initializes the game according to the difficulty level selected.

    Args:
        Takes no inputs.

    Returns:
        paragraph (str): The initialized paragraph.
        answers (list): The initialized answers.
        guess_num (int): The number of guesses you can try for each blank.
        blank_num (int): The number of blanks you need to guess.
    """
	difficulty = select_level()
	if difficulty == 'easy':
		paragraph = easy_quiz
		answers = easy_answer
	else:
		if difficulty == 'medium':
			paragraph = medium_quiz
			answers = medium_answer
		else:
			paragraph = hard_quiz
			answers = hard_answer
	guess_num = set_guess_num()
	blank_num = len(answers)
	return paragraph, answers, guess_num, blank_num

def prompt_try(paragraph, blank):
	"""The function displays the paragraph and prompts the user to try an answer to fill the blank.

    Args:
        paragraph (str): The paragraph.
        blank (str): The blank needs to be filled.

    Returns:
        str: User input.

    """
	print "The current paragraph reads as such:\n" + paragraph + "\n\n"
	return raw_input("What should be substituted in for" + blank + "?") 

def word_contain_blank(word, blank):
	"""The function tests whether or not a word contains the blank.

    Args:
        word (str): The word to be tested.
        blank (str): The blank.

    Returns:
        str: Return the blank if the word contains the blank; return None otherwise.

    """
	if blank in word:
		return blank
	else:
		return None

def replace_blank(paragraph, blank, answer):
	"""The function replaces the blanks in the paragraph with the answer.

    Args:
        paragraph (str): The paragraph with blanks.
        blank (str): The blank need to be replaced.
        answer (str): The answer to replace the blank.

    Returns:
        str: The updated paragraph with the blanks replaced by the answer.

    """  
	replaced = []
	splitted = paragraph.split()
	for entry in splitted:
		replacement = word_contain_blank(entry, blank)
		if replacement == None:
			replaced.append(entry)
		else:
			replaced.append(entry.replace(replacement, answer))
	return " ".join(replaced)

def try_correct(paragraph, blank, answer):
	"""The function is called when the trial is correct:
	It displays the Correct information, and calls replace_blank() function 
	to replaces the blanks in the paragraph with the answer.

    Args:
        paragraph (str): The paragraph with blanks.
        blank (str): The blank need to be replaced.
        answer (str): The answer to replace the blank.

    Returns:
        paragraph (str): The updated paragraph with the blanks replaced by the answer.

    """ 
	print "Correct!\n\n"				
	paragraph = replace_blank(paragraph, blank, answer)
	return paragraph

def try_wrong(guess_left, guess_zero_left):
	"""The function is called when the trial is wrong:
	It updates the number of guesses left and displays the Wrong information accordingly.

    Args:
        guess_left (int): The number of guesses left.
        guess_zero_left (int): 0 guess left(means you lose).

    Returns:
        guess_left(int): The updated number of guesses left.

    """ 
	guess_left -= 1
	if guess_left != guess_zero_left:
		print "Wrong! Try again. You have " + str(guess_left) + " guesses left.\n\n"
	return guess_left


def play_game(paragraph, answers, guess_num, blank_num):
	"""The main function to play the game, called after initialize_game().

    Args:
        paragraph (str): The initialized paragraph.
        answers (list): The initialized answers.
        guess_num (int): The number of guesses you can try for each blank.
        blank_num (int): The number of blanks you need to guess.

    Returns:
        No returns.

    """ 	
	index, guess_zero_left = 0, 0
	while index < blank_num:
		guess_left = guess_num
		blank = "__" + str(index + 1) + "__"
		while guess_left > guess_zero_left:
			answer = answers[index]
			trial = prompt_try(paragraph, blank)			
			if trial == answer:
				paragraph = try_correct(paragraph, blank, answer)
				index += 1
				break
			guess_left = try_wrong(guess_left, guess_zero_left)
		if guess_left == guess_zero_left:
			print "\nYou've failed too many straight guesses!  Game over!"
			break
	if guess_left != guess_zero_left:
		print paragraph + "\n\nYou won!"



paragraph, answers, guess_num, blank_num = initialize_game()
play_game(paragraph, answers, guess_num, blank_num)