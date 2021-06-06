# importing library
import arcade
import random
# variables
total_score = 0
questions_missed = 0
question = 1


def intro():
    # Welcome statement
    print("Welcome to my Final Project! \n"
          "In this project I will be quizzing you on Star Wars trivia!")


# question 1
def han_death():
    global question
    global questions_missed
    global total_score
    print("Question", question)
    question += 1
    print("In what movie did Han Solo die?")
    print("A) The Phantom Menace \n"
          "B) The Force Awakens \n"
          "C) Rise of Skywalker \n"
          "D) Return of the Jedi \n ")
    game_choice = input("Enter your choice ")
    if game_choice.lower() == "b":
        print("Congratulations, you got the question right!\n" +
              "Unfortunately  he was stabbed by his son with a lightsaber.")
        total_score += 20
        print("Your new score is ", total_score)
        print("You have missed ", questions_missed, " questions.")

    else:
        print("The correct answer is D")
        questions_missed += 1
        print("You have missed ", questions_missed, " questions")


# question 2
def movie_count():
    global question
    global questions_missed
    global total_score
    print("Question ", question)
    question += 1
    total_movies = input("How many Star Wars movies are there? ")
    if total_movies == "9":
        print("Nice job!")
        total_score += 20
        print("Your new score is", total_score)
        print("You have missed ", questions_missed, " questions.")

    else:
        print("There are 9 movies, Rouge One is a movie but does not follow the timeline.")
        print("Your current score is:", total_score)
        questions_missed += print("You have missed ", questions_missed, " questions")

# question 3


def george_lucas():
    global question
    global questions_missed
    global total_score
    print("Question ", question)
    question += 1
    print("Why did George Lucas sell the Star Wars franchise to Disney?")
    print("A) He wanted to spend time with his family and raise his daughter \n"
          "B) He was tired of the Star Wars fandom \n" 
          "C) He had some scripts written for the next trilogy but was too tired to direct them \n" 
          "D) He was stressed about movie reactions")
    lucas_daughter = input("Enter  your choice ")
    if lucas_daughter.lower() == "a":
        print("Congratulations! He wanted to spend time with his family.")
        total_score += 20
        print("Your score is ", total_score)
        print("You have missed ", questions_missed, " questions.")

    else:
        print("He sold the franchise to spend time with his family")
        questions_missed += 1
        print("You have missed ", questions_missed, " questions.")

# question 4


def lucas_net_worth():
    global question
    global questions_missed
    global total_score
    print("Question ", question)
    question += 1
    net_worth = input("What is George Lucas's net worth? ")
    if net_worth.lower() == "7 billion usd":
        print("That is correct!")
        total_score += 20
        print("Your new score is ", total_score)
        print("You have missed ", questions_missed, " questions.")

    else:
        print("His net worth is 7 billion USD")
        questions_missed += 1
        print("You have missed ", questions_missed, " questions")

# question 5


def species():
    global question
    global questions_missed
    global total_score
    print("Question ", question)
    question += 1
    print(" What species is Jar Jar Binks?")
    print("A) Toydarian\n"
          "B) Wookie\n"
          "C) Gungan\n"
          "D) Geonosian")
    jarjar_species = input("Enter your choice ")
    if jarjar_species.lower() == "c":
        print("Congratulations! Jar Jar Binks is from Naboo.")
        total_score += 20
        print("Your score is ", total_score)
        print("You have missed ", questions_missed, " questions.")

    else:
        print("No, Jar Jar Binks is a Gungan, while the others are other species of creatures from Star Wars")
        questions_missed += 1
        print("You have missed ", questions_missed, " questions.")

# question 6


def stormtrooper_number():
    global question
    global questions_missed
    global total_score
    print("Question ", question)
    question += 1
    print("What is Finn's Stormtrooper number?")
    print("A) TK-421\n"
          "B) CT-7567\n"
          "C) CC-2224\n"
          "D) FN-2187")
    finn_number = input("Enter your choice ")
    if finn_number.lower() == "d":
        print("Congratulations! The others are from the movies or Clone Wars.")
        total_score += 20
        print("Your score is ", total_score)
        print("You have missed ", questions_missed, " questions.")

    else:
        print("No, Finn's number was FN-2187, Poe gave Finn as a name to him")
        questions_missed += 1
        print("You have missed ", questions_missed, " questions.")

