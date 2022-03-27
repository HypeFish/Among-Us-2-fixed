label teacher_end:

    "You race down the the halls to Dean Vance’s Office"

    scene dean office with dissolve
    
    show dean at center wit with dissolve

    user "Dean Vance- Dean-" 

    D "Woah, catch your breath"

    D "What do you need [user]?"

    user "Dean, the satis curae has been stolen and I know who did it!"


    #***NOT CYCLIC***

    menu:
        "Curtis stole it":

            user "Curtis was in the building after hours due to band practice and therefore would have access to the plant. He would have exited through the window to avoid being seen by anyone else."

            D "Do you know why he would have done this?" 

            user "…To be honest sir, I’m not sure. But he is the most likely according to my investigation."
            D "Alright bring him in."

            show curtis neutral at left with dissolve
            show dean at right with dissolve

            D "Curtis do you know why you are here"
            
            show curtis surprised with dissolve

            C "..."

            show curtis embarrassed with dissolve

            C "..."

            C "I SWEAR I’ll never forget my reed again to practice, it was just one time and i still practiced the fingerings and look! I found it today so I’m ready-"

            D "Curtis"

            D "Did you steal the satis curae from Professor Milicent’s classroom?"

            show curtis question with dissolve

            C "No? Why would I do that?"

            D "[user], I don’t think that Curtis would do this, while he may have had the means, it doesn’t seem he has any motive."

            D "Curtis, is it okay if we were to send Professor Milicent home with you today? So she could check your room for it."

            show curtis neutral with dissolve

            C "Yes, of course. You won’t find it though."

            D "That is what I expect"

            "You are starting to suspect you have got the wrong guy."

            D "You are dismissed"

            hide curtis neutral with dissolve

            show dean at center with dissolve

            user "Is Professor Milicent going to lose her job?"

            D "That depends, if the plant is not found then she might face disciplinary action"
            
            D "it is possible that you will too [user]"

            hide dean with dissolve

            scene school hallway with dissolve

            user "*So this is how it feels, to get the wrong guy.*"

            "There’s a deep pit in your stomach"

            "If only you could turn back time once again"

            scene bad end with dissolve
            
            scene credits with dissolve

            return
    

        "Blake stole it":

            user "Blake waited till Professor Milicent had left her classroom, then broke in, stole the plant, and then left through the window."

            D "Do you have anything more than that?"

            user "Only that she was hostile to me and did not provide an alibi when asked."

            D "Okay send her in."

            show blake neutral at left with dissolve

            show dean at right with dissolve

            D "Do you know why you are here?"

            B "Cause I put gum in Jenna’s hair?"

            D "No Blake."

            B "Cause I wrote school sux on the bathroom wall?"

            D "Also no but we can deal with that later"

            D "Did you steal the satis curae from Professor Milicent’s classroom?"

            show blake embarrassed at left with disolve

            B "No, I did not."

            D "Then you wouldn’t mind if Professor Milicent came home with you today to check if the plant was in your room"
            
            show blake angry at left with dissolve

            B "YES I would mind! That’s a fucking invasion of privacy!"

            D "Blake please understand we just need to find the plant, it’s very dangerous-"

            B "Well I'm not letting a teacher follow me home!"

            B "Screw this I’m going back to class."

            hide blake angry with dissolve 

            show dean at center with dissolve

            D "We’ll call her parents to see if the plant is there."

            user "Is Professor Milicent going to lose her job?"

            D "Well if the plant is there, and I suspect that it is. No."

            D "Thank you for your assistance User, It is imperative that the plant is found."

            user "You're welcome Dean Vance!"

            hide dean with dissolve

            scene school hallway dissolve 

            "You feel a sense of pride in your chest."

            "Your first real case, solved."

            "There’s something pulling at the back of your mind."

            "The necklace, you still never figured out who it belonged to."

            "If only you could turn back time once again"


            scene neutral end with Dissolve(3.0)

            scene credits with dissolve(5.0)

            return

        "Lavender stole it":

            user "Lavender was in the building afterschool last evening and stole the plant, then she left by breaking the window so as not to be seen."

            D "Lavender? Why do you think she would do that?"

            user "She has the knowledge to use the plant’s more beneficial properties, like healing and a potion accelerator."

            user "I found this on the scene."

            "You show the Dean the necklace."

            user "While Lavender denies that it is hers, it has the L on it which was left at the scene when she was stealing the plant."

            D "Alright, send her in"

            show lavender neutral at left with dissolve

            show dean at right with dissolve

            D "Do you know why you are here?"

            show lavender angry at left with dissolve

            "You feel Lavender staring daggers into your back"

            L "I do, Dean Vance, I did not steal that plant."

            show lavender neutral at left with dissolve

            L "I know what [user] has told you and I can prove that I was home at the time that it happened."

            "Lavender pulls out her phone and pulls out spellchat"

            L "These are all posted to my spellchat story at the time of the crime"

            "She flickers through her story, pointing at the time stamps"

            user "Why didn’t you show me this when I asked for your alibi?"

            L "I found it right after you left, I would have shown it to you if you came back to me"

            D "Thank you Lavender, you may go back to class."

            "You connect eyes with Lavender as she leaves, you mouth I’m sorry, she turns her head in response."

            "You feel a deep pit in your stomach."

            hide lavender away at left with dissolve

            show dean at center with dissolve

            user "Is Professor Milicent going to lose her job."

            D "That depends, if the plant is not found then she might face disciplinary action."

            D "It is possible that you will too [user]"

            hide dean with dissolve

            scene school hallway with dissolve

            "So this is how it feels, to get the wrong guy."

            "There’s a deep pit in your stomach."

            "You don’t know if Lavender will ever see you the same way again."

            "If only you could turn back time once again."

            scene bad end with Dissolve(3.0)

            scene credits with Dissolve(5.0)


            return
