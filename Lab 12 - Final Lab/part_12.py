
def intro():
    # Welcome statement
    print("Welcome to my Final Project! \n"
          "In this project I will be quizzing you on Star Wars trivia!")
def main():
    # variables
    total_score = 0
    questions_missed = 0
    question = 1
    # question 1

    while True:
        print ("Question",question)
        question +=1
        print("In what movie did Han Solo die?")
        print("A) The Phantom Menace \n"
              "B) The Force Awakens \n"
              "C) Rise of Skywalker \n"
              "D) Return of the Jedi \n ")
        game_choice = input("Enter your choice: ")
        if game_choice.lower() == "b":
            print("Congratulations, you got the question right!\n"
                  "Unfortunately  he was stabbed by his son with a lightsaber.")
            total_score += 20
            print("Your new score is ", total_score)
            break
        else:
            print("The correct answer is D")
            questions_missed += 1
            print("You have missed ", questions_missed, " questions")
            break
       # Question 2
        print("Question ", question)
        question += 1
        total_movies = input("How many Star Wars movies are there?")
        if total_movies == "9":
            print("Nice job!")
            total_score += 20
            print("Your new score is", total_score)
            break
        else:
            print("There are 9 movies, Rouge One is a movie but does not follow the timeline.")
            print("Your current score is:", total_score)
            questions_missed += print("You have missed ", questions_missed, " questions")
            break
        # break
        print("Question ", question)
        # question 3
        question += 1
        print("Why did George Lucas sell the Star Wars franchise to Disney?")
        print("A) He wanted to spend time with his family and raise his daughter \n"
              "B) He was tired of the Star Wars fandom \n" 
              "C) He had some scripts written for the next trilogy but was too tired to direct them \n" 
              "D) He was stressed about movie reactions")
        input("Enter  your choice:")
        if game_choice.lower() == ("a"):
            print("Congratulations! He wanted to spend time with his family.")
            total_score += 20
            print("Your score is ", total_score)
            break
        else:
            print("He sold the franchise to spend time with his family")
            questions_missed += 1
            print("You have missed ", questions_missed, " questions.")
            break
        # question 4
        print("Question ", question)
        question += 1
        net_worth == input("What is George Lucas's net worth?")
        if net_worth.lower() == ("7 billion USD"):
            print("That is correct!")
            total_score += 20
            print("Your new score is ", total_score)
            break
        else:
            print("His net worth is 7 billion USD")
            questions_missed += 1
            print("You have missed ", questions_missed, " questions")
            break
        # question 5
        print("Question ", question)
        question += 1
        print(" What species is Jar Jar Binks?")
        print("A) Toydarian\n"
              "B) Wookie\n"
              "C) Gungan\n"
              "D) Geonosian")
        input("Enter your game choice:")
        if game_choice.lower() == ("c"):
            print("Congratulations! Jar Jar Binks is from Naboo.")
            total_score += 20
            print("Your score is ", total_score)
            break

        else:
            print("No, Jar Jar Binks is a Gungan, while the others are other species of creatures from Star Wars")
            questions_missed += 1
            print("You have missed ", questions_missed, " questions.")

        # question 6
        print("Question ", question)
        question += 1
        print("What is Finn's Stormtrooper number?")
        print("A) TK-421\n"
              "B) CT-7567\n"
              "C) CC-2224\n"
              "D) FN-2187")
        input("Enter your game choice:")
        if game_choice.lower() == ("d"):
            print("Congratulations! The others are from the movies or Clone Wars.")
            total_score += 20
            print("Your score is ", total_score)
            break

        else:
            print("No, Finn's number was FN-2187, Poe gave Finn as a name to him")
            questions_missed += 1
            print("You have missed ", questions_missed, " questions.")

        # question 7
        print("Question ", question)
        question += 1
        scenes_shared == input("How many scenes did Darth Vader and C-3PO share? ")
        if scenes_shared == 1:
            print("Correct! This scene was in The Empire Strikes back.")
            total_score += 20
            print("Your score is ", total_score)
            break
        else:
            print("Shockingly there was only 1 scene!")
            questions_missed += 1
            print("You have missed ", questions_missed, " questions.")

        # question 8
        print("Question ", question)
        question += 1
        print("Who is Anakin Skywalkers mother?")
        print("A) Leia Skywalker\n"
              "B) Satine Kryze\n"
              "C) Maz Kanata\n"
              "D) Shimi Skywalker")
        input("Enter your choice")
        if game_choice.lower() == "d":
            print("Congratulations! Shimi Skywalker is Anakin's mother")
            total_score += 20
            print("Your score is ", total_score)
            break

        else:
            print("Shimi Skywalker is Anakin's mother")
            questions_missed += 1
            print("You have missed ", questions_missed, " questions.")
            break
        # question 9
        print("Question ", question)
        question += 1
        twins == input("Were Leia and Luke twins? ")
        if twins.lower() == ("yes"):
            print("Correct! They were twins of Padme Amidala.")
            total_score += 20
            print("Your score is ", total_score)
            break
        else:
            print("They were twins.")
            questions_missed += 1
            print("You have missed ", questions_missed, " questions.")
            break
        # question 10
        print("Question ", question)
        question += 1
        print("What colour is C-3PO’s arm in the force awakens?")
        print("A) Red\n"
              "B) Purple\n"
              "C) Gold\n"
              "D) Green")
        input("Enter your choice")
        if game_choice.lower() == ("a"):
            print("Congratulations! C-3PO's arm was red.")
            total_score += 20
            print("Your score is ", total_score)
            break

        else:
            print("No, C-3PO's arm was red in The Force Awakens")
            questions_missed += 1
            print("You have missed ", questions_missed, " questions.")
            break

        # question 11
        print("Question ", question)
        question += 1
        grevious_lightsabers == input("How many light sabers did General Grevious have? ")
        if scenes_shared == 4:
            print("Correct! None of these were red lightsabers as well.")
            total_score += 20
            print("Your score is ", total_score)
            break
        else:
            print("Suprisingly he had 4!")
            questions_missed += 1
            print("You have missed ", questions_missed, " questions.")
            break
        # question 12
        print("Question ", question)
        question += 1
        print("What animal nearly played Yoda?")
        print("A) Bear\n"
              "B) Cat\n"
              "C) Monkey\n"
              "D) Eagle")
        input("Enter your choice")
        if game_choice.lower() == ("c"):
            print("Congratulations! That would have been a chaotic set!")
            total_score += 20
            print("Your score is ", total_score)
            break

        else:
            print("No, Yoda was about to be played by a monkey!")
            questions_missed += 1
            print("You have missed ", questions_missed, " questions.")
            break
        # question 13
        print("Question ", question)
        question += 1
        pritn("What did the younglings say before Anakin killed them?")
        print("A) Master Skywalker there are too many of them!\n"
              "B) What are we going to do?\n"
              "C) Master Skywalker there are too many of them! What are we going to do?\n"
              "D) What are we going to do? Master Skywalker there are too many of them!")
        input("Enter your choice")
        if game_choice.lower() == ("c"):
            print("Congratulations! These were Sors Bandeam's last words")
            total_score += 20
            print("Your score is ", total_score)
            break

        else:
            print("No they said,'Master Skywalker there are too many of them! What are we going to do?'")
            questions_missed += 1
            print("You have missed ", questions_missed, " questions.")
            break

        # question 14
        print("Question ", question)
        question += 1
        print("Which is not a temple location for the jedi order?")
        print("A) Coruscant\n"
              "B) Endor\n"
              "C) Ossus\n"
              "D) Tython")
        input("Enter your choice")
        if game_choice.lower() == ("b"):
            print("Congratulations! There are a total of 4")
            total_score += 20
            print("Your score is ", total_score)
            break

        else:
            print("No, there is no temple on Endor.")
            questions_missed += 1
            print("You have missed ", questions_missed, " questions.")
            break
        # question15
        print("Question ", question)
        question += 1
        rey_p == input("Who is Senator Palpatine's Granddaughter?")
        if rey_p.lower() == ("Rey"):
            print("That is correct!")
            total_score += 20
            print("Your score is ", total_score)
            break
        else:
            print("Sheev Palpatine's granddaughter is Rey.")
            questions_missed += 1
            print("You have missed ", questions_missed, " questions.")
            break
        # question 16
        print("Question ", question)
        question += 1
        print("What is the height difference between Harrison Ford and Leia Organa?")
        print("A) 2 inches\n"
              "B) 6 inches\n"
              "C) 2 feet\n"
              "D) 1 foot")
        input("Enter your choice")
        if game_choice.lower() == ("d"):
            print("Congratulations! Carrie Fischer had to stand on a block!")
            total_score += 20
            print("Your score is ", total_score)
            break

        else:
            print("No there was a 1 foot height difference.")
            questions_missed += 1
            print("You have missed ", questions_missed, " questions.")
            break
        # question 17
        print("Question ", question)
        question += 1
        print("How tall is R2D2?")
        print("A) 0.96m\n"
              "B) 1.4m\n"
              "C) 2.0m\n"
              "D) 0.46m")
        input("Enter your choice")
        if game_choice.lower() == ("a"):
            print("Congratulations! R2D2 is the best droid.")
            total_score += 20
            print("Your score is ", total_score)
            break

        else:
            print("No, R2D2 was 0.96m tall.")
            questions_missed += 1
            print("You have missed ", questions_missed, " questions.")
            break
        # question 18
        print("Question ", question)
        question += 1
        print("Who was Darth Maul's apprentice")
        print("A) Watto"
              "B) Savage Opress"
              "C) Boba Fett"
              "D) Yoda")
        input("Enter your choice")
        if game_choice.lower() == ("b"):
            print("Congratulations! Savage Opress was also his brother.")
            total_score += 20
            print("Your score is ", total_score)
            break

        else:
            print("Savage Opress was his apprentice and brother")
            questions_missed += 1
            print("You have missed ", questions_missed, " questions.")
            break
        # question 19
        print("Question ", question)
        question += 1
        print("How old was Yoda when he died? ")
        if yoda_age == ("900"):
            print("Congratulations, he died at an old age")
            total_score += 20
            print("Your score is ", total_score)
            break
        else:
            print("He died when he was 900")
            questions_missed += 1
            print("You have missed ", questions_missed, " questions.")
            break
        # question 20
        print("Question ", question)
        question += 1
        print("What was Han Solo’s overall dept to Jabba?")
        print("A) 22,000 credits\n"
              "B) 3,190 credits\n"
              "C) 21,090 credits\n"
              "D) 14,260 credits")
        input("Enter your choice")
        if game_choice.lower() == ("d"):
            print("Congratulations! He was not very responsible")
            total_score += 20
            print("Your score is ", total_score)
            break

        else:
            print("No, he had a dept of 14,260 credits")
            questions_missed += 1
            print("You have missed ", questions_missed, " questions.")
            break
        # question 21
        print("Question ", question)
        question += 1
        print("Who killed Qui Gon Jinn?")
        print("A) Anakin Skywalker\n"
              "B) Rex\n"
              "C) Sheev Palpatine\n"
              "D) Darth Maul")
        if game_choice.lower() == ("d"):
            print("Congratulations! Sadly he was killed by Darth Maul")
            total_score += 20
            print("Your score is ", total_score)
            break

        else:
            print("No, Darth Maul had a life goal of killing him")
            questions_missed += 1
            print("You have missed ", questions_missed, " questions.")
            break
        # question 22
        print("Question ", question)
        question += 1
        print("What is the Toydarian’s name who owned Anakin Skywalker? ")
        print("A) Watto\n"
              "B) Chewbacca\n"
              "C) Darth Sidious\n"
              "D) Barara")
        if game_choice.lower() == ("a"):
            print("Congratulations! He was owned by Watto")
            total_score += 20
            print("Your score is ", total_score)
            break

        else:
            print("No, Watto owned him and his mother")
            questions_missed += 1
            print("You have missed ", questions_missed, " questions.")
            break