# question 7


def shared_scenes():
    global question
    global questions_missed
    global total_score
    print("Question ", question)
    question += 1
    scenes_shared = input("How many scenes did Darth Vader and C-3PO share? ")
    if scenes_shared == "1" or "one":
        print("Correct! This scene was in The Empire Strikes back.")
        total_score += 20
        print("Your score is ", total_score)
        print("You have missed ", questions_missed, " questions.")

    else:
        print("Shockingly there was only 1 scene!")
        questions_missed += 1
        print("You have missed ", questions_missed, " questions.")

# question 8


def skywalker_mother():
    global question
    global questions_missed
    global total_score
    print("Question ", question)
    question += 1
    print("Who is Anakin Skywalkers mother?")
    print("A) Leia Skywalker\n"
          "B) Satine Kryze\n"
          "C) Maz Kanata\n"
          "D) Shimi Skywalker")
    anakin_mother = input("Enter your choice ")
    if anakin_mother.lower() == "d":
        print("Congratulations! Shimi Skywalker is Anakin's mother")
        total_score += 20
        print("Your score is ", total_score)
        print("You have missed ", questions_missed, " questions.")
    else:
        print("Shimi Skywalker is Anakin's mother")
        questions_missed += 1
        print("You have missed ", questions_missed, " questions.")

# question 9


def leia_luke():
    global question
    global questions_missed
    global total_score
    print("Question ", question)
    question += 1
    twins = input("Were Leia and Luke twins? ")
    if twins.lower() == "yes":
        print("Correct! They were twins of Padme Amidala.")
        total_score += 20
        print("Your score is ", total_score)
        print("You have missed ", questions_missed, " questions.")

    else:
        print("They were twins.")
        questions_missed += 1
        print("You have missed ", questions_missed, " questions.")

# question 10


def arm_colour():
    global question
    global questions_missed
    global total_score
    print("Question ", question)
    question += 1
    print("What colour is C-3PO’s arm in the force awakens?")
    print("A) Red\n"
          "B) Purple\n"
          "C) Gold\n"
          "D) Green")
    metal_arm = input("Enter your choice ")
    if metal_arm.lower() == "a":
        print("Congratulations! C-3PO's arm was red.")
        total_score += 20
        print("Your score is ", total_score)
        print("You have missed ", questions_missed, " questions.")

    else:
        print("No, C-3PO's arm was red in The Force Awakens")
        questions_missed += 1
        print("You have missed ", questions_missed, " questions.")

# question 11


def general_grevious():
    global question
    global questions_missed
    global total_score
    print("Question ", question)
    question += 1
    grevious_lightsabers = input("How many light sabers did General Grevious have? ")
    if grevious_lightsabers == "4" or "four":
        print("Correct! None of these were red lightsabers as well.")
        total_score += 20
        print("Your score is ", total_score)
        print("You have missed ", questions_missed, " questions.")

    else:
        print("Shockingly he had 4!")
        questions_missed += 1
        print("You have missed ", questions_missed, " questions.")

# question 12


def yoda_animal():
    global question
    global questions_missed
    global total_score
    print("Question ", question)
    question += 1
    print("What animal nearly played Yoda?")
    print("A) Bear\n"
          "B) Cat\n"
          "C) Monkey\n"
          "D) Eagle")
    monkey_yoda = input("Enter your choice ")
    if monkey_yoda.lower() == "c":
        print("Congratulations! That would have been a chaotic set!")
        total_score += 20
        print("Your score is ", total_score)
        print("You have missed ", questions_missed, " questions.")

    else:
        print("No, Yoda was about to be played by a monkey!")
        questions_missed += 1
        print("You have missed ", questions_missed, " questions.")

# question 13


