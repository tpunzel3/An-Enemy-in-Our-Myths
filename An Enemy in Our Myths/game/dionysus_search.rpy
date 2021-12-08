# To create clues, you first need to define a variable and set it equal to the Clue object to create a new instance of a Clue
# Then you simply fill in the name of the clue, the clue ui art that will appear in the inventory, and the description of the clue
# Below are all the clues for Dionysus' penthouse

default ambrosia = Clue("Ambrosia", "ambrosia_ui", "The new drug 'Ambrosia' is golden in color. Supposedly makes someone feel like a god, but effects are still not well known. Dionysus claims to not know much about it and just wanted to try it. But as a god himself, why would he be so interested in a drug that makes him feel like a god? And how would the god of intoxication not know much about a drug? I don't trust him...")

default broken_glass = Clue("Broken Glass", "broken_glass_ui", "Glass shards on the floor, no broken windows in sight. Might just be a broken wine bottle because it's Dionysus' house.")

default horseshoe = Clue("Pegasus Horseshoe", "horseshoe_ui", "We found a pegasus horseshoe at the scene. It probably belonged to the victim since he was racing in the undergound pegasus racing ring. But we still don't know why he would take it to the penthouse with him. Did he always carry it with him?")

default scorches = Clue("Scorch Marks", "scorches_ui", "Scorch marks appear near the body, however, their placement doesn't make any sense if they came from the body. Shouldn't the scorch marks be all around the victim? Also, why didn't anything else catch fire?")

# Though the syringe is delcared here, it is not actually a part of the penthouse search and find
# It is later appended to the inventory after Nimbus has found the syringe
default syringe = Clue("Syringe", "syringe_ui", "Medical grade syringe - seems expensive. Medical tools are supposed to be strictly regulated, so it can’t be Dionysus'. Has an “E” engraved in the plunger.")

default cat_hair = Clue("Cat Hair", "cat_hair_ui", "A lot of cat hair at the scene. But Dionysus doesn't have cats, so how did it get there? If the victim or culprit had enough cat hair on them to bring it into the penthouse, why is it only in one spot? The cat hair points to the cat goddess Bastet as the culrpit, but there's no motive.")

default body = Clue("Body", "body_ui", "The body is burnt beyond recognition and it's missing its torso. He was either killed by an extreme force striking his torso, set on fire, or both? The victim is Arel Farphine, an elf with Norse connections. He was a jockey in the underground pegasus racing ring.")

# This grid is used as the background for the clue bank at the top of the screen
style grid_background:
    background Frame("grid_background", 0, 0)

