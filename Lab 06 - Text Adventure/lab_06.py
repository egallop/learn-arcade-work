import arcade
total_score = 0
# Welcome statement
print("Welcome to the rock and roll pop culture Quiz")

# line break

print()
# question about REM
print ("Who wrote the song Losing my Religion in 1991? ")
print ("A) Judas Priest\n"
      "B) Pantera\n"  
      "C) R.E.M.\n"
       "D) Iron Maiden")
answer_REM = input("Enter your choice: ")

if answer_REM.lower() == "c":
    print("That is correct!")
    total_score += 20
    print("Your new score is", total_score)
else:
    print("The correct answer is R.E.M.")
    print("Your current score is:", total_score)

# line break
print()

# Rush question
answer_rush = input("How many studio albums has the Toronto based band, Rush, released? ")
if answer_rush == "19":
    print("Nice job!")
    total_score += 20
    print("Your new score is", total_score)
else:
    print("Try harder next time! ")
    print("Your current score is:", total_score)

# line break
print()

# Ozzy Osbourne
answer_ozzy = input("What year did Ozzy Osbourne bite the head of a bat off on stage?")
if answer_ozzy == "1982":
    print("Wow! nice job")
    total_score += 20
    print("Your new score is", total_score)
else:
    print("Probably best that you do not watch it here: https://www.youtube.com/watch?v=GeuW4Smf9PI ")
    print("Your current score is:", total_score)


# line break
print()

# question about Led Zeppelin
print ("What is the best Led Zeppelin song? ")
print ("A) Houses of The Holy\n"
      "B) Zeppelin IV\n"  
      "C) The Song Remains the Same\n"
       "D) In Through the Out Door \n")
answer_LZ = input("Enter your choice: ")

if answer_LZ.lower() == "b":
    print("You have amazing taste!")
    total_score += 20
    print("Your new score is", total_score)
else:
    print("Zeppelin IV is better")
    print("Your current score is:", total_score)

# line break
print()

# who does not belong
print ("Who does not belong? ")
print ("A) John Lennon\n"
      "B) Robert Plant\n"  
      "C) Angus Young\n"
       "D) Dave Grohl")
answer_WDNB = input("Enter your choice: ")

if answer_WDNB.lower() == "d":
    print("We still love you Dave!")
    total_score += 20
    print("Your new score is", total_score)
else:
    print("The correct answer is Dave is the only non-lead singer here")
    print("Your current score is:", total_score)

# final statements
print(" Good game, let's play again sometime! Your final score is:", total_score)
