#CHARACTERS

# To create a character in Ren'Py, you first define a variable
# You set it equal to the Character object, which creates a new character
# Then you're able to fill in the arguments with useful information like the character's name, their prefix and suffix for dialogue, their image, dialogue box image, etc.

# The random characters at the beginning of the game
define rando = Character("...", what_prefix='"', what_suffix='"')

# I had to create the credits as a "character" in order to get the scrolling to function properly
# There was probably a better way to do this, but this is the fix that I found
define credits = Character("Credits", what_prefix='"', what_suffix='"', image="credits")

image credits picture:
    "images/Credits.png"
    xanchor 0.5
    yanchor 0.0

# The detective Amelia O'Finnigan
define d = Character("Detective", what_prefix='"', what_suffix='"', image="detective", window_background=Frame("detective_dialogue_box.png"))

# Here you can also add additional character sprites that you may want to use
# You can *technically* put these images anywhere and they would still work, but I liked to have all the character's sprites under their delcaration for organization purposes
image detective neutral:
    "images/detective_neutral.png"
    size(774, 972)

image detective neutral dark:
    "images/detective_neutral_dark.png"
    size(774, 972)

image detective barf:
    "images/detective_barf.png"
    size(774, 972)

image detective thinking:
    "images/detective_thinking.png"
    size(774, 972)

image detective thinking dark:
    "images/detective_thinking_dark.png"
    size(774, 972)

image detective excited:
    "images/detective_excited.png"
    size(774, 972)

image detective excited dark:
    "images/detective_excited_dark.png"
    size(774, 972)

image detective accusation:
    "images/detective_accusation.png"
    size(774, 972)

image detective smile:
    "images/detective_smile.png"
    size(774, 972)

image detective smile dark:
    "images/detective_smile_dark.png"
    size(774, 972)

image detective smile flip:
    "images/detective_smile.png"
    size(774, 972)
    xzoom -1

image detective annoyed:
    "images/Detective_Annoyed.png"
    size(774, 972)

image detective annoyed dark:
    "images/Detective_Annoyed_Dark.png"
    size(774, 972)

image detective notes:
    "images/Detective_Taking_Notes.png"
    size(774, 972)

image detective accusation:
    "images/detective_accusation.png"
    size(774, 972)

# This character is used when the detective is thinking
define D = Character("Detective", window_background=Frame("detective_dialogue_box.png"), what_font="fonts/PTSerif-Italic.ttf")

# This character is used when the assistant Pan is talking over the speaker in the interrogation room
define A = Character("Assistant", what_prefix='"', what_suffix='"', image="assistant", window_background=Frame("assistant_dialogue_box.png"), what_font="fonts/PTSerif-Italic.ttf")

# The assistant Pan
define a = Character("Assistant", what_prefix='"', what_suffix='"', image="assistant", window_background=Frame("assistant_dialogue_box.png"))

image assistant neutral:
    "images/Assistant_Neutral.png"
    size (597, 940)

image assistant neutral flip:
    "images/Assistant_Neutral.png"
    size (597, 940)
    xzoom -1

image assistant dark:
    "images/Assistant_Neutral_Dark.png"
    size (597, 940)

image assistant dark flip:
    "images/Assistant_Neutral_Dark.png"
    size (597, 940)
    xzoom -1

image assistant annoyed:
    "images/Assistant_Annoyed.png"
    size (597, 940)

image assistant annoyed flip:
    "images/Assistant_Annoyed.png"
    size (597, 940)
    xzoom -1

image assistant annoyed dark:
    "images/Assistant_Annoyed_Dark.png"
    size (597, 940)

image assistant annoyed dark flip:
    "images/Assistant_Annoyed_Dark.png"
    size (597, 940)
    xzoom -1

image assistant thinking:
    "images/Assistant_Thinking.png"
    size (597, 940)

image assistant thinking flip:
    "images/Assistant_Thinking.png"
    size (597, 940)
    xzoom -1

image assistant thinking dark flip:
    "images/Assistant_Thinking_Dark.png"
    size (597, 940)
    xzoom -1

image assistant shocked:
    "images/Assistant_Shocked.png"
    size (597, 940)

image assistant shocked flip:
    "images/Assistant_Shocked.png"
    size (597, 940)
    xzoom -1

image assistant shocked flip dark:
    "images/Assistant_Shocked_Dark.png"
    size (597, 940)
    xzoom -1

image assistant sideeye:
    "images/Assistant_Side_Eye.png"
    size (597, 940)

image assistant sideeye flip:
    "images/Assistant_Side_Eye.png"
    size (597, 940)
    xzoom -1

image assistant sideeye dark:
    "images/Assistant_Side_Eye_Dark.png"
    size (597, 940)

image assistant sideeye flip dark:
    "images/Assistant_Side_Eye_Dark.png"
    size (597, 940)
    xzoom -1


# The party boy Dionysus
define di = Character("Dionysus", what_prefix='"', what_suffix='"', image="dionysus", window_background=Frame("dionysus_dialogue_box.png"))

image dionysus neutral:
    "images/dionysus.png"
    size(736, 933)

image dionysus dark:
    "images/dionysus_dark.png"
    size(736, 933)

image dionysus tipsy:
    "images/dionysus_tipsy.png"
    size(736, 933)

image dionysus shocked:
    "images/Dionysus_Shocked.png"
    size(736, 933)

image dionysus shocked dark:
    "images/Dionysus_Shocked_Dark.png"
    size(736, 933)