# Make graphic function
import arcade

arcade.open_window(800, 350, "Star Wars")
arcade.set_background_color(arcade.csscolor.BLACK)
arcade.start_render()

# function for the circles
def final_stars(x,y):
    arcade.draw_circle_filled(x, y, 3, arcade.csscolor.WHITE_SMOKE)
    arcade.draw_text("Congratulations!\n"+
                     "You finished the game!\n" +
                    "You are a Star Wars buff!",
                    300, 150,
                    arcade.color.YELLOW, 17)
# stars at 100
final_stars(75,100)
final_stars(100,100)
final_stars(125,100)
final_stars(150,100)
final_stars(175,100)
final_stars(200,100)
final_stars(225,100)
final_stars(250,100)
final_stars(275,100)
final_stars(300,100)
final_stars(325,100)
final_stars(350,100)
final_stars(375,100)
final_stars(400,100)
final_stars(425,100)
final_stars(450,100)
final_stars(475,100)
final_stars(500,100)
final_stars(525,100)
final_stars(550,100)
final_stars(575,100)
final_stars(600,100)
final_stars(625,100)
final_stars(650,100)
final_stars(675,100)
final_stars(700,100)
final_stars(725,100)

# stars at 150
final_stars(75,150)
final_stars(100,150)
final_stars(125,150)
final_stars(150,150)
final_stars(175,150)
final_stars(200,150)
final_stars(225,150)
final_stars(250,150)
final_stars(275,150)
final_stars(525,150)
final_stars(550,150)
final_stars(575,150)
final_stars(600,150)
final_stars(625,150)
final_stars(650,150)
final_stars(675,150)
final_stars(700,150)
final_stars(725,150)

