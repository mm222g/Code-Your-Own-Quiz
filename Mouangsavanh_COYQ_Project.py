# level one question
level_one = "Mary had a __1__ lamb, little __2__ , little lamb!\n"\
             "Mary __3__ a little lamb,\n"\
             "Its fleece was __4__ as snow."

# level one answers
level_one_answers = ["little", "lamb", "had", "white"]

# level two question
level_two = "And everywhere that __1__ went, Mary __2__ , Mary went!\n"\
               "__3__ that Mary went,\n"\
               "The __4__ was sure to go."

# level two answers
level_two_answers = ["Mary", "went", "Everywhere", "lamb"]

# level three question
level_three = "He __1__ her to __2__ one day, school one day, school one day!\n"\
             "He followed her to school __3__ day,\n"\
             "Which was __4__ the rules."

# level three answers
level_three_answers = ["followed", "school", "one", "against"]

# level four question
level_four = "It made the __1__ laugh and __2__, __3__ and play, laugh and play!\n"\
             "It made the children laugh and play,\n"\
             "To see a lamb at __4__."

# level four answers
level_four_answers = ["children", "play", "laugh", "school"]



# Game has 3 or more levels and each level contains 4 or more blanks to fill in
questions = ["__1__", "__2__","__3__","__4__"]

# Immediately after running the program, user is prompted to select a difficulty level from easy / medium / hard
def get_level():
    print "Hi I am Mary, would you like to join me in a sing-along? Select a level to begin our song. You get 4 attempts per question."
    level_name = raw_input("Type in one, two, three or four\n").lower()
    if level_name=="one":
        process_paragraph(level_one, questions, level_one_answers)
    elif level_name=="two":
        process_paragraph(level_two, questions, level_two_answers)
    elif level_name=="three":
        process_paragraph(level_three, questions, level_three_answers)
    elif level_name=="four":
        process_paragraph(level_four, questions, level_four_answers)
    else:
        print "Please choose only one, two, three, or four"
    print get_level

# Once a level is selected, game displays a fill-in-the-blank and a prompt to fill in the first blank.
# When player guesses correctly, new prompt shows with correct answer in the previous blank and a new prompt for the next blank
# When player guesses incorrectly, they are prompted to try again
def process_paragraph(quiz, blanks, answers):
	print quiz
	for count_blanks in range(0, len(blanks)):
		answer_input = raw_input("Whatdo you mean, " + blanks[count_blanks] +"?")
		attempts = 1
		max_attempts = 4
		while answer_input.lower()!= answers[count_blanks]:
			attempts += 1
			answer_input = raw_input("Try again. What do you mean," + blanks[count_blanks] + "?")
			if attempts == max_attempts:
				print ("Mary needs her lamb! Try again!")
				get_level()
		else:
			quiz = quiz.replace(blanks[count_blanks], answers[count_blanks])
			print("Yes! You are on a roll! " + quiz)
	if len(blanks) == len(answers):
		print ("Thanks for singing along! Want to try another verse?")
		get_level()
