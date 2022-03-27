label blake_reveal:
        
    show blake neutral with dissolve

    B "Dude what are you doing here?"

    "Whatever you do, don't say you’re solving a mystery"
    user "I’m solving a mystery"
    "Come on man"
    

    menu:
        "Where were you yesterday night?":
            $ x = "1"
            show blake angry with dissolve
            B "Are you asking for my alibi?" 
            B "Fuck"
            B "Off"
            "Your first uncooperative witness, you’re a real detective now."

        "What did you think of the plant?":
            $ x = "2"
            show blake angry with dissolve
            B "I don’t care about the stupid satus cureus"
            user "You mean the satis curae?"
            B "Whatever! What am I gonna do with an uber deadly plant? Kill someone?"
            "You gather from her expression that she wouldn't need a plant to kill someone."

        "Do you know who might want to steal the plant":
            $ x = "3"
            show blake angry with dissolve
            B "I don't know! Why don't you ask your little friend, what’s her name? Rose?"
            user "Lavender?"
            B "Yeah whatever, she's the president of the alchemy club, she’d know what to do with the scatu cares."
            user "The satis curae"
            B "WHATEVER! Point is that aside from Milicent she’s the only other person who would make use of the sat- the plant."

    user "*What else can I ask?*"

    if x == "1":
        menu:
            "What did you think of the plant?":
                $ x = "12"
                show blake angry with dissolve
                B "I don’t care about the stupid satus cureus"
                user "You mean the satis curae?"
                B "Whatever! What am I gonna do with an uber deadly plant? Kill someone?"
                "You gather from her expression that she wouldn't need a plant to kill someone."

            "Do you know who might want to steal the plant":
                $ x = "13"
                show blake angry with dissolve
                B "I don't know! Why don't you ask your little friend, what’s her name? Rose?"
                user "Lavender?"
                B "Yeah whatever, she's the president of the alchemy club, she’d know what to do with the scatu cares."
                user "The satis curae"
                B "WHATEVER! Point is that aside from Milicent she’s the only other person who would make use of the sat- the plant."

    if x == "2":
        menu:
            "Where were you yesterday night?":
                $ x = "12"
                show blake angry with dissolve
                B "Are you asking for my alibi?" 
                B "Fuck"
                B "Off"
                "Your first uncooperative witness, you’re a real detective now."

            "Do you know who might want to steal the plant":
                $ x = "23"
                show blake angry with dissolve
                B "I don't know! Why don't you ask your little friend, what’s her name? Rose?"
                user "Lavender?"
                B "Yeah whatever, she's the president of the alchemy club, she’d know what to do with the scatu cares."
                user "The satis curae"
                B "WHATEVER! Point is that aside from Milicent she’s the only other person who would make use of the sat- the plant."
        
    if x == "3":
        menu:
            "What did you think of the plant?":
                $ x = "23"
                show blake angry with dissolve
                B "I don’t care about the stupid satus cureus"
                user "You mean the satis curae?"
                B "Whatever! What am I gonna do with an uber deadly plant? Kill someone?"
                "You gather from her expression that she wouldn't need a plant to kill someone."

            "Where were you yesterday night?":
                $ x = "13"
                show blake angry with dissolve
                B "Are you asking for my alibi?" 
                B "Fuck"
                B "Off"
                "Your first uncooperative witness, you’re a real detective now."

    user "*What else can I ask?*"

    if x == "12":
        menu:
            "Where were you yesterday night?":
                show blake angry with dissolve
                B "Are you asking for my alibi?" 
                B "Fuck"
                B "Off"
                "Your first uncooperative witness, you’re a real detective now."

    if x == "13":
        menu:
            "What did you think of the plant?":
                show blake angry with dissolve
                B "I don’t care about the stupid satus cureus"
                user "You mean the satis curae?"
                B "Whatever! What am I gonna do with an uber deadly plant? Kill someone?"
                "You gather from her expression that she wouldn't need a plant to kill someone."

    if x == "23":
        menu:
            "Do you know who might want to steal the plant":
                show blake angry with dissolve
                B "I don't know! Why don't you ask your little friend, what’s her name? Rose?"
                user "Lavender?"
                B "Yeah whatever, she's the president of the alchemy club, she’d know what to do with the scatu cares."
                user "The satis curae"
                B "WHATEVER! Point is that aside from Milicent she’s the only other person who would make use of the sat- the plant."


    "Blake turns on her heels and walks out of the room, slamming the door behind her."

    "You think about what she said about Lavender. She wouldn’t do this would she?"

    "You remember that the alchemy club meets on Tuesdays. She would have been in the building after Milicent left." 

    "You take the necklace out of your pocket. The L shines back at you. You don’t think you’ve ever seen Lavender wear a necklace like that, or has she? No she wouldn’t have done this."

    "The bell for first period rings, you’re out of time. You take the potion out of your pocket and down the last swallow."

    jump potion2

