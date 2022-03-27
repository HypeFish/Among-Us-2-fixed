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
