label blake_end:

    "You race down the the halls to Dean Vance’s Office"
    
    show dean at center

    user "Dean Vance- Dean-" 

    D "Woah, catch your breath"

    D "What do you need [user]?"

    user "Dean, the satis curae has been stolen and I know who did it!"
    
    menu:
        "Curtis stole it":

            user "Curtis was in the building after hours due to band practice and therefore would have access to the plant. He would have exited through the window to avoid being seen by anyone else."

            D "Do you know why he would have done this?" 

            user "…To be honest sir, I’m not sure. But he is the most likely according to my investigation."

            D "Alright, bring him in."

            show curtis neutral at left
            show dean at right

            D "Curtis do you know why you are here"
            
            show curtis surprised

            C "..."

            show curtis embarrassed

            C "..."

            C "I SWEAR I’ll never forget my reed again to practice, it was just one time and i still practiced the fingerings and look! I found it today so I’m ready-"

            D "Curtis"

            D "Did you steal the satis curae from Professor Milicent’s classroom?"

            show curtis question

            C "No? Why would I do that?"

            D "[user], I don’t think that Curtis would do this, while he may have had the means, it doesn’t seem he has any motive."

            D "Curtis, is it okay if we were to send Professor Milicent home with you today? So she could check your room for it."

            show curtis neutral

            C "Yes, of course. You won’t find it though."

            D "That is what I expect"

            "You are starting to suspect you have got the wrong guy."

            D "You are dismissed"

            hide curtis neutral

            show dean at center

            user "Is Professor Milicent going to lose her job?"

            D "That depends, if the plant is not found then she might face disciplinary action"
            
            D "it is possible that you will too [user]"

            hide dean

            scene school hallway

            "You know Curtis didn't do it."

            "But at least Blake will be able to give the potion to her sister."

            "There’s a deep pit in your stomach"

            "You hope it’s enough to have Milicent keep her job"

            "You could have done better"

            "If only you could turn back time again"


            scene bad end 
            
            ""
            scene credits 

            ""

            return
    

        "Blake stole it":

            user "Blake waited till Professor Milicent had left her classroom, then broke in, stole the plant, and then left through the window. She dropped her locket on the scene with her sister’s first initial on it."

            D "Why would Blake take a risk like that?"

            user "Because her sister is very sick. And while the satis curae is quite poisonous, it also can be used to create powerful healing potions."

            D "Okay, send her in."

            show blake neutral at left
            show dean at right

            D "Do you know why you are here?"

            B "…"

            B "…"

            show blake sad at left

            B "I trusted you!"

            B "I trusted you [user]!" 

            D "Blake, do you have the plant"

            B "Yes! But I need it! It was just sitting there in the classroom and I needed it!"

            D "Blake, I need you to stare here and we can discuss disciplinary action."

            D "[user], thank you for your assistance in solving this case. Please make your way to your first period."

            hide blake sad 
            hide dean 

            scene school hallway

            "You did it!"

            "You solved your first case!"

            "This calls for celebrations! Right?"

            "There’s something tugging at you."

            "Something you could have done better."

            "If only you could turn back time once more."



            scene neutral end

            ""
            scene credits

            return

        "Lavender stole it":

            user "Lavender was in the building afterschool last evening and stole the plant, then she left by breaking the window so as not to be seen."

            D "Lavender? Why do you think she would do that?"

            user "She has the knowledge to use the plant’s more beneficial properties, like healing and a potion accelerator."

            user "I found this on the scene."

            "You show the Dean the necklace."

            user "While Lavender denies that it is hers, it has the L on it which was left at the scene when she was stealing the plant."

            D "Alright, send her in"

            show lavender neutral at left 
            show dean at right

            D "Do you know why you are here?"

            show lavender angry at left

            "You feel Lavender staring daggers into your back"

            L "I do, Dean Vance, I did not steal that plant."

            show lavender neutral at left

            L "I know what [user] has told you and I can prove that I was home at the time that it happened."

            "Lavender pulls out her phone and pulls out spellchat"

            L "These are all posted to my spellchat story at the time of the crime"

            "She flickers through her story, pointing at the time stamps"

            user "Why didn’t you show me this when I asked for your alibi?"

            L "I found it right after you left, I would have shown it to you if you came back to me"

            D "Thank you Lavender, you may go back to class."

            "You connect eyes with Lavender as she leaves, you mouth I’m sorry, she turns her head in response."

            "You feel a deep pit in your stomach."

            hide lavender away at left
            show dean at center

            user "Is Professor Milicent going to lose her job."

            D "That depends, if the plant is not found then she might face disciplinary action."

            D "It is possible that you will too [user]"

            hide dean 

            scene school hallway

            "So this is how it feels, to get the wrong guy."

            "There’s a deep pit in your stomach."

            "You don’t know if Lavender will ever see you the same way again."

            "If only you could turn back time once again."

            scene bad end 

            ""
            scene credits

            ""

            return
