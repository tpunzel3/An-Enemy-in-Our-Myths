# The custom screen used to darken the screen
screen dark:
    add "dark"

# The screen used for debugging the inventory
# This just has a single button that appends the inventory with every clue
screen add_clues:
    # Creates a text button with the string as the button
    textbutton "Add Clues":
        # As long as the inventory is empty
        if len(inventory) < 14:
            # it will append the inventory over and over with all the clues until it is full
            action [Function(inventory.append, ambrosia),
                    Function(inventory.append, cat_hair),
                    Function(inventory.append, body),
                    Function(inventory.append, broken_glass),
                    Function(inventory.append, horseshoe),
                    Function(inventory.append, scorches),
                    Function(inventory.append, horse_whips),
                    Function(inventory.append, ambrosia_2),
                    Function(inventory.append, broken_chains),
                    Function(inventory.append, wine_bottle),
                    Function(inventory.append, cat_collar),
                    Function(inventory.append, scalpel),
                    Function(inventory.append, syringe),
                    Function(inventory.append, id_cards)]
        xalign 0.1
        yalign 0.1

# The screen used to show the buttons that allows the player to choose who they think is guilty
screen accusation_buttons:
    # Modal means that the player can only click on the screen currently being shown and nothing behind it
    # This is used to stop the player from accidentally advancing the game when in the inventory or some other screen
    modal True
    zorder 10

    # This creates an imagebutton of the character and places it over where their sprite currently is in the game
    imagebutton:
        # idle is used to define the sprite shown when the button is in the idle state
        idle "pegasus dark"
        # focus mask makes it to where the player has to click specifically on the sprite, rather than just blank space, to activate the button
        focus_mask True
        xalign 0.5
        yalign 1.0
        # Jumps to the appropriate label and plays an ominous reveal sound
        action Jump('pegasus_accused')
        activate_sound "audio/reveal_sound.mp3"

    # The next three buttons are the same as the last
    imagebutton:
        idle "dionysus neutral"
        focus_mask True
        xalign 0.0
        yalign 1.0
        action Jump('dionysus_accused')
        activate_sound "audio/reveal_sound.mp3"

    imagebutton:
        idle "eir neutral"
        focus_mask True
        xalign 0.75
        yalign 1.0
        action Jump('eir_accused')
        activate_sound "audio/reveal_sound.mp3"

    imagebutton:
        idle "bastet neutral"
        focus_mask True
        xalign 1.35
        yalign 1.0
        action Jump('bastet_accused')
        activate_sound "audio/reveal_sound.mp3"
