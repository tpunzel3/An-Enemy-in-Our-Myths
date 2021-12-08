# Transforms are used to set the position of images/sprites on the screen
# The can also be used to create faux-animations

#LEFT TRANSFORMS

transform character_left:
    xalign 0.15 yalign 1.0

transform character_move_back_left:
    xalign -0.125 yalign 1.0

transform character_move_back_back_left:
    xalign -0.35 yalign 1.0

transform character_table_left:
    xalign 0.025 yalign 1.0

transform character_move_middle_back_left:
    xalign 0.0 yalign 1.0

transform character_move_off_screen_left:
    xalign -1.75 yalign 1.0


#RIGHT TRASNFORMS

transform character_right:
    xalign 0.85 yalign 1.0

transform character_pegasus_right:
    xalign 1.15 yalign 1.0

transform character_move_back_right:
    xalign 1.15 yalign 1.0

transform character_move_back_back_right:
    xalign 1.35 yalign 1.0

transform character_move_middle_back_right:
    xalign 1.0 yalign 1.0

transform character_move_off_screen_right:
    xalign 2.6 yalign 1.0

transform character_table_right:
    xalign 0.97 yalign 1.0




#OTHERS

transform character_clipboard:
    xalign 1.065 yalign 1.0
    
transform character_1:
    xalign 0.5 yalign 1.0

transform character_2:
    xalign 0.0 yalign 1.0

transform character_3:
    xalign 0.75 yalign 1.0

transform character_4:
    xalign 1.35 yalign 1.0

transform character_5:
    xalign -0.15 yalign 1.0


transform character_move_middle:
    xalign 0.5 yalign 1.0

transform speaker_bounce:
    pause 0.15
    yoffset 0
    easein .175 yoffset -20
    easeout .175 yoffset 0
    easein .175 yoffset -15
    easeout .175 yoffset 0
    yoffset 0
    repeat 1

transform bounce:
    pause .15
    yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 0
    easein .175 yoffset -7
    easeout .175 yoffset 0
    yoffset 0
    repeat

transform credits_start:
    xalign 0.5 yalign 0.0

transform credits_move:
    xalign 0.5 yalign 1.0
