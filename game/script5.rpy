label potion2:
    "The school bell rings once signaling to everyone that there’s 30 minutes before the first period."

    "You grab your bag and sling it over your shoulder. One more chance to solve this mystery. You don't like where the clues are leading."

    "You reach into your pocket. The necklace is still there. You run your hand over it. The L doesn’t stand for Lavender! It could stand for many things! Like lesbians!"
    
    "Or lobster? or…"

    "You walk down the hall towards Lavender's locker. (L also could be locker)"

    #show lavender neutral

    user "Hi Lavender!"

    #show lavender happy 

    L "Hey [user], Going to visit-"

    user "The satis curae has been stolen..."

    #show lavender surprise

    L "The satis curae! That is extremely deadly in the wrong hands it could-"

    "She knows the plant and its effect, she might even know how to use it"

    user "and this was found on the scene"

    "You bring the necklace out of your pocket and show it to her."

    #show lavender question

    L "You don't think, you don't think I did this do you?"

    #show lavendar angry

    L "I wouldn't do this! [user], you know I wouldn't do this"

    user "Can i please just ask a couple of questions"

    #show lavender neutral

    L "... sure"

    menu:
        "Where were you last night":
            $ x = "1"
            L "Well alchemy club ended at 6:30, and I went home. I studied for the upcoming divination quiz. Made myself some dinner, and then went to bed."

            user "Did anyone see you when you got home"

            L "No. My parents were out for some dinner party thing and I was alone in my room"

            "You wonder if you could put her cat on the stand to testify her wherabouts"

            L "And Danny was down in the basement"
            
            "Nevermind"

        "What did you know about the satis curae":
            $ x =  "2" 
            L "I know that it contains an extremely deadly poison. If not taken care by a talented botanist it can even kill just from its growth."

            L "Its main use is as an accelerator for reactions. Transmutations that would normally take a month happen in a day. But again, if used improperly it will just kill the potion drinker."

            L "As well the bulb of the plant has been shown to contain a powerful chemical that can accelerate the effects of a healing potion."

            L "Basically it can kill you fast, change you fast, or heal you fast."

            L "But most likely it’ll just kill you fast"

            user "Milicent didn't tell me about any of this when i asked her about why same"

            L "Well because its positive properties are really hard to bring out. You have to be a very talented alchemist to use its accelerant properties."

            L "Plus she's probably worried that whoever stole it will hurt themselves with it. That woman could not kill a fly. She probably blames herself for it being stolen."

            user "you know that telling me this-"

            #show lavender angry

            L "gives me motive? Yeah I know, I want you to catch whoever did this because I didn't! So I’m trying to be helpful [user]!"

            "It's hard to have Lavender be angry like this at you."

            L "I'm pleased that you think of my alchemy talents so highly"

            "Lavender can pour sarcasm on sentences like one pours syrup on pancakes"

            #show lavender neutral

        "Is this your necklace?":
            $ x = "3"

            #show lavender angry    
            
            L "NO! Thats not mine!"
            L "I don't wear silver jewelry!"
            L "And i think monogrammed jewelry is tacky"

            #show lavender neutral

        user "*What can I ask?*"

    if x == "1":
        menu:
            "What did you know about the satis curae":
                $ x =  "12" 
                L "I know that it contains an extremely deadly poison. If not taken care by a talented botanist it can even kill just from its growth."

                L "Its main use is as an accelerator for reactions. Transmutations that would normally take a month happen in a day. But again, if used improperly it will just kill the potion drinker."

                L "As well the bulb of the plant has been shown to contain a powerful chemical that can accelerate the effects of a healing potion."

                L "Basically it can kill you fast, change you fast, or heal you fast."

                L "But most likely it’ll just kill you fast"

                user "Milicent didn't tell me about any of this when i asked her about why same"

                L "Well because its positive properties are really hard to bring out. You have to be a very talented alchemist to use its accelerant properties."

                L "Plus she's probably worried that whoever stole it will hurt themselves with it. That woman could not kill a fly. She probably blames herself for it being stolen."

                user "you know that telling me this-"

                #show lavender angry

                L "gives me motive? Yeah I know, I want you to catch whoever did this because I didn't! So I’m trying to be helpful [user]!"

                "It's hard to have Lavender be angry like this at you."

                L "I'm pleased that you think of my alchemy talents so highly"

                "Lavender can pour sarcasm on sentences like one pours syrup on pancakes"

                #show lavender neutral

            "Is this your necklace?":
                $ x = "13"

                #show lavender angry    
                    
                L "NO! Thats not mine!"
                L "I don't wear silver jewelry!"
                L "And i think monogrammed jewelry is tacky"

                #show lavender neutral
        
    if x == "2":
        menu:
            "Where were you last night":
                $ x = "12"
                L "Well alchemy club ended at 6:30, and I went home. I studied for the upcoming divination quiz. Made myself some dinner, and then went to bed."

                user "Did anyone see you when you got home"

                L "No. My parents were out for some dinner party thing and I was alone in my room"

                "You wonder if you could put her cat on the stand to testify her wherabouts"

                L "And Danny was down in the basement"
                    
                "Nevermind"

            "Is this your necklace?":
                $ x = "23"

                #show lavender angry    
                    
                L "NO! Thats not mine!"
                L "I don't wear silver jewelry!"
                L "And i think monogrammed jewelry is tacky"

                #show lavender neutral

    if x == "3":
        menu:
            "Where were you last night":
                $ x = "1"
                L "Well alchemy club ended at 6:30, and I went home. I studied for the upcoming divination quiz. Made myself some dinner, and then went to bed."

                user "Did anyone see you when you got home"

                L "No. My parents were out for some dinner party thing and I was alone in my room"

                "You wonder if you could put her cat on the stand to testify her wherabouts"

                L "And Danny was down in the basement"
                    
                "Nevermind"    

            "What did you know about the satis curae":
                $ x =  "23" 
                L "I know that it contains an extremely deadly poison. If not taken care by a talented botanist it can even kill just from its growth."

                L "Its main use is as an accelerator for reactions. Transmutations that would normally take a month happen in a day. But again, if used improperly it will just kill the potion drinker."

                L "As well the bulb of the plant has been shown to contain a powerful chemical that can accelerate the effects of a healing potion."

                L "Basically it can kill you fast, change you fast, or heal you fast."

                L "But most likely it’ll just kill you fast"

                user "Milicent didn't tell me about any of this when i asked her about why same"

                L "Well because its positive properties are really hard to bring out. You have to be a very talented alchemist to use its accelerant properties."

                L "Plus she's probably worried that whoever stole it will hurt themselves with it. That woman could not kill a fly. She probably blames herself for it being stolen."

                user "you know that telling me this-"

                #show lavender angry

                L "gives me motive? Yeah I know, I want you to catch whoever did this because I didn't! So I’m trying to be helpful [user]!"

                "It's hard to have Lavender be angry like this at you."

                L "I'm pleased that you think of my alchemy talents so highly"

                "Lavender can pour sarcasm on sentences like one pours syrup on pancakes"

                #show lavender neutral

    user "*What else can I ask?*"

    if x == "12":
        menu:
            "Is this your necklace?":

                #show lavender angry    
                        
                L "NO! Thats not mine!"
                L "I don't wear silver jewelry!"
                L "And i think monogrammed jewelry is tacky"

                #show lavender neutral

    if x == "13":
        menu:
            "What did you know about the satis curae":
                L "I know that it contains an extremely deadly poison. If not taken care by a talented botanist it can even kill just from its growth."

                L "Its main use is as an accelerator for reactions. Transmutations that would normally take a month happen in a day. But again, if used improperly it will just kill the potion drinker."

                L "As well the bulb of the plant has been shown to contain a powerful chemical that can accelerate the effects of a healing potion."

                L "Basically it can kill you fast, change you fast, or heal you fast."

                L "But most likely it’ll just kill you fast"

                user "Milicent didn't tell me about any of this when i asked her about why same"

                L "Well because its positive properties are really hard to bring out. You have to be a very talented alchemist to use its accelerant properties."

                L "Plus she's probably worried that whoever stole it will hurt themselves with it. That woman could not kill a fly. She probably blames herself for it being stolen."

                user "you know that telling me this-"

                #show lavender angry

                L "gives me motive? Yeah I know, I want you to catch whoever did this because I didn't! So I’m trying to be helpful [user]!"

                "It's hard to have Lavender be angry like this at you."

                L "I'm pleased that you think of my alchemy talents so highly"

                "Lavender can pour sarcasm on sentences like one pours syrup on pancakes"

                #show lavender neutral

    if x == "23":
        menu:
            "Where were you last night":
                L "Well alchemy club ended at 6:30, and I went home. I studied for the upcoming divination quiz. Made myself some dinner, and then went to bed."

                user "Did anyone see you when you got home"

                L "No. My parents were out for some dinner party thing and I was alone in my room"

                "You wonder if you could put her cat on the stand to testify her wherabouts"

                L "And Danny was down in the basement"
                    
                "Nevermind"

    L "Anything else detective?"

    "Ouch"

    user "I’m sorry Lavender. Please if you can think of anyway to verify that you were home yesterday night, please let me know."

    L "Yeah, I will"

    #show lavender neutral at left

    #show curtis embarrassed at right

    "Curtis hurriedly runs past you, clutching something in his left hand. So he really did leave the reed in the botany classroom."

    #hide curtis embarrassed

    #hide lavender neutral

    "You look at Lavender. This is worse than the time you spilled cranberry sauce on her bed…you don’t like seeing Lavender mad like this, especially not at you."

    "You look at the clock, 15 minutes, youre running out of time."

    "There’s still so much you don’t know, but you only have time to question someone once more"


    menu:
        "Ask Milicent about the other students Motive":
            jump teacher_final
        "Ask Curtis about yesterday's band practice":
            jump curtis_final
        "Try to question Blake again":
            jump blake_final
        "Ask Lavender if she can verify her alibi":
            jump lavender_final    




    




