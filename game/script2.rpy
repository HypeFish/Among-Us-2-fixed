label hallway:

    "The school bell rings once signaling to everyone that there’s 30 minutes before the first period."

    "You grab your bag and sling it over your shoulder."

    "Yeah it's a little early to be arriving to first period,
    but you like speaking to your botany teacher, Milicent, before class starts."

    "You make your way to the classroom passing familiar faces."

    #show lavender neutral

    "You’ve been best friends with Lavender ever since you were in Mr. Clay’s 4th grade class."

    "She has seen you at your highest (winning your school’s mystery story contest) and your lowest (that time a transmission spell you cast backfired and you croaked like a frog for the rest of the week)."

    #show lavender happy

    L "Hey [user]! Going to visit Milicent?"
    user "Yup! She's got this new brown mold that can boost-"
    L "ooooh mold sounds amazing!"
    user "shut up! It is amazing!"
    L "I gotta go return this breaker to the alchemy lab but I’ll catch you later."

    "You two do a super secret super sweet handshake"

    #hide lavender happy


    #show blake neutral

    "You pass Blake. You do your best not to be scared, you think she can smell fear."

    "Alright you're calm, you're cool. You wave at her."

    #show blake angry

    B "*scowels*"

    "Blake is in your evocation class"
    "On fire week she made a spell so big that it singed the top of the teacher's hair"
    "You’ve been trying to open friendly communications just in case you get paired for any kind of project, but have thus far been unsuccessful."

    #hide blake neutral

    #show curtis neutral

    "You pass Curtis. He looks like he always does."

    "Like he really needs to pee, and has been holding it for way too long out of fear of asking a teacher to leave class."

    scene background_botony

    "Finally you make it to the botany classroom, you open the door and- "

    user "It's gone! The satis curae!! It's- "

    "The door slams behind you! You hear the deadbolt click."

    "You turn around to see Milicent."

    #show milicent embarrased

    user "Professor Milicent! What's going on!? The satis curae is gone!"

    M "Shh! Shh! I can see that! Please be quieter, I don’t want anyone coming in."

    # show milicent neutral

    M "Yes the satis curae is gone, I came here in the morning and it wasn’t here."

    "There are so many questions to ask! Where should you start?"

    menu:
        "Why would someone want to steal a plant?":
            $ x = "plant"
            #show milicent question
            M "Aside from the plant's beauty?"
            M "It is extremely deadly without proper care from a botanist."
            #show milicent surprise
            M "Whoever took the plant might want to use it to harm someone, however I fear for the person who took the plant."
            M "If they don't know what they are doing it could kill them!"
            #show milicent neutral


        "When would the plant have been taken?":
            $ x = "taken"
            M "After school, I packed up my things and went home."
            M "Made some tea, graded some papers, and then went to bed."
            #show milicent sad
            M "Perhaps I should have taken the plant home with me, I feel so terrible that it’s gone now."
            #show milicent neutral
            M "Gladis at the front desk said bye to me as I left at 7?"
            M "It was 7, yes. And then when I came into school this morning, it was gone. It would have been taken in between then."
            "The night guard comes on shift at 10. So thats a 3 hour time window for it to have gone missing."
            user "Can anyone verify your whereabouts?"
            M  "Yes, I was with my wife for the whole night. She can verify that I didn’t leave."



        "What happens if we don't find who stole it?":
            $ x = "unknown"
            M "[user], I fear that if we do not find the satis curse then the school will think that I stole it for myself."
            M " I have access to the botany classroom at any time and the only member of staff who would have any use for it. The dean will fire me."

            "Your heart drops, how could anyone think that Milicent would do that!"
            "She is the sweetest teacher in all the school, nay the world!!!!"

    user "*What else can I ask?*"

    if x == "plant":
        menu:
            "When would the plant have been taken?":
                $ x = "PT"
                M "After school, I packed up my things and went home."
                M "Made some tea, graded some papers, and then went to bed."
                #show milicent sad
                M "Perhaps I should have taken the plant home with me, I feel so terrible that it’s gone now."
                #show milicent neutral
                M "Gladis at the front desk said bye to me as I left at 7?"
                M "It was 7, yes. And then when I came into school this morning, it was gone. It would have been taken in between then."
                "The night guard comes on shift at 10. So thats a 3 hour time window for it to have gone missing."
                user "Can anyone verify your whereabouts?"
                M  "Yes, I was with my wife for the whole night. She can verify that I didn’t leave."



            "What happens if we don't find who stole it?":
                $ x = "PU"
                M "[user], I fear that if we do not find the satis curse then the school will think that I stole it for myself."
                M " I have access to the botany classroom at any time and the only member of staff who would have any use for it. The dean will fire me."

                "Your heart drops, how could anyone think that Milicent would do that!"
                "She is the sweetest teacher in all the school, nay the world!!!!"

    if x == "taken":
        menu:
            "Why would someone want to steal a plant?":
                $ x = "PT"
                #show milicent question
                M "Aside from the plant's beauty?"
                M "It is extremely deadly without proper care from a botanist."
                #show milicent surprise
                M "Whoever took the plant might want to use it to harm someone, however I fear for the person who took the plant."
                M "If they don't know what they are doing it could kill them!"
                #show milicent neutral

            "What happens if we don't find who stole it?":
                $ x = "TU"
                M "[user], I fear that if we do not find the satis curse then the school will think that I stole it for myself."
                M " I have access to the botany classroom at any time and the only member of staff who would have any use for it. The dean will fire me."
                "Your heart drops, how could anyone think that Milicent would do that!"
                "She is the sweetest teacher in all the school, nay the world!!!!"

    if x == "unknown":
        menu:
            "Why would someone want to steal a plant?":
                $ x = "PU"
                #show milicent question
                M "Aside from the plant's beauty?"
                M "It is extremely deadly without proper care from a botanist."
                #show milicent surprise
                M "Whoever took the plant might want to use it to harm someone, however I fear for the person who took the plant."
                M "If they don't know what they are doing it could kill them!"
                #show milicent neutral


            "When would the plant have been taken?":
                $ x = "TU"
                M "After school, I packed up my things and went home."
                M "Made some tea, graded some papers, and then went to bed."
                #show milicent sad
                M "Perhaps I should have taken the plant home with me, I feel so terrible that it’s gone now."
                #show milicent neutral
                M "Gladis at the front desk said bye to me as I left at 7?"
                M "It was 7, yes. And then when I came into school this morning, it was gone. It would have been taken in between then."
                "The night guard comes on shift at 10. So thats a 3 hour time window for it to have gone missing."
                user "Can anyone verify your whereabouts?"
                M  "Yes, I was with my wife for the whole night. She can verify that I didn’t leave."

    user "*What else can I ask?*"

    if x == "PT":
        menu:
            "What happens if we don't find who stole it?":
                $ x = "unknown"
                M "[user], I fear that if we do not find the satis curse then the school will think that I stole it for myself."
                M " I have access to the botany classroom at any time and the only member of staff who would have any use for it. The dean will fire me."

                "Your heart drops, how could anyone think that Milicent would do that!"
                "She is the sweetest teacher in all the school, nay the world!!!!"

    if x == "TU":
        menu:
            "Why would someone want to steal a plant?":
                $ x = "plant"
                #show milicent question
                M "Aside from the plant's beauty?"
                M "It is extremely deadly without proper care from a botanist."
                #show milicent surprise
                M "Whoever took the plant might want to use it to harm someone, however I fear for the person who took the plant."
                M "If they don't know what they are doing it could kill them!"
                #show milicent neutral

    if x == "PU":
        menu:
            "When would the plant have been taken?":
                M "After school, I packed up my things and went home."
                M "Made some tea, graded some papers, and then went to bed."
                #show milicent sad
                M "Perhaps I should have taken the plant home with me, I feel so terrible that it’s gone now."
                #show milicent neutral
                M "Gladis at the front desk said bye to me as I left at 7?"
                M "It was 7, yes. And then when I came into school this morning, it was gone. It would have been taken in between then."
                "The night guard comes on shift at 10. So thats a 3 hour time window for it to have gone missing."
                user "Can anyone verify your whereabouts?"
                M  "Yes, I was with my wife for the whole night. She can verify that I didn’t leave."



    "You hear someone jiggle the handle of the door. Someone else arriving early to class?"

    M "We don't have much time, after first period starts in 15 minutes all the students will see that the satis curae and the dean will be alerted to it’s disappearance."

    #show milicent embarrassed

    M "[user], I know this is a lot to ask of you, but I know that you love mysteries."

    "The Detective Harvy Lawson (Esquire) books weight heavy in your backpack."

    #show milicent neutral

    M "I need you to find out who stole the plant."

    "A case, a real case. You've never taken on a real case before."

    user "Alright, I will figure out who did it."

    #show milicent happy

    M "Here, take this."

    "Milicent pushes a small potion bottle into your hands."

    #show milicent neutral

    M "This potion can rewind time for 30 minutes, but there's only 2 swallows in here. That can buy you a little extra time?"

    user "How much time do i have now?"

    M "About 13 minutes left before the period starts."

    user "Okay, enough time to search the room"

    #hide milicent neutral

    user "Okay, okay time to search the crime scene now!"

    "You've never searched a crime scene before..."

    "The thing that stands out the most is the lack of the satis curae. It had stool tall in the middle of the room and it’s absences was hard to miss."

    "Scanning among the rows and rows of plants, everything else is accounted for. All the herbs, flowers, and molds are in their place."

    "As you are looking you feel a cold breeze, brrrgh! Where’s that draft coming from! You turn your attention to the window, which has been broken!"

    "*zoom in on window*"

    "A forced entry or exit! If the thief had to come or go from the window they might not have had access to the room after school. Or perhaps they didn't want to be seen leaving with the plant by others."

    "*zoom out*"

    "Either way this means that Milicent couldn’t have done it. She has access to the room and wouldn’t have needed to break in."

    "As well, no one would bat an eye at the botany professor carrying a plant out of the building."

    "It just doesn’t make sense for her to have needed to break the window."

    "The clock is moving very fast. You see Milicent pacing back and forth. Think! Think! You've got to think! Who would have been in the building yesterday night after students had left."

    "You remember hearing about band practice for the spring showcase. It could be been one of them?"

    "The school bell rings"

    jump potion1