# The Chief Valkyrie
define v = Character("Chief Valkyrie", what_prefix='"', what_suffix='"', image="valkyrie", window_background=Frame("valkyrie_dialogue_box.png"))

image valkyrie neutral:
    "images/valkyrie.png"
    size(727, 930)

image valkyrie dark:
    "images/valkyrie_dark.png"
    size(727, 930)

image valkyrie dark flip:
    "images/valkyrie_dark.png"
    size(727, 930)
    xzoom -1

image valkyrie salute:
    "images/valkyrie_salute.png"
    size(727, 930)

image valkyrie salute flip:
    "images/valkyrie_salute.png"
    size(727, 930)
    xzoom -1

image valkyrie neutral flip:
    "images/valkyrie.png"
    size(727, 930)
    xzoom -1

image valkyrie shocked flip:
    "images/Valkyrie_Shocked.png"
    size(727, 930)
    xzoom -1

image valkyrie shocked dark flip:
    "images/Valkyrie_Shocked_Dark.png"
    size(727, 930)
    xzoom -1

image valkyrie thinking:
    "images/Valkyrie_Thinking.png"
    size(727, 930)

image valkyrie thinking flip:
    "images/Valkyrie_Thinking.png"
    size(727, 930)
    xzoom -1

image valkyrie thinking flip dark:
    "images/Valkyrie_Thinking_Dark.png"
    size(727, 930)
    xzoom -1

image valkyrie sad flip:
    "images/Valkyrie_Sad.png"
    size(727, 930)
    xzoom -1

image valkyrie sad flip dark:
    "images/Valkyrie_Sad_Dark.png"
    size(727, 930)
    xzoom -1

# The pegasus Nimbus
define n = Character("Nimbus", what_prefix='"', what_suffix='"', image="pegasus", window_background=Frame("nimbus_dialogue_box.png"))

image pegasus neutral:
    "images/pegasus.png"
    # size()

image pegasus dark:
    "images/pegasus_dark.png"
    # size()

image pegasus neigh:
    "images/Nimbus Neighing.png"

image pegasus sad:
    "images/Nimbus_Sad.png"

image pegasus sad dark:
    "images/Nimbus_Sad_Dark.png"

image pegasus angry:
    "images/Nimbus Angry.png"

image pegasus angry dark:
    "images/Nimbus Angry Dark.png"

# The catgirl Bastet
define b = Character("Bastet", what_prefix='"', what_suffix='"', image="bastet", window_background=Frame("bastet_dialogue_box.png"))

image bastet neutral:
    "images/Bastet_Neutral.png"
    size (872, 948)

image bastet neutral flip:
    "images/Bastet_Neutral.png"
    size (872, 948)
    xzoom -1

image bastet thinking:
    "images/Bastet_Thinking.png"
    size (872, 948)

image bastet thinking flip:
    "images/Bastet_Thinking.png"
    size (872, 948)
    xzoom -1

image bastet defensive:
    "images/Bastet_Defensive.png"
    size (872, 948)

image bastet defensive flip:
    "images/Bastet_Defensive.png"
    size (872, 948)
    xzoom -1

image bastet shocked:
    "images/Bastet_Shocked.png"
    size (872, 948)

image bastet shocked flip:
    "images/Bastet_Shocked.png"
    size (872, 948)
    xzoom -1

image bastet annoyed:
    "images/Bastet_Annoyed.png"
    size (872, 948)

image bastet annoyed flip:
    "images/Bastet_Annoyed.png"
    size (872, 948)
    xzoom -1

image bastet neutral dark:
    "images/Bastet_Neutral_Dark.png"
    size (872, 948)

image bastet thinking dark:
    "images/Bastet_Thinking_Dark.png"
    size (872, 948)

image bastet defensive dark:
    "images/Bastet_Defensive_Dark.png"
    size (872, 948)

image bastet shocked dark:
    "images/Bastet_Shocked_Dark.png"
    size (872, 948)

image bastet annoyed dark:
    "images/Bastet_Annoyed_Dark.png"
    size (872, 948)


# The nurse Eir
define e = Character("Eir", what_prefix='"', what_suffix='"', image="eir", window_background=Frame("eir_dialogue_box.png"))

image eir neutral:
    "images/Eir General.png"
    size (576, 972)

image eir neutral flip:
    "images/Eir General.png"
    size (576, 972)
    xzoom -1

image eir happy:
    "images/Eir Happy.png"
    size (576, 972)

image eir happy flip:
    "images/Eir Happy.png"
    size (576, 972)
    xzoom -1

image eir defensive:
    "images/Eir Defensive.png"
    size (576, 972)

image eir defensive flip:
    "images/Eir Defensive.png"
    size (576, 972)
    xzoom -1

image eir shocked:
    "images/Eir Shocked.png"
    size (576, 972)

image eir shocked flip:
    "images/Eir Shocked.png"
    size (576, 972)
    xzoom -1

image eir neutral dark:
    "images/Eir_General_Dark.png"
    size (576, 972)

image eir happy dark:
    "images/Eir_Happy_Dark.png"
    size (576, 972)

image eir defensive dark:
    "images/Eir_Defensive_Dark.png"
    size (576, 972)

image eir shocked dark:
    "images/Eir_Shocked_Dark.png"
    size (576, 972)


# The character used for the officer that finds the IDs in the pegasus racing ring
define vks = Character("Valkyries", what_prefix='"', what_suffix='"', window_background=Frame("officer_dialogue.png"))
