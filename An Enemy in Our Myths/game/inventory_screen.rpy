# The variable used to track if the player has clicked on a clue
default clue_clicked = False

# The style used to format the clue description text
style inventory_label:
    xalign 0.2

# The style used to create each slot for the clues in the UI
style slot:
    background Frame("square", 0, 0)
    minimum(100,100)
    maximum(100,100)
    xalign 0.5

# The actual screen for the inventory
screen inventory_screen:
    style_prefix "inventory"
    zorder 2
    modal True
    # Adds the clipboard image to use as the background
    add "clipboard"

    # If a clue is clicked, then the Close Inventory button will appear to allow the player to leave the inventory
    if clue_clicked:
        textbutton "Close Inventory":
            action [Hide("inventory_screen"), Return()]
            xalign 0.5
            yalign 0.975

    vbox:
        xanchor 0.5
        xpos 980
        yanchor 0.0
        ypos 225
        #The 7x2 grid that is populated with the clues
        grid 7 2:
            yalign 0.2
            spacing 35
            # For every item in the inventory array (which should be 14)
            for item in inventory:
                frame:
                    # A new slot is created for the clue
                    style "slot"
                    # Then an image button is created for the player to be able to click on
                    imagebutton:
                        # The image for the button is the item.img, which is the Clue UI art from the arguments of the Clue declaration
                        idle item.img
                        # When you click on a button, the selected item variable is updated, as is the clue clicked variable
                        action [SetVariable("selected_item", item), SetVariable("clue_clicked", True)]
                        xalign 0.5
                        yalign 0.5
            # For every spot in the inventory, a slot is created with the slot style
            for i in range(len(inventory), 14):
                frame:
                    style "slot"

        #This vbox is used to display the description for the clues
        vbox:
            xmaximum 850
            #spacing 20
            ypos 65
            xalign 0.5
            # If there is an item selected
            if selected_item != None:

                # A label is created and updated with the description of the item we created in the clue declaration
                label "[selected_item.desc]"
            # If there isn't an item selected, then the label tells the player to pick a clue
            else:
                label "Select an item to read more about it."
