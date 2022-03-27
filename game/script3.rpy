label potion1:

    play sound audio.bell

    M "Quick [user], drink the potion!"

    user "See you soon professor!"

    "You drink the potion, it's thick like cough syrup. Tastes like cough syrup too."

    "You're creating to wonder if Milicent has given you cough syrup when the room starts to get dizzy."

    scene hallway half

    "The school bell rings once signaling to everyone that there’s 30 minutes before the first period. You grab your bag and sling it over your shoulder."

    "Yeah it’s a little early to be arriving to first period but you like speaking to the botany teac-"

    "holy shit it worked. You look down at your arms, you almost expect to be a ghost."

    "Turns out... you are not a ghost."

    "Yet." with hpunch

    "You quickly turn around retracing your steps."

    show lavender happy with dissolve

    "There's Lavender."

    hide lavender happy with dissolve

    show blake angry with dissolve

    "There's Blake."

    hide blake angry with dissolve

    show curtis neutral with dissolve

    "There's Curtis."

    hide curtis neutral with dissolve

    "And there's the botany classroom. You hurry inside."

    user "Milicent?"

    show milicent surprised with dissolve

    M "[user]!"

    "She sees the bottle in your hands"

    show milicent happy with dissolve

    M " I see, you’ve agreed to solve the mystery for me."

    user "Yes I have, now I need you to leave. I need more time to investigate the room."

    "Milicent nods."

    "Wow she really does believe in you. She turns and leaves."

    hide milicent happy with dissolve

    "You continue to scan the room. You have already gotten the plants and the walls and the windows."

    "Your eyes then move the floor, you get down on your hands and knees to take a better look when."

    "*click*" 

    "You hear the door open. You peak around the desh your huddled under to see..."

    show curtis embarrassed with dissolve

    " Curtis, who is even more red than normal. He shuffles around, looking under the desks until he comes to your desk"

    show curtis surprised with dissolve

    C "AH!"

    user "AH!"

    C "Hi! Uh!"

    "You stand up. Curtis is a couple inches taller than you but that doesn't mean he'll be able to escape your questions."

    menu:
        "What are you doing here right now?":
            $ y = "1"
            C "so I lost my reed for my clarinet and i thin-"
            user "I’m sorry, what are you saying?"
            C "I lost my re-"
            user "I still can't hear you."
            C "I LOST MY REED FOR MY CLARINET AND IT WAS REALLY EMBARRASSING TO GO TO BAND REHEARSAL WITHOUT IT AND IT'S EMBARRASSING NOW CAUSE I NEED TO FIND IT BEFORE THE CONCERT."
            "Is he gonna cry?"
            C "Practice ran till 8 *sniff* I pretended to play the clarinet the whole time. It was awful"
            "You scan the floor, you see a small wooden rectangle under one of the desks that Curtis had passed before."
            user "Ah! Here it is."
            show curtis neutral with dissolve
            C "Oh thanks"
            "Hm so the reed was in here. He could have dropped it when he said he did, or in the heat of the crime OR when he saw I was in here he could have dropped it when he saw that I was in here investigating to cove his tracks."
            "Oh Oh Oh the game is a foot Mr. Curtis, the game is a foot."
            show curtis question with dissolve
            C "Are you okay? You look a little dazed"
            user "Oh I’m okay"
            "The question dear Curtis is are you guilty!!"

        "What were you doing yesterday?":
            $ y = "2"
            C "Okay so I,"
            C "Okay so."
            C "I was at band practice and I didnt have my reed."
            C "I didn't have my reed and the concert is coming up."
            "Jesus can he get to the point."
            C "So I just kind sat there pretending to play, just like doing the fingerings with no sound coming out."
            C "God it was so embarrassing"
            "You’d put a hand on his shoulder to comfort him…but he looks really spiky…best not risk it"

        "What did you think about the plant?":
            $ y = "3"
            hide curtis question with dissolve
            C "Uh what plant."
            "You gesture with your head to where the satis curae should be"
            show curtis surprised with dissolve
            C "Oh! You mean the big plant with the     petals and the leaves and the…"
            user "Yeah the one that is usually right there"
            show curtis neutral with dissolve
            C "Uh can't really say that I think about it, much at all. It’s a plant"

    user "*What else can I ask?*"

    if y == "1":
        menu:
            "What were you doing yesterday?":
                $ y = "12"
                C "Okay so I,"
                C "Okay so."
                C "I was at band practice and I didnt have my reed."
                C "I didn't have my reed and the concert is coming up."
                "Jesus can he get to the point."
                C "So I just kind sat there pretending to play, just like doing the fingerings with no sound coming out."
                C "God it was so embarrassing"
                "You’d put a hand on his shoulder to comfort him…but he looks really spiky…best not risk it"

            "What did you think about the plant?":
                $ y = "13"
                hide curtis question with dissolve
                C "Uh what plant."
                "You gesture with your head to where the satis curae should be"
                show curtis surprised with dissolve
                C "Oh! You mean the big plant with the     petals and the leaves and the…"
                user "Yeah the one that is usually right there"
                show curtis neutral with dissolve
                C "Uh can't really say that I think about it, much at all. It’s a plant"

    if y == "2":
        menu:
            "What are you doing here right now?":
                $ y = "12"
                C "so I lost my reed for my clarinet and i thin-"
                user "I’m sorry, what are you saying?"
                C "I lost my re-"
                user "I still can't hear you."
                C "I LOST MY REED FOR MY CLARINET AND IT WAS REALLY EMBARRASSING TO GO TO BAND REHEARSAL WITHOUT IT AND IT'S EMBARRASSING NOW CAUSE I NEED TO FIND IT BEFORE THE CONCERT."
                "Is he gonna cry?"
                C "Practice ran till 8 *sniff* I pretended to play the clarinet the whole time. It was awful"
                "You scan the floor, you see a small wooden rectangle under one of the desks that Curtis had passed before."
                user "ah! Here it is."
                show curtis neutral with dissolve
                C "Oh thanks"
                "Hm so the reed was in here. He could have dropped it when he said he did, or in the heat of the crime OR when he saw I was in here he could have dropped it when he saw that I was in here investigating to cove his tracks."
                "Oh Oh Oh the game is a foot Mr. Curtis, the game is a foot."
                show curtis question with dissolve
                C "Are you okay? You look a little dazed"
                user "Oh I’m okay"
                "The question dear Curtis is are you guilty!!"

            "What did you think about the plant?":
                $ y = "23"
                hide curtis question with dissolve
                C "Uh what plant."
                "You gesture with your head to where the satis curae should be"
                show curtis surprised with dissolve
                C "Oh! You mean the big plant with the     petals and the leaves and the…"
                user "Yeah the one that is usually right there"
                show curtis neutral with dissolve
                C "Uh can't really say that I think about it, much at all. It’s a plant"

    if y == "3":
        menu:
            "What are you doing here right now?":
                $ y = "13"
                C "So I lost my reed for my clarinet and i thin-"
                user "I’m sorry, what are you saying?"
                C "I lost my re-"
                user "I still can't hear you."
                C "I LOST MY REED FOR MY CLARINET AND IT WAS REALLY EMBARRASSING TO GO TO BAND REHEARSAL WITHOUT IT AND IT'S EMBARRASSING NOW CAUSE I NEED TO FIND IT   BEFORE THE CONCERT."
                "Is he gonna cry?"
                "You scan the floor, you see a small wooden rectangle under one of the desks that Curtis had passed before."
                user "Ah! Here it is."
                show curtis neutral with dissolve
                C "Oh thanks"
                "Hm so the reed was in here. He could have dropped it when he said he did, or in the heat of the crime OR when he saw I was in here he could have dropped it when he saw that I was in here investigating to cove his tracks."
                "Oh Oh Oh the game is a foot Mr. Curtis, the game is a foot."
                show curtis question with dissolve
                C "Are you okay? You look a little dazed"
                user "Oh I’m okay"
                "The question dear Curtis is are you guilty!!"

            "What were you doing yesterday?":
                $ y = "23"
                C "Okay so I,"
                C "Okay so."
                C "I was at band practice and I didnt have my reed."
                C "I didn't have my reed and the concert is coming up."
                "Jesus can he get to the point."
                C "So I just kind sat there pretending to play, just like doing the fingerings with no sound coming out."
                C "God it was so embarrassing"
                "You’d put a hand on his shoulder to comfort him…but he looks really spiky…best not risk it"

    user "*What else can i ask?*"

    if y == "13":
        menu:
            "What were you doing yesterday?":
                C "Okay so I,"
                C "Okay so."
                C "I was at band practice and I didnt have my reed."
                C "I didn't have my reed and the concert is coming up."
                "Jesus can he get to the point."
                C "So I just kind sat there pretending to play, just like doing the fingerings with no sound coming out."
                C "God it was so embarrassing"
                "You’d put a hand on his shoulder to comfort him…but he looks really spiky…best not risk it"

    if y == "12":
        menu:
            "What did you think about the plant?":
                show curtis question with dissolve
                C "Uh what plant."
                "You gesture with your head to where the satis curae should be"
                show curtis surprised with dissolve
                C "Oh! You mean the big plant with the petals and the leaves and the…"
                user "Yeah the one that is usually right there"
                show curtis neutral with dissolve
                C "Uh can't really say that I think about it, much at all. It’s a plant"

    if y == "23":
        menu:
            "What are you doing here right now?":
                C "So I lost my reed for my clarinet and i thin-"
                user "I’m sorry, what are you saying?"
                C "I lost my re-"
                user "I still can't hear you."
                C "I LOST MY REED FOR MY CLARINET AND IT WAS REALLY EMBARRASSING TO GO TO BAND REHEARSAL WITHOUT IT AND IT'S EMBARRASSING NOW CAUSE I NEED TO FIND IT   BEFORE THE CONCERT."
                "Is he gonna cry?"
                C "Practice ran till 8 *sniff* I pretended to play the clarinet the whole time. It was awful"
                "You scan the floor, you see a small wooden rectangle under one of the desks that Curtis had passed before."
                user "Ah! Here it is."
                show curtis neutral with dissolve
                C "Oh thanks"
                "Hm so the reed was in here. He could have dropped it when he said he did, or in the heat of the crime OR when he saw I was in here he could have dropped it when he saw that I was in here investigating to cove his tracks."
                "Oh Oh Oh the game is a foot Mr. Curtis, the game is a foot."
                show curtis question with dissolve
                C "Are you okay? You look a little dazed"
                user "Oh I’m okay"
                "The question dear Curtis is are you guilty!!"

    show curtis neutral with dissolve
    C "uh, well, thank you for finding my reed…I gotta…I gotta go to class, we have a quiz in divination…"

    C "I’ll see you… See you later"

    hide curtis neutral with dissolve

    "Hmmmm. Curtis was in the building yesterday night, but he doesn’t seem to care about the plant. Like at all. Means without motive, hmmmmmm."

    "You go back to scanning the ground, a small glint of silver catches you eye. You bend down and grab a silver chain on the ground"

    "It’s a delicate necklace with a heart shaped pendant on the bottom with an L carved onto the front. What does the L stand for?"

    "The thief might have dropped it while trying to make their escape. You shove the necklace into your pocket."

    "You hear the door hand open again, as someone who often hangs out in the botany classroom it is never this busy in the morning."

jump blake_reveal
