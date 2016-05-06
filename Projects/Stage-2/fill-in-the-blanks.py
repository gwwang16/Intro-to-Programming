# IPND Stage 2 Final Project

# Quiz bank
easy_quiz = '''In this stage, you will use the ___1___ programming language to build your own ___2___. 
You will use a fill-in-the blank style to ___3___ a ___2___ that can even be used as a study tool 
to help you remember important ___4___.'''
easy_answer = ['Python', 'quiz', 'creat', 'vocabulary']

medium_quiz = '''For this ___1___, you'll be building a Fill-in-the-Blanks ___2___.
Your ___2___ will prompt a user with a paragraph containing several ___3___s.
The user should then be asked to fill in each blank appropriately to complete the paragraph.
This can be used as a study tool to help you remember important ___4___!'''
medium_answer = ['project', 'quiz', 'blank', 'vocabulary']

hard_quiz = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''
hard_answer = ['function', 'variables', 'nothing', 'list']

white_blanks = ['___1___', '___2___', '___3___', '___4___']

levels = ['easy', 'medium', 'hard']

# Print language bank
welcome = "*" * 50 + "\n" + "  Welcome to this quiz. \n  Please select difficulty by typing it in." + "\n" + "*" * 50
congratulation = "*" * 50 + "\n" + "  Congratulation! You have completed this quiz! " + "\n" + "*" * 50
sorry = "*" * 50 + "\n" + "  Sorry! You lost the game! " + "\n" + "*" * 50

def check_answer(user_input_answer, answer, index_blank):
	'''Check the answer right or wrong. Input: [user_input_answer, answer, index_blank]. Output: [Correct or Incorrect]'''
	if user_input_answer == answer[index_blank]:
		return 'Correct'
	else:
		return 'Incorrect'

def level_chosen(user_input_level):	
	'''Determine the game level, quiz, and answer. Input: [user_inpu]. Output :[quiz, answer, and level]'''
	while user_input_level not in levels:
		user_input_level = raw_input( "Wrong input! \nPossible choices are easy, medium, and hard: "" ")
	if user_input_level == 'easy':
		return easy_quiz, easy_answer, 'easy'
	if user_input_level == 'medium':
		return medium_quiz, medium_answer, 'medium'
	else:
		return hard_quiz, hard_answer , 'hard'

# The game body
def fill_in_blanks():
	'''Fill in blank game, chose game level first, and then fill all the white blanks'''
	user_input_level = raw_input( "Possible choices are easy, medium, and hard: "" ")
	quiz, answer, difficulty_chosen = level_chosen(user_input_level)
	print ("\n" + "You've chosen " + difficulty_chosen + " difficulty." + "\n" + "*" * 50 + "\nYou will get 5 guesses per problem.\nThe quiz is: \n" + quiz + "\n")
	index_blank, num_guess, total_guess = 0, 1, 5
	while index_blank < len(white_blanks) and num_guess < total_guess: #1 there have to check if the tries exceeded two times. This tries check make the game end... 
		num_guess = 1 # guess number reset
		user_input_answer = raw_input("What should be filled in for " + str(white_blanks[index_blank]) + "? ")
		while check_answer(user_input_answer, answer, index_blank) == 'Incorrect' and num_guess < total_guess:#1 this tries check make the answer_input stop. I tried to remove one of them, but the results output are not satisfactory...
			print "You have " + str(total_guess - num_guess) + " try left"
			user_input_answer = raw_input("The answer is wrong, try again: " + " ")
			num_guess += 1		
		if 	check_answer(user_input_answer, answer, index_blank) == 'Correct': #2 The answer have to be checked again, to avoid the 'Correct' and quiz print when the tries exceeded....
			quiz = quiz.replace(white_blanks[index_blank], user_input_answer)
			print "Correct! \n" + quiz + "\n"
		index_blank += 1
	if index_blank == len(white_blanks):
		return congratulation 
	return sorry # I have tried my best to shorten this function... But it still longer than 18 lines...:(

print welcome
print fill_in_blanks() 