# This is the actual screen shown for the search and find
screen dionysus_search_screen:
    # It first shows the empty penthouse
    add "penthouse_empty"
    # Modal is true to stop the player from accidentally moving on without finding all the clues
    modal True
    zorder 2

    # This horizontal box (hbox) is used to hold the grid that the clue hints are stored in
    hbox:
        xalign 0.5
        yalign 0.02
        frame:
            # This is the previously defined style from line 20
            style "grid_background"
            xsize 900
            ysize 125
            # This 6x1 grid stores all the UI art for the clue hints
            grid 6 1:
                    xalign 0.5
                    yalign 0.5
                    spacing 50

                    # Here is a list of conditionals for the clue hints
                    # If the player HAS found the clue, which is extrapolated from the dionysus_clues array, then the clue UI shows in full color to acknowledge that
                    if "ambrosia" in dionysus_clues:
                        image "ambrosia_ui"
                    # But if the player HAS NOT found the clue, the UI is dark to show that the player still needs to find that clue
                    else:
                        image "ambrosia_ui_dark"

                    if "broken_glass" in dionysus_clues:
                        image "broken_glass_ui"
                    else:
                        image "broken_glass_ui_dark"

                    if "horseshoe" in dionysus_clues:
                        image "horseshoe_ui"
                    else:
                        image "horseshoe_ui_dark"

                    if "scorches" in dionysus_clues:
                        image "scorches_ui"
                    else:
                        image "scorches_ui_dark"

                    if "cat_hair" in dionysus_clues:
                        image "cat_hair_ui"
                    else:
                        image "cat_hair_ui_dark"

                    if "body" in dionysus_clues:
                        image "body_ui"
                    else:
                        image "body_ui_dark"

    # So long as the length of the dionysus_clues array is less than 6 (the number of clues), then it will continue to populate the screen with clues
    if len(dionysus_clues) < 6:
        # If the player had already found the ambrosia clue, then it returns null, removing the imagebutton for the clue
        if "ambrosia" in dionysus_clues:
            null
        else:
            # This creates an image button for the clue that allows the player to click the clues on the screen
            imagebutton:
                idle "ambrosia_clue"
                focus_mask True
                activate_sound "audio/find_sound.wav"
                # hover "ambrosia_clue_hover"

                # If the length of dionysus_clues is less than 5 (one less than the max amount of clues), then
                if len(dionysus_clues) < 5:
                    # The clue gets added to the inventory and the specific search and find array, in this case: dionysus_clues
                    action [Function(inventory.append, ambrosia), Function(dionysus_clues.append, "ambrosia")]
                # If the length of dionysus_clues is equal to or greater than 5, then
                else:
                    # The clue gets added to the inventory and the specific search and find array, but also hides the screen and returns to the dialogue that was previously being displayed
                    action [Function(inventory.append, ambrosia), Function(dionysus_clues.append, "ambrosia"), Hide("dionysus_search_screen"), Return()]

        # This repeats over and over again for every clue in the search and find
        if "broken_glass" in dionysus_clues:
            null
        else:
            imagebutton:
                idle "broken_glass_clue"
                focus_mask True
                activate_sound "audio/find_sound.wav"
                # hover "broken_glass_clue_hover"

                if len(dionysus_clues) < 5:
                    action [Function(inventory.append, broken_glass), Function(dionysus_clues.append, "broken_glass")]
                else:
                    action [Function(inventory.append, broken_glass), Function(dionysus_clues.append, "broken_glass"), Hide("dionysus_search_screen"), Return()]

        if "horseshoe" in dionysus_clues:
            null
        else:
            imagebutton:
                idle "horseshoe_clue"
                focus_mask True
                activate_sound "audio/find_sound.wav"
                # hover "horseshoe_clue_hover"

                if len(dionysus_clues) < 5:
                    action [Function(inventory.append, horseshoe), Function(dionysus_clues.append, "horseshoe")]
                else:
                    action [Function(inventory.append, horseshoe), Function(dionysus_clues.append, "horseshoe"), Hide("dionysus_search_screen"), Return()]

        if "scorches" in dionysus_clues:
            null
        else:
            imagebutton:
                idle "scorches_clue"
                focus_mask True
                activate_sound "audio/find_sound.wav"
                # hover "scorches_clue_hover"

                if len(dionysus_clues) < 5:
                    action [Function(inventory.append, scorches), Function(dionysus_clues.append, "scorches")]
                else:
                    action [Function(inventory.append, scorches), Function(dionysus_clues.append, "scorches"), Hide("dionysus_search_screen"), Return()]

        if "cat_hair" in dionysus_clues:
            null
        else:
            imagebutton:
                idle "cat_hair_clue"
                focus_mask True
                activate_sound "audio/find_sound.wav"
                # hover "cat_hair_clue_hover"

                if len(dionysus_clues) < 5:
                    action [Function(inventory.append, cat_hair), Function(dionysus_clues.append, "cat_hair")]
                else:
                    action [Function(inventory.append, cat_hair), Function(dionysus_clues.append, "cat_hair"), Hide("dionysus_search_screen"), Return()]

        if "body" in dionysus_clues:
            null
        else:
            imagebutton:
                idle "body_clue"
                focus_mask True
                activate_sound "audio/find_sound.wav"
                # hover "body_clue_hover"

                if len(dionysus_clues) < 5:
                    action [Function(inventory.append, body), Function(dionysus_clues.append, "body")]
                else:
                    action [Function(inventory.append, body), Function(dionysus_clues.append, "body"), Hide("dionysus_search_screen"), Return()]
