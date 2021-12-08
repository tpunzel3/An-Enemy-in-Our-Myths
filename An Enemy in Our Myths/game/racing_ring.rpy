# The following four variables are used to keep track of which clues the detective has talked with the Chief Valkyrie about
default ambrosia_asked_3 = False
default cat_collar_asked = False
default scalpel_asked = False
default wine_bottle_asked = False

# This variable keeps track of how many of the clues have been talked about
default pegasus_total_asked = 0

# This is the clue for the ID cards that one of the Valkyrie officers finds
default id_cards = Clue("ID Cards", "id_cards_ui", "Three ID cards found in the pegasus racing ring belonging to Dionysus, Bastet, and Eir, clearly linking them to the victim and the racing ring. However, that doesn't mean that they murdered our victim. Also, why were they left at the racing ring?")


label racing_ring:

    scene pegasus_full with fade

    play music "audio/racing_ring.mp3" fadein 1.0

    show detective smile at character_left with dissolve

    d "For my first raid, I would say that was pretty successful."
    show valkyrie neutral at character_right with dissolve
    v "I'll be honest, that went a lot smoother than I thought. Even without Nimbus."
    show detective neutral
    d "I feel bad that he missed out on this."
    d "Hopefully he will feel better soon."
    show valkyrie thinking
    v "I told him the hay seemed questionable, but he didn't listen."
    show valkyrie neutral
    v "So, how are you feeling?"
    show detective excited
    d "I feel all jittery and pumped up."
    d "It was quite the adrenaline rush when that man-"
    show valkyrie neutral at character_move_middle_back_right
    show detective excited at character_move_middle
    show assistant annoyed flip at character_move_middle_back_left
    with ease
    a "Detective."
    show detective thinking
    d "What? I was just talking about when he pulled out his-"
    show assistant sideeye flip
    a "Detective, look around..."
    d "Huh...?"
    show detective neutral
    d "Oh my gods..."
    show assistant neutral flip
    show valkyrie thinking
    v "I guess we found where they kept the pegasi."
    show valkyrie neutral
    show detective barf
    d "This is worse than I thought."
    a "This is just terrible, but unfortunately, our main focus must be on finding our murderer."
    show detective thinking
    d "I know... It's just..."
    v "Don't worry, you focus on your murderer."
    v "The Valkyrie Force will help the pegasi and see if we can find anything useful."
    show detective neutral
    d "Thank you..."
    d "I guess we will start looking around here for any clues."
    show valkyrie salute
    v "Roger that."
    show valkyrie neutral
    v "Please notify me if you need any help."
    show valkyrie neutral flip
    show valkyrie neutral flip at character_move_off_screen_right with ease
    show screen dark
    D "I hope we can find something useful..."
    hide screen dark
    show detective neutral at character_move_off_screen_left
    show assistant neutral at character_move_off_screen_left
    with ease

    show screen racing_ring_search_screen

    D "I think that's all the clues I can find in these stables."
    show screen dark
    D "I think that's all the clues I can find in these stables."
    hide screen dark

    show assistant neutral flip at character_left
    a "Detective, I was looking in the empty stable and found a wooden plaque that says 'Thunder Cloud'."
    show detective thinking at character_right
    d "So {i}that's{/i} the name of the pegasus that escaped?"
    show assistant thinking flip
    a "A pegasus escaped?"
    show detective neutral
    d "Yes. At least, that is my theory based on the empty stable and the broken chains."
    a "The stable seems like it has been unoccupied for a while now, so if a pegasus escaped from here it would have been a while ago."
    show assistant neutral flip
    a "So wouldn't that pegasus have tried to get help?"
    show detective thinking
    d "Maybe, but it might have been so scared that it just wanted to get as far away from here as possible."
    d "Or worse, something else happened to it..."
    show assistant neutral flip at character_move_middle_back_left
    show detective thinking at character_move_middle
    show valkyrie neutral at character_move_middle_back_right
    with ease
    v "Detective, have you figured out anything from looking around here?"
    show detective neutral
    d "Well, we believe a pegasus might have escaped some time ago, but I am not sure how helpful that will be."
    show detective thinking
    d "But other than that, we found evidence of pegasus abuse like we suspected and also some clues that seem to connect this place to the scene of the murder."
    v "That sounds promising."
    v "What did you find?"

