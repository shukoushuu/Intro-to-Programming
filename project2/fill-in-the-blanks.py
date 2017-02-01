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
def prompt_try(current_paragraph, blank):
	# display the current paragraph and 
	# prompt the used to try an answer to fill the blank
	print "The current paragraph reads as such:\n" + current_paragraph + "\n\n"
	return raw_input("What should be substituted in for" + blank + "?") 

def word_contain_blank(word, blank):
	# test whether or not a string contains the blank
	# True: return the blank; False: return None
	if blank in word:
		return blank
	else:
		return None

def replace_blank(paragraph, blank, answer):  
	# replace the blanks in the paragraph with the answer
	replaced = []
	splitted = paragraph.split()
	for entry in splitted:
		replacement = word_contain_blank(entry, blank)
		if replacement == None:
			replaced.append(entry)
		else:
			replaced.append(entry.replace(replacement, answer))
	return " ".join(replaced)

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

print "Please select a game difficulty by typing it in!\n"
choices = ['easy', 'medium', 'hard']
while True:
	difficulty = raw_input("Possible choices include easy, medium, and hard.\n")
	if difficulty in choices:
		print "You've chosen " + difficulty + "!\n"
		break
	else:
		print "That's not an option!"

guess_num = raw_input("Set how many wrong guesses you can make before you lose.\n")
print "You will get " + str(guess_num) + " guesses per problem\n"

if difficulty == 'easy':
	current_paragraph = easy_quiz
	answers = easy_answer
else:
	if difficulty == 'medium':
		current_paragraph = medium_quiz
		answers = medium_answer
	else:
		current_paragraph = hard_quiz
		answers = hard_answer
blank_num = len(answers)

index = 0
while index < blank_num:
	guess_left = int(guess_num)
	blank = "__" + str(index + 1) + "__"
	while guess_left > 0:
		trial = prompt_try(current_paragraph, blank)
		answer = answers[index]
		if trial == answer:
			print "Correct!\n\n"
			current_paragraph = replace_blank(current_paragraph, blank, answer)
			index += 1
			break
		else:
			guess_left -= 1
			if guess_left != 0:
				print "Wrong! Try again. You have " + str(guess_left) + " guesses left."
	if guess_left == 0:
		print "\nYou've failed too many straight guesses!  Game over!"
		break

if guess_left != 0:
	print current_paragraph + "\nYou won!"