def younglings_death():
    global question
    global questions_missed
    global total_score
    print("Question ", question)
    question += 1
    print("What did the younglings say before Anakin killed them?")
    print("A) Master Skywalker there are too many of them!\n"
          "B) What are we going to do?\n"
          "C) Master Skywalker there are too many of them! What are we going to do?\n"
          "D) What are we going to do? Master Skywalker there are too many of them!")
    kid_death = input("Enter your choice ")
    if kid_death.lower() == "c":
        print("Congratulations! These were Sors Bandeam's last words")
        total_score += 20
        print("Your score is ", total_score)
        print("You have missed ", questions_missed, " questions.")
    else:
        print("No they said,'Master Skywalker there are too many of them! What are we going to do?'")
        questions_missed += 1
        print("You have missed ", questions_missed, " questions.")

# question 14


def temple_location():
    global question
    global questions_missed
    global total_score
    print("Question ", question)
    question += 1
    print("Which is not a temple location for the jedi order? ")
    print("A) Coruscant\n"
          "B) Endor\n"
          "C) Ossus\n"
          "D) Tython")
    temple_planets = input("Enter your choice ")
    if temple_planets.lower() == "b":
        print("Congratulations! There are a total of 4")
        total_score += 20
        print("Your score is ", total_score)
        print("You have missed ", questions_missed, " questions.")

    else:
        print("No, there is no temple on Endor.")
        questions_missed += 1
        print("You have missed ", questions_missed, " questions.")

# question 15


def palpatine_granddaughter():
    global question
    global questions_missed
    global total_score
    print("Question ", question)
    question += 1
    rey_p = input("Who is Senator Palpatine's Granddaughter? ")
    if rey_p.lower() == "rey":
        print("That is correct!")
        total_score += 20
        print("Your score is ", total_score)
        print("You have missed ", questions_missed, " questions.")

    else:
        print("Sheev Palpatine's granddaughter is Rey.")
        questions_missed += 1
        print("You have missed ", questions_missed, " questions.")

# question 16


def height_dif():
    global question
    global questions_missed
    global total_score
    print("Question ", question)
    question += 1
    print("What is the height difference between Harrison Ford and Leia Organa?")
    print("A) 2 inches\n"
          "B) 6 inches\n"
          "C) 2 feet\n"
          "D) 1 foot")
    han_leia_height = input("Enter your choice ")
    if han_leia_height.lower() == "d":
        print("Congratulations! Carrie Fischer had to stand on a block!")
        total_score += 20
        print("Your score is ", total_score)
        print("You have missed ", questions_missed, " questions.")

    else:
        print("No there was a 1 foot height difference.")
        questions_missed += 1
        print("You have missed ", questions_missed, " questions.")

# question 17


def r2d2_height():
    global question
    global questions_missed
    global total_score
    print("Question ", question)
    question += 1
    print("How tall is R2D2?")
    print("A) 0.96m\n"
          "B) 1.4m\n"
          "C) 2.0m\n"
          "D) 0.46m")
    r2_height = input("Enter your choice ")
    if r2_height.lower() == "a":
        print("Congratulations! R2D2 is the best droid.")
        total_score += 20
        print("Your score is ", total_score)
        print("You have missed ", questions_missed, " questions.")

    else:
        print("No, R2D2 was 0.96m tall.")
        questions_missed += 1
        print("You have missed ", questions_missed, " questions.")

# question 18


def maul_apprentice():
    global question
    global questions_missed
    global total_score
    print("Question ", question)
    question += 1
    print("Who was Darth Maul's apprentice")
    print("A) Watto\n"
          "B) Savage Opress\n"
          "C) Boba Fett\n"
          "D) Yoda")
    maul_brother = input("Enter your choice ")
    if maul_brother.lower() == "b":
        print("Congratulations! Savage Opress was also his brother.")
        total_score += 20
        print("Your score is ", total_score)
        print("You have missed ", questions_missed, " questions.")

    else:
        print("Savage Opress was his apprentice and brother")
        questions_missed += 1
        print("You have missed ", questions_missed, " questions.")

# question 19


def yoda_age():
    global question
    global questions_missed
    global total_score
    print("Question ", question)
    question += 1
    yoda_age = input("How old was Yoda when he died? ")
    if yoda_age == ("900"):
        print("Congratulations, he died at an old age")
        total_score += 20
        print("Your score is ", total_score)
        print("You have missed ", questions_missed, " questions.")

    else:
        print("He died when he was 900")
        questions_missed += 1
        print("You have missed ", questions_missed, " questions.")

