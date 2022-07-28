#  MAD LIBS IS A PHRASAL TEMPLATE WORD GAME.
# In this, one player act like a reader and as the other player who hasn't seen the story to fill in the blanks with
# adjectives, verbs, nouns, etc. these words are inserted in the blanks and then the story is read aloud sounds
# hilarious. There are no winner or loser only laughter :)

#taking input from user
adj = input("Adjective : ")
verb1 = input("verb : ")
verb2 = input("verb : ")
famous_person = input("Famous person : ")

#filling the balnks w user inputs
madlib = f"Computer programming is so {adj}! It makes me so excited all the time because i love to " \
         f"{verb1}. Stay hydrated and {verb2} like your are {famous_person}"

#outputing the final result
print(madlib)