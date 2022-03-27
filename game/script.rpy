# The script of the game

define M = Character("Milicent")
define B = Character("Blake")
define L = Character("Lavender")
define C = Character("Curtis")
define E = Character("Curtis's Friend")
define D = Character("Dean")

image blake angry:
    "./images/blake_angry.png"

image blake embarrassed:
    "./images/blake_embrrassed.png"

image blake neutral:
    "./images/blake_neutral.png"

image blake question:
    "./images/blake_question.png"

image blake sad:
    "./images/blake_sad.png"

image blake surprised:
    "./images/blake_surprised.png"

image curtis embarrassed:
    "./images/curtis_embarrassed.png"

image curtis neutral:
    "./images/curtis_neutral.png"

image curtis question:
    "./images/curtis_neutral.png"  

image curtis surprised:
    "./images/curtis_surprised.png"

image dean:
    "./images/dean moment.png"

image egg:
    "./images/egg.png"

image lavendar angry:
    "./images/lavender_angry.png"

image lavendar happy:
    "./images/lavender_happy.png"

image lavender neutral:
    "./images/lavender_neutral.png"

image lavender question:
    "./images/lavender_question.png"

image lavender surprised:
    "./images/lavender_question.png"

image milicent happy:
    "./images/milicent_happy.png"

image milicent embarrassed:
    "./images/milicent_embarrassed.png"

image milicent neutral:
    "./images/milicent_neutral.png"

image milicent question:
    "./images/milicent_questions.png"

image milicent sad:
    "./images/milicent_sad.png"

image milicent surprised:
    "./images/milicent.surprised.png"

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
    "./images/intro_2.jpg"

image intro 3:
    "./images/intro_3.png"

image intro 4:
    "./images/intro_4.jpg"

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

    scene intro 1 with dissolve

    ""

    scene intro 2 with dissolve

    ""

    scene intro 3 with dissolve

    ""

    scene intro 4 with dissolve

    ""

    scene intro 5 with dissolve

    ""

    scene intro 6 with dissolve

    ""

    scene intro 7 with dissolve

    ""

    scene intro 8 with dissolve

    ""

    jump hallway