# question 20


def credit_dept():
    global question
    global questions_missed
    global total_score
    print("Question ", question)
    question += 1
    print("What was Han Solo’s overall dept to Jabba?")
    print("A) 22,000 credits\n"
          "B) 3,190 credits\n"
          "C) 21,090 credits\n"
          "D) 14,260 credits")
    credits_owed = input("Enter your choice ")
    if credits_owed.lower() == ("d"):
      print("Congratulations! He was not very responsible")
      total_score += 20
      print("Your score is ", total_score)
      print("You have missed ", questions_missed, " questions.")


    else:
      print("No, he had a dept of 14,260 credits")
      questions_missed += 1
      print("You have missed ", questions_missed, " questions.")

# question 21


def qgj_death():
    global question
    global questions_missed
    global total_score
    print("Question ", question)
    question += 1
    print("Who killed Qui Gon Jinn?")
    print("A) Anakin Skywalker\n"
          "B) Rex\n"
          "C) Sheev Palpatine\n"
          "D) Darth Maul")
    death_of_qgj = input("Enter your choice ")
    if death_of_qgj.lower() == ("d"):
      print("Congratulations! Sadly he was killed by Darth Maul")
      total_score += 20
      print("Your score is ", total_score)
      print("You have missed ", questions_missed, " questions.")

    else:
      print("No, Darth Maul had a life goal of killing him")
      questions_missed += 1
      print("You have missed ", questions_missed, " questions.")

# question 22


def anakin_owner():
    global question
    global questions_missed
    global total_score
    print("Question ", question)
    question += 1
    print("What is the Toydarian’s name who owned Anakin Skywalker? ")
    print("A) Watto\n"
          "B) Chewbacca\n"
          "C) Darth Sidious\n"
          "D) Barara")
    anakin_toydarian = input("Enter your choice ")
    if anakin_toydarian.lower() == ("a"):
      print("Congratulations! He was owned by Watto")
      total_score += 20
      print("Your score is ", total_score)
      print("You have missed ", questions_missed, " questions.")

    else:
      print("No, Watto owned him and his mother")
      questions_missed += 1
      print("You have missed ", questions_missed, " questions.")


# Make audio function

theme = arcade.load_sound("1-02 Main Title_Rebel Blockade Runne.mp3")
arcade.play_sound(theme)


# Play functions
intro()
my_list = [han_death, movie_count, george_lucas, lucas_net_worth, species,
           stormtrooper_number, shared_scenes, skywalker_mother, leia_luke,
           arm_colour, general_grevious,yoda_animal, younglings_death, temple_location,
           palpatine_granddaughter, height_dif, r2d2_height, maul_apprentice,yoda_age,
           credit_dept, qgj_death,anakin_owner]

num_questions = random.randint(7, 22)
questions_seen = [-1]*num_questions
for i in range(num_questions):
    repeat = False
    question_num = random.randint(0, 22)
    for qq in range(num_questions):
        if question_num == questions_seen[qq]:
            repeat = True
    if repeat == False:
        my_list[question_num]()
        questions_seen[i] = question_num
    else:
        i -=1


arcade.open_window(800, 350, "Star Wars")
arcade.set_background_color(arcade.csscolor.BLACK)
def final_stars(x,y):
    arcade.draw_circle_filled(x, y, 3, arcade.csscolor.WHITE_SMOKE)

    # stars at 100
for x in range(25):
    final_stars(75+x*25,100)
    # stars at 150
for x in range(9):
    final_stars(75+x*25,150)
for x in range(9):
    final_stars(525+x*25,150)

    # stars at 200
for x in range(9):
    final_stars(75+x*25,200)
for x in range(9):
    final_stars(525+x*25,200)

    # circles at 250
for x in range(25):
    final_stars(75+x*25,250)

    # circles at 300
for x in range(25):
    final_stars(75+x*25,300)

    # circles 450
for x in range(25):
    final_stars(75+x*25,50)

arcade.draw_text("Congratulations!\n" +
                 "You finished the game!\n" +
                 "You are a Star Wars buff!",
                 300, 150,
                 arcade.color.YELLOW, 17)
arcade.finish_render()

arcade.run()