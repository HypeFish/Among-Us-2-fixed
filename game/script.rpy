# The script of the game

define M = Character("Milicent")
define B = Character("Blake")
define L = Character("Lavender")
define C = Character("Curtis")
define D = Character("Dean")

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