# The label used to loop back to to ensure the player can talk about all the new clues with the Chief Valkyrie
label pegasus_ring_questions:
    show assistant thinking flip
    show detective notes
    show valkyrie thinking

    menu:
        # If the player has not asked about a clue
        "Ambrosia..." if ambrosia_asked_3 != True:
            # The tracking variable is set to True
            $ ambrosia_asked_3 = True
            # The total number of clues talked about is incremented by one
            $ pegasus_total_asked += 1

            show valkyrie neutral
            v "More Ambrosia?"
            show detective neutral
            d "Yes, like what we found at Dionysus' place."
            d "It seems like the pegasus races are connected to the wave of Ambrosia hitting the streets."
            v "Well we know our victim has used Ambrosia before, so this is probably where he got it from."
            show valkyrie thinking
            v "But are you suggesting the organizers are the ones distributing Ambrosia to the streets?"
            show detective thinking
            d "I believe that it's a possibility."
            d "We should also consider the organizers may be using the races as a way to draw in clients for their drug business."
            v "I feel like there are easier ways to distribute drugs."
            show valkyrie neutral
            v "Why would they go through all the trouble of putting on these races to entertain {i}potential{/i} clients if they are just trying to sell drugs?"
            v "Especially since it's a new drug that no one has heard of or knows the effects of?"
            show assistant thinking flip
            a "What if the races aren't just for entertainment?"
            show valkyrie thinking
            v "You don't mean..."
            show detective neutral
            d "They are using the races to {i}show{/i} the effects of the drug."
            show assistant neutral flip
            a "And the jockeys and pegasi are the test subjects."
            show valkyrie thinking
            v "This is getting much more complicated."

            # If the player hasn't talked about all the clues
            if pegasus_total_asked < 4:
                # They loop to the label and can talk about more clues
                jump pegasus_ring_questions
            # If the player has talked about all the clues
            else:
                # Then the player jumps to the post-clue dialogue
                jump post_pegasus_ring_questions

        # The same logic is repeated for every clue
        "A cat collar..." if cat_collar_asked != True:
            $ cat_collar_asked = True
            $ pegasus_total_asked += 1

            show valkyrie neutral
            v "Why is there a cat collar in the pegasus stables?"
            show detective neutral
            d "I was wondering the same thing."
            show detective thinking
            show assistant sideeye flip
            d "What is strange is that there was a lot of cat hair at Dionysus' penthouse even though he doesn't have any cats."
            show valkyrie thinking
            v "So all we know is that a cat is somehow involved in all of this?"
            show detective neutral
            d "Well, it is a very fancy collar, and the pattern resembles Egyptian patterns I would see in museums back on earth."
            show valkyrie neutral
            v "So, a cat with Egyptian origins?"
            show assistant sideeye flip
            a "Oh... her..."
            show detective thinking
            d "Her?"
            show assistant neutral flip
            a "Bastet, the Egyptian goddess of cats."
            show detective neutral
            d "You don't seem too fond of her."
            show assistant sideeye flip
            a "Well, she runs a cat café..."
            show detective neutral
            d "Enough said."
            d "Chief Valkyrie, we should bring Bastet in for questioning."
            show valkyrie salute
            v "Roger!"

            if pegasus_total_asked < 4:
                jump pegasus_ring_questions
            else:
                jump post_pegasus_ring_questions

        "A scalpel..." if scalpel_asked != True:
            $ scalpel_asked = True
            $ pegasus_total_asked += 1

            v "A scalpel?"
            show detective neutral
            d "This is a medical grade scalpel with the same 'E' engraved in it like the syringe we found at Dionysus' penthouse."
            show assistant neutral flip
            a "So unless it was stolen, we should be looking for a well-known doctor whose name starts with an 'E'."
            show valkyrie thinking
            v "An 'E'..."
            show valkyrie neutral
            v "Well I doubt it's her, but the only one I can think of who meets the criteria is Eir."
            show detective thinking
            d "Eir?"
            a "She is the Norse goddess of medicine, so she does indeed fit the criteria."
            v "She is also one of the head doctors at the hospital, so she would definitely have customized medical tools."
            show valkyrie thinking
            v "But she seems too nice to be able to do something like this..."
            show detective neutral
            d "Nice or not, I think it would be a good idea to have a chat with her."
            show valkyrie neutral
            v "I'll send some Valkyrie to her cottage and have them bring her to the station for questioning."

            if pegasus_total_asked < 4:
                jump pegasus_ring_questions
            else:
                jump post_pegasus_ring_questions

        "A very fine bottle of wine..." if wine_bottle_asked != True:
            $ wine_bottle_asked = True
            $ pegasus_total_asked += 1

            v "A fancy bottle of wine? In these dingy stables?"
            show valkyrie neutral
            v "You would have to be crazy to... Oh..."
            show assistant sideeye flip
            show detective annoyed
            d "Yes, I'm afraid so."
            show valkyrie thinking
            v "Should I have the Valkyrie bring him in?"
            show detective neutral
            show assistant neutral flip
            d "No, I don't think that is necessary."
            d "They should just keep watching him for now."
            show valkyrie neutral
            v "That works for me."

            if pegasus_total_asked < 4:
                jump pegasus_ring_questions
            else:
                jump post_pegasus_ring_questions

# The label used to jump to after the player has talked about all the new clues
label post_pegasus_ring_questions:
    show detective neutral
    d "We should probably start looking elsewhere."
    vks "Chief Valkyrie! We found these!"
    v "Let me see those..."
    show valkyrie neutral flip at character_move_off_screen_right with ease
    pause 0.5
    show valkyrie neutral at character_move_middle_back_right with ease

    show valkyrie thinking
    v "Well I'll be."
    show detective thinking
    d "What did they find?"
    show valkyrie neutral
    v "These are ID badges for Dionysus, Bastet, and Eir."

    # This appends the inventory with the ID card clue after the Valkyrie officer has found them
    $ inventory.append(id_cards)

    show assistant sideeye flip
    a "That is very convenient."
    show detective neutral
    d "Very."
    show assistant neutral flip
    d "Now we can return their badges to them in the interrogation room."
    v "I'll send some Valkyrie to bring them in right away."
    d "They can just bring Eir and Bastet for now."
    d "I don’t think talking to Dionysus again would be worth the headache."
    show valkyrie salute
    v "Roger that."
    show valkyrie neutral
    v "I'll have some Valkyrie escort you to the station to prepare for the interrogation."
    d "Much appreciated."
    show valkyrie neutral flip at character_move_off_screen_right
    show detective neutral at character_right
    show assistant neutral flip at character_left
    with ease
    d "Now let's go have a chat with some goddesses about an underground pegasus racing and/or drug ring!"
    d "That's not something I ever thought I would say in my life."
    show assistant sideeye flip
    a "Let's go, Detective."

    stop music fadeout 1.0
    jump interrogation_room
