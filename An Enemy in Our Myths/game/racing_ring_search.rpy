# To create clues, you first need to define a variable and set it equal to the Clue object to create a new instance of a Clue
# Then you simply fill in the name of the clue, the clue ui art that will appear in the inventory, and the description of the clue
# Below are all the clues for pegasus racing ring

default cat_collar = Clue("Cat Collar", "cat_collar_ui", """A collar found in the pegasus stables, but it's way too small for a pegasus. I believe it's a cat collar. It seems very regal and has Egyptian influence in the design and color. Having found cat hair at the penthouse, a cat is definitely tied to this case. Now I believe the collar belongs to Bastet.""")

default broken_chains = Clue("Broken Chains", "broken_chains_ui", """The pegasi were chained up in the stables. There was one pair of chains that had been broken, as well as an empty stable which leads me to believe one of the pegasi might have escaped. but we're not sure when. The pegasus was called Thunder Cloud. According to Bastet, Thunder Cloud was the pegasus our victim was the jockey for. If only we knew Thunder Cloud's whereabouts.""")

default wine_bottle = Clue("Bottle of Wine", "wine_bottle_ui", """This wine bottle is very fancy and looks a little ancient. The only one who would leave something so fancy in a dingy pegasus stable is Dionysus. The design of the bottle seems Greek influenced, which further proves my theory that it's Dionysus'.""")

default scalpel = Clue("Scalpel", "scalpel_ui", """Medical grade scalpel that matches the syringe we found at the penthouse. Has an 'E' engraved in the handle, proving they both belong to the same medical professional. We now know they belong to Eir.""")

default horse_whips = Clue("Pegasus Whips", "horse_whips_ui", """The jockeys used these whips on the pegasi... How cruel.""")

default ambrosia_2 = Clue("Ambrosia", "ambrosia_2_ui", """More 'Ambrosia' found at the stables. Clearly tied to the case, but not sure how. Could the Ambrosia just mean the jockeys were doing drugs? Or were they making it for distribution? Could these races just be a way to show off the drug's effects? Were they testing it on the jockeys and the pegasi? What is the culprit's connection to the drugs?""")

# The logic here is exactly the same as that of the dionysus_search script
# See that script for a more detailed explanation

screen racing_ring_search_screen:
    add "pegasus_empty"
    modal True
    zorder 2

    hbox:
        xalign 0.5
        yalign 0.02
        frame:
            style "grid_background"
            xsize 900
            ysize 125
            grid 6 1:
                    xalign 0.5
                    yalign 0.5
                    spacing 50

                    if "cat_collar" in racing_ring_clues:
                        image "cat_collar_ui"
                    else:
                        image "cat_collar_ui_dark"

                    if "broken_chains" in racing_ring_clues:
                        image "broken_chains_ui"
                    else:
                        image "broken_chains_ui_dark"

                    if "wine_bottle" in racing_ring_clues:
                        image "wine_bottle_ui"
                    else:
                        image "wine_bottle_ui_dark"

                    if "scalpel" in racing_ring_clues:
                        image "scalpel_ui"
                    else:
                        image "scalpel_ui_dark"

                    if "horse_whips" in racing_ring_clues:
                        image "horse_whips_ui"
                    else:
                        image "horse_whips_ui_dark"

                    if "ambrosia_2" in racing_ring_clues:
                        image "ambrosia_2_ui"
                    else:
                        image "ambrosia_2_ui_dark"

    if len(racing_ring_clues) < 6:
        if "cat_collar" in racing_ring_clues:
            null
        else:
            imagebutton:
                idle "cat_collar_clue"
                focus_mask True
                activate_sound "audio/find_sound.wav"
                xalign 0.0
                yalign 0.0
                # hover "ambrosia_clue_hover"

                if len(racing_ring_clues) < 5:
                    action [Function(inventory.append, cat_collar), Function(racing_ring_clues.append, "cat_collar")]
                else:
                    action [Function(inventory.append, cat_collar), Function(racing_ring_clues.append, "cat_collar"), Hide("racing_ring_search_screen"), Return()]

        if "broken_chains" in racing_ring_clues:
            null
        else:
            imagebutton:
                idle "broken_chains_clue"
                focus_mask True
                activate_sound "audio/find_sound.wav"
                xalign 0.1
                yalign 0.1
                # hover "broken_glass_clue_hover"

                if len(racing_ring_clues) < 5:
                    action [Function(inventory.append, broken_chains), Function(racing_ring_clues.append, "broken_chains")]
                else:
                    action [Function(inventory.append, broken_chains), Function(racing_ring_clues.append, "broken_chains"), Hide("racing_ring_search_screen"), Return()]

        if "wine_bottle" in racing_ring_clues:
            null
        else:
            imagebutton:
                idle "wine_bottle_clue"
                focus_mask True
                activate_sound "audio/find_sound.wav"
                xalign 0.2
                yalign 0.2
                # hover "horseshoe_clue_hover"

                if len(racing_ring_clues) < 5:
                    action [Function(inventory.append, wine_bottle), Function(racing_ring_clues.append, "wine_bottle")]
                else:
                    action [Function(inventory.append, wine_bottle), Function(racing_ring_clues.append, "wine_bottle"), Hide("racing_ring_search_screen"), Return()]

        if "scalpel" in racing_ring_clues:
            null
        else:
            imagebutton:
                idle "scalpel_clue"
                focus_mask True
                activate_sound "audio/find_sound.wav"
                xalign 0.3
                yalign 0.3
                # hover "scorches_clue_hover"

                if len(racing_ring_clues) < 5:
                    action [Function(inventory.append, scalpel), Function(racing_ring_clues.append, "scalpel")]
                else:
                    action [Function(inventory.append, scalpel), Function(racing_ring_clues.append, "scalpel"), Hide("racing_ring_search_screen"), Return()]

        if "horse_whips" in racing_ring_clues:
            null
        else:
            imagebutton:
                idle "horse_whips_clue"
                focus_mask True
                activate_sound "audio/find_sound.wav"
                xalign 0.4
                yalign 0.4
                if len(racing_ring_clues) < 5:
                    action [Function(inventory.append, horse_whips), Function(racing_ring_clues.append, "horse_whips")]
                else:
                    action [Function(inventory.append, horse_whips), Function(racing_ring_clues.append, "horse_whips"), Hide("racing_ring_search_screen"), Return()]

        if "ambrosia_2" in racing_ring_clues:
            null
        else:
            imagebutton:
                idle "ambrosia_2_clue"
                focus_mask True
                activate_sound "audio/find_sound.wav"
                xalign 0.5
                yalign 0.5
                # hover "cat_hair_clue_hover"

                if len(racing_ring_clues) < 5:
                    action [Function(inventory.append, ambrosia_2), Function(racing_ring_clues.append, "ambrosia_2")]
                else:
                    action [Function(inventory.append, ambrosia_2), Function(racing_ring_clues.append, "ambrosia_2"), Hide("racing_ring_search_screen"), Return()]

    # BUTTON USED TO CLOSED THE GAME SCREEN BEFORE IT DID IT AUTOMATICALLY
    # imagebutton:
    #     idle "close_inventory.png"
    #     action Hide("dionysus_search_screen")
    #     xalign 0.5
    #     yalign 0.925
