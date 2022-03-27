# The script of the game

define M = Character("Milicent")
define B = Character("Blake")
define L = Character("Lavender")
define C = Character("Curtis")
define E = Character("Curtis's Friend")
define D = Character("Dean")

image blake angry:
    "./images/blake_angry.png"
    zoom 0.5

image blake embarrassed:
    "./images/blake_embrrassed.png"
    zoom 0.5

image blake neutral:
    "./images/blake_neutral.png"
    zoom 0.5

image blake question:
    "./images/blake_question.png"
    zoom 0.5

image blake sad:
    "./images/blake_sad.png"
    zoom 0.5

image blake surprised:
    "./images/blake_surprised.png"
    zoom 0.5

image curtis embarrassed:
    "./images/curtis_embarrassed.png"
    zoom 0.5

image curtis neutral:
    "./images/curtis_neutral.png"
    zoom 0.5

image curtis question:
    "./images/curtis_neutral.png"
    zoom 0.5    

image curtis surprised:
    "./images/curtis_surprised.png"
    zoom 0.5

image dean:
    "./images/dean moment.png"
    zoom 0.5

image egg:
    "./images/egg.png"
    zoom 0.5

image lavendar angry:
    "./images/lavender_angry.png"
    zoom 0.5

image lavendar happy:
    "./images/lavender_happy.png"
    zoom 0.5

image lavender neutral:
    "./images/lavender_neutral.png"
    zoom 0.5

image lavender question:
    "./images/lavender_question.png"
    zoom 0.5

image lavender surprised:
    "./images/lavender_question.png"
    zoom 0.5

image milicent happy:
    "./images/milicent_happy.png"
    zoom 0.5

image milicent embarrassed:
    "./images/milicent_embarrassed.png"
    zoom 0.5

image milicent neutral:
    "./images/milicent_neutral.png"
    zoom 0.5

image milicent question:
    "./images/milicent_questions.png"
    zoom 0.5

image milicent sad:
    "./images/milicent_sad.png"
    zoom 0.5

image milicent surprised:
    "./images/milicent.surprised.png"
    zoom 0.5

image potion empty:
    "./images/potion empty.png"
    zoom 0.5

image potion full:
    "./images/potion full.png"
    zoom 0.5

image potion half full:
    "./images/potion half full.png"
    zoom 0.5

image school hallway:
    "./images/school hallway.png"

image time swirl 1:
    "./images/time_swirl_1.png"

image time swirl 2:
    "./images/time_swirl_2.png"

image time swirl 3:
    "./imagse/time_swirl_3.png"

image locket closed:
    "./images/locket closed.png"
    zoom 0.5

image locket open:
    "./images/locket open.png"
    zoom 0.5

image intro 1:
    "./images/intro_1.png"

image intro 2:
    "./images/intro_2.png"

image intro 3:
    "./images/intro_3.png"

image intro 4:
    "./images/intro_4.png"

image intro 5:
    "./images/intro_5.png"

image intro 6:
    "./images/intro_6.png"

image intro 7:
    "./images/intro_7.png"

image intro 8:
    "./images/intro_8.png"
    

image background_botony:
    "./images/botanyclass(1).png"

define audio.general = "./audio/e_woven.m4a"

label start:

    $ user = renpy.input("What is your name?")
    $ user = user.strip()

    if not user:
        $ user = "Julia"

    # scene background_botony

    jump hallway
