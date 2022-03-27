label teacher_final:

    #show milicent neutral

    "You make your way to the botany classroom. You know that Milicent will be there, you didn’t ask her to leave the classroom this time around."

    #show milicent happy

    M " I see, you’ve agreed to solve the mystery for me."

    user "Yes but this is my last potion go, I only have time to ask you one question."

    M "Go then!"

    #show milicent neutral

    menu:
        "Do you think Curtis could have done it?":
            $ x = "curtis"

            M "Curtis? He just came in here to get his reed. He was so preoccupied with finding it, he didn’t even notice that the satis curae was gone."

            M "I do not think he would have done it. He’s in my 3rd period, he gets good grades but has never really seemed interested in the art of botany. I don’t see why he would do this."

        "Do you think Lavender could have done it?":
            $ x = "lavender"

            M "Oh goodness. Lavender? She is quite the talented alchemist, if a little slightly clumsy botanist."

            M "Out of all the students here she is the most likely to know how to use the plant to its fullest capacities. But, she’s such a good kid."

            M "I surely hope that she would not have done this. But yes, I think she has a motive."
            
        "Do you think Blake could have done it":
            $ x = "blake"

            M "Blake? Hmmm… Early this semester she didn’t seem to have much of an interest in botany or even passing this class, but things have changed this past month."
        
            M "She is more attentive in class and even came to my after school lecture about healing plants." 

            "You were at that lecture. You remember Blake sitting in the back taking notes, that was odd because you’ve never seen Blake take notes in any class."

            M "I really hope that it was not her. She really seemed to be turning over a new leaf. It's possible she would have stolen it due to her poor grades in the beginning of this semester."

    #play audio.bell
    "The school bell rings" 

    user "Thank you Milicent, I know who took the plant."

    "Before she can say who, you take off for the dean’s office."

    "If you're being honest with yourself, you aren’t 100% sure that you know who took the plant, but you are as sure as you ever will be."


    jump teacher_end