# pacman circles at 200
final_stars(75,200)
final_stars(100,200)
final_stars(125,200)
final_stars(150,200)
final_stars(175,200)
final_stars(200,200)
final_stars(225,200)
final_stars(250,200)
final_stars(275,200)
final_stars(525,200)
final_stars(550,200)
final_stars(575,200)
final_stars(600,200)
final_stars(625,200)
final_stars(650,200)
final_stars(675,200)
final_stars(700,200)
final_stars(725,200)

# circles at 250
final_stars(75,250)
final_stars(100,250)
final_stars(125,250)
final_stars(150,250)
final_stars(175,250)
final_stars(200,250)
final_stars(225,250)
final_stars(250,250)
final_stars(275,250)
final_stars(300,250)
final_stars(325,250)
final_stars(350,250)
final_stars(375,250)
final_stars(400,250)
final_stars(425,250)
final_stars(450,250)
final_stars(475,250)
final_stars(500,250)
final_stars(525,250)
final_stars(550,250)
final_stars(575,250)
final_stars(600,250)
final_stars(625,250)
final_stars(650,250)
final_stars(675,250)
final_stars(700,250)
final_stars(725,250)

# circles at 300
final_stars(75,300)
final_stars(100,300)
final_stars(125,300)
final_stars(150,300)
final_stars(175,300)
final_stars(200,300)
final_stars(225,300)
final_stars(250,300)
final_stars(275,300)
final_stars(300,300)
final_stars(325,300)
final_stars(350,300)
final_stars(375,300)
final_stars(400,300)
final_stars(425,300)
final_stars(450,300)
final_stars(475,300)
final_stars(500,300)
final_stars(525,300)
final_stars(550,300)
final_stars(575,300)
final_stars(600,300)
final_stars(625,300)
final_stars(650,300)
final_stars(675,300)
final_stars(700,300)
final_stars(725,300)

# circles 450
final_stars(75, 50)
final_stars(100,50)
final_stars(125,50)
final_stars(150,50)
final_stars(175,50)
final_stars(200,50)
final_stars(225,50)
final_stars(250,50)
final_stars(275,50)
final_stars(300,50)
final_stars(325,50)
final_stars(350,50)
final_stars(375,50)
final_stars(400,50)
final_stars(425,50)
final_stars(450,50)
final_stars(475,50)
final_stars(500,50)
final_stars(525,50)
final_stars(550,50)
final_stars(575,50)
final_stars(600,50)
final_stars(625,50)
final_stars(650,50)
final_stars(675,50)
final_stars(700,50)
final_stars(725,50)


arcade.finish_render()

arcade.run()
# Make audio function

# Make shuffle question function

intro()
main()
final_stars()