label post_interrogation_office:

    scene office with dissolve

    play music "audio/office.mp3" fadein 1.0

    show detective annoyed at character_left
    show assistant neutral at character_right
    with dissolve

    # show screen add_clues

    d "This case is proving to be much more difficult than I thought it would be."
    show assistant sideeye
    a "It {i}is{/i} a complicated case."
    show detective thinking
    d "If we were just on the case for the pegasus racing ring, we could just arrest Dionysus, Bastet, and Eir, but..."
    show assistant neutral
    a "But we are trying to solve the murder."
    show detective neutral
    d "Yes, and I'm still not quite sure who did it."
    show detective thinking
    d "They all have evidence against them, but they also don't seem to have a good enough reason to murder our victim."
    a "Let's look over our notes and see if anything clicks."

# The label used for when it's time for the player to check their clue inventory
label inventory_check:
    # clue_clicked is set to False just to ensure that the player has to click a clue
    $ clue_clicked = False
    show assistant thinking at character_clipboard
    show detective notes at character_move_back_left
    with ease

    # The inventory screen is shown and the player can click on clues, reading the descriptions
    # Once the player has decided to move on, there is a Close Inventory button that allows them to close the inventory_screen
    show screen inventory_screen
    pause

    show screen dark
    D "I think that's enough looking at my notes."
    hide screen dark

    show detective thinking at character_left
    show assistant neutral at character_right
    with ease
    a "Did your notes prove useful?"
    menu:
        # If the player doesn't want to look at their inventory again
        "Yes, I think it's time to assemble our suspects.":
            a "I'll inform Chief Valkyrie to bring them to the station."
            show detective thinking
            d "Actually, let's have them brought to the scene of the murder."
            show assistant thinking
            a "Smart. It would be a pain to get Dionysus anywhere since he -"
            show detective smile
            d "True, but that's not why. I'll fill you in on the way."
            d "Let's go!"
            show detective smile at character_move_off_screen_left
            with ease
            show assistant neutral
            a "Right!"
            show assistant neutral flip at character_move_off_screen_right
            with ease

            scene black
            with fade

            pause 0.5

            stop music fadeout 1.0
            # Then the game jumps to the final penthouse scene
            jump penthouse_final

        # If the player wants to take another look at their inventory
        "Not really. I'm on the verge of a breakthrough, but I'm still missing something.":
            show assistant thinking
            a "Well, it can't hurt to give your notes another look."
            show detective neutral
            d "I guess you're right. I'll take another look."
            # Then the game jumps back to the inventory_check so the player can look at the inventory again
            jump inventory_check
