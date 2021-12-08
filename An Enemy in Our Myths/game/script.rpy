# This is the inventory array used to store the clues the player finds throughout the game
default inventory = []
# This is the variable used to keep track of which clue the player last clicked on in the inventory
default selected_item = None

# This array keeps track of Dionysus' penthouse clues
default dionysus_clues = []
# This array keeps track of the racing ring clues
default racing_ring_clues = []

#Start of game
label start:
    # All of these jumps are used for debugging purposes
    # The jump function allows you to move to a specific label
    #
    # jump post_nimbus_questions
    jump interrogation_room
    # jump post_discovery_office
    # jump dionysus_questions
    # jump penthouse1
    # jump racing_ring
    # jump post_questions
    # jump post_interrogation_office
    # jump penthouse2
    # jump eir_questions
    # jump penthouse_final
    # jump post_bastet_questions
    # jump accusation
    # jump debugging


    rando "AAAAAAAAAAAAAAAAAA"
    rando "What's going on?"
    rando "What happened?"
    rando "Oh no! Someone call the Valkyrie Force!"
    rando "What happened?!"
    rando "There has been a..."

    # The pause function allows you to pause the game for a certain interval, or if there's not defined time, until the player clicks to move on
    pause 0.5

    # Scene is similar to show in that it shows an image for the current scene you're in
    scene office
    with fade

    # The play function allows you to play music or sounds and can include transitions
    play music "audio/office.wav" fadein 1.0

    # The show function allows you to show images/character sprites on the screen
    # It allows the adding of locations, tranisitions, and zorder (layering)
    show detective thinking at character_left
    with dissolve

    # To have a character speak, you simply type their assigned 'name', then type the string you want them to say
    # In An Enemy In Our Myths:
    # rando = The random characters at the beginning of the game
    # d = Detective Amelia O'Finnigan
    # D = Detecetive thinking
    # a = Assistant Pan
    # A = Assistant using the interrogation room speaker
    # v = Chief Valkyrie
    # di = Dionysus
    # b = Bastet
    # e = Eir
    # n = Nimbus
    # vks = The officer that finds the IDs in the pegasus racing ring

    d "Murder at Dionysus's place? Is he the victim?"

    show assistant neutral at character_right
    with dissolve

    a "No Detective, he is not."
    show detective neutral
    d "Damn."
    d "You know how light my workload would be if he was out of the picture?"
    show assistant sideeye
    a "Detective!"
    a "Watch yourself."

    show detective thinking
    show assistant neutral

    # Ren'Py allows for easy option selection through its menus
    # Simply declare a menu, add strings for the different options, then add what you want to happen if the player were to choose that option
    menu:
        "Yeah, yeah, I know. But he's even Zeus' least favorite child and you know that's saying something.":
            show assistant sideeye
        "Yeah, okay, let’s get to the case.":
            show detective neutral
            jump start_continued


    a "Detective!"
    menu:
        "What? We all know those Greek myths have like a million kids.":
            show assistant annoyed
        "I know. Back to the case.":
            show detective neutral
            jump start_continued


    a "DETECTIVE!"
    d "And don't get me started on how they-"
    a "DETECTIVE!!!"
    show detective neutral
    d "Yeah, yeah, okay."
    d "So back to the case at hand."

# Different labels are used throughout the game as a sort of checkpoint
# You can jump to different labels in the code, so the game doesn't necessarily be in the perfect order, nor even in the same script
label start_continued:

    show assistant thinking
    a "At about midnight last night, Dionysus’ maid went up to clean while he went out to party."
    a "When she opened the door, she saw a corpse splattered on the floor, some of the walls, and on the-"
    show detective barf
    d "Okay, next please!"
    show assistant neutral
    a "Okay."
    a "The maid's scream alerted the others and they called the Valkyrie."
    show detective neutral
    d "So do they know who the victim is?"
    a "Not yet."
    show detective thinking
    d "So in theory, the victim could be Diony-"
    show assistant annoyed
    a "No!"
    show assistant neutral
    a "The Valkyrie found him passed out on the side of the road surrounded by wine bottles."
    show detective neutral
    d "Okay, fine."
    d "Make sure the Valkyrie keep an eye on him."
    d "I'll question him after we look around at the scene."
    show detective thinking
    d "Also, is the scene actually that bad...?"
    stop music fadeout 1.0



label penthouse1:

    scene penthouse_syringeless with fade
    play music "audio/penthouse.mp3" fadein 1.0
    pause 0.5

    show detective neutral at character_left
    with dissolve
    d "My GODS!"

    show detective barf

    d "That's a lot of....huuuugh..."
    d "I can't even tell what it... huuugh... is?"

    show assistant neutral at character_right
    with dissolve
    a "Detective, I explained it back at the office."

    show detective thinking

    d "I know, but I thought you were exaggerating!"
    show assistant annoyed
    a "Yes, because I always like to add some extra spice to a murder debriefing."

    hide assistant with dissolve
    show valkyrie neutral at character_right
    with dissolve

    v "Detective Amelia O'Finnigan, this way please."
    show detective neutral
    d "Right, sorry."
    show detective smile
    d "It's nice to see you again, Chief Valkyrie."
    v "Nice to see you too."
    v "This is an interesting case we have on our hands this time."
    show detective neutral
    d "Yeah, this crime scene is... interesting."
    show detective thinking
    d "Do you have any more information for us?"
    show valkyrie thinking
    v "Well, aside from what you know already, we haven't really found much else."
    show valkyrie neutral
    v "We are still waiting on the analysis of the... corpse..."
    show detective neutral
    d "Okay. I guess we will start looking around!"
    d "Chief Valkyrie, please make sure no one enters or leaves the building!"
    show valkyrie salute
    v "Roger!"
    show valkyrie neutral
    show valkyrie neutral flip at character_move_off_screen_right with ease
    hide valkyrie with dissolve
    show detective notes

    D "So, let's see what we have going on here..."

    # Inversely to the show function, the hide function will hide an image/character sprite
    hide detective with dissolve

    # You can create your own custom screens in Ren'Py and you can show them using the "show screen" function
    show screen dionysus_search_screen

    D "There doesn't seem to be any more useful information at the scene."
    show screen dark
    D "There doesn't seem to be any more useful information at the scene."

    hide screen dark
    pause 0.5

label penthouse2:
    show valkyrie neutral at character_right
    with dissolve

    v "Detective, my officers have arrived with Dionysus."

    show detective neutral at character_left
    with dissolve

    d "Okay great. You can have him wait."

    show valkyrie dark at character_move_back_right
    with moveinright

    show dionysus neutral at character_right

    di "Woah, what happened here?!"
    show detective annoyed
    d "Oh, Dionysus. Nice to see you again, I guess..."
    di "Ohhh!"

    show dionysus tipsy

    di "You were at my last party... man, that was a blast."
    show detective neutral
    d "Actually, I was called to your last party to investigate the disappearance of 600 gallons of ale from all the bars in the Realm of Myths!"

    show penthouse_party with dissolve

    pause

    hide penthouse_party with dissolve

    show dionysus tipsy
    di "Huh. Yeah, like I said, it was a blast."
    show detective annoyed
    d "A BLAST?!"
    d "I haven't even been in the Realm of Myths for a year yet, and I've already had seven cases that involve you!"
    d "I swear to the gods, I'mma-"

    show detective annoyed dark at character_move_back_left
    with ease

    show assistant annoyed flip at character_left
    with moveinleft

    a "DETECTIVE! The case!"

    show detective neutral at character_left zorder 2
    show assistant annoyed dark flip at character_move_back_left zorder 1

    d "Oh, right..."
    show assistant dark flip
    d "NOW IT'S EIGHT CASES THAT INVOLVE YOU!"

    show assistant annoyed flip at character_left zorder 2
    show detective neutral dark at character_move_back_left zorder 1

    a "Detective..."
    # In a string, you can surround a character/word/words with {i}{/i} to make them italicized
    a "I meant we should be investigating our {i}current{/i} case."

    show detective neutral at character_left zorder 2
    show assistant dark flip at character_move_back_left zorder 1

    d "Oh yeah, that..."
    di "Broooo, you should really chill out. You're killing the vibes of the party."
    show assistant sideeye flip dark
    d "Party?"
    di "Yeah brooo. This chick brought me here for your house party."
    di "Nice place you got, but you gotta do somethin 'bout that smell."
    di "Like geez, did something die in here?"

    show valkyrie neutral at character_right zorder 2
    show dionysus dark at character_move_back_right zorder 1

    v "Dionysus..."
    show assistant dark flip
    v "This is your house. And I brought you here because someone DID die."

    show dionysus neutral at character_right zorder 2
    show valkyrie dark at character_move_back_right zorder 1

    di "Wooah, this is my house? Siiick!"

    show valkyrie neutral at character_right zorder 2
    show dionysus dark at character_move_back_right zorder 1

    v "Also, I don't care if you're a god, call me chick again and you won't be able to drink ever again."

    show dionysus neutral at character_right zorder 2
    show valkyrie dark at character_move_back_right zorder 1

    di "Yes ma'am, sorry ma'am."

    show screen dark
    D "Woah. She can threaten a god like that and they listen... I love her, but she's also scary."
    hide screen dark
    d "We need to find the culprit fast and something tells me this isn’t going to get us anywhere, but Dionysus we need to ask you a few questions."
    di "Really? About what?"
    d "The MURDER that happened at YOUR penthouse! Are you fu-"

    show assistant annoyed flip at character_left zorder 2
    show detective neutral dark at character_move_back_left zorder 1

    a "DETECTIVE! The questions."

    show detective neutral at character_left zorder 2
    show assistant dark flip at character_move_back_left zorder 1

    d "Okay, Dionysus."
    show screen dark
    D "Here goes nothing..."
    hide screen dark
    jump dionysus_questions

label post_questions:
    d "Well Dionysus, I guess that was... helpful."
    di "Siiiick!"
    di "So how long 'til this mess is cleaned up? I'm thinking of throwing a party tonight."
    show detective annoyed
    d "A party? Tonight?! There is literally a dead body in your house!"
    di "Oh, riiiight..."
    show dionysus tipsy
    di "Broooo, the party could be spooky-themed. Then the body can just be a part of the vibes."
    d "Are you serious?!"
    d "NO! You cannot throw a party in here."
    show detective neutral
    d "I'm sure since you're one of Zeus' kids you can find another penthouse to party in for tonight."
    d "I mean, he does own the building."
    show dionysus neutral
    di "He cut- I mean..."
    show dionysus tipsy
    di "Broooo, you're riiiight."
    di "I should start getting all the booze together. This is gonna be another rager!"
    show detective annoyed
    d "Are you serious?!"

    show assistant sideeye flip at character_left zorder 2
    show detective annoyed dark at character_move_back_left zorder 1

    a "Detective, did you really expect the god of wine and partying to do anything besides boondoggling around?"

    show detective neutral at character_left zorder 2
    show assistant dark flip at character_move_back_left zorder 1

    d "What does that even-"

    scene penthouse_clued
    show pegasus neigh zorder 3
    show detective neutral dark at character_left zorder 2
    show assistant dark flip at character_move_back_left zorder 1
    show dionysus dark at character_right zorder 2
    show valkyrie dark at character_move_back_right zorder 1

    n "Neiiiiighhhhhhh!"

    show detective neutral at character_left zorder 2
    show pegasus dark zorder 1

    d "What?! How did a pegasus get in here?!"

    show valkyrie neutral at character_right zorder 2
    show dionysus dark at character_move_back_right zorder 1

    v "Sorry, Detective. That is Nimbus, my new partner."
    v "He just started, so he doesn't know all the protocols for working a crime scene."

    show pegasus neutral zorder 3
    show detective neutral dark at character_left zorder 2
    show valkyrie dark at character_right zorder 2

    n "Neiiiiighhhhhhh!"

    show assistant neutral flip at character_left zorder 2
    show detective neutral dark at character_move_back_left zorder 1
    show pegasus dark zorder 1

    a "Detective, he seems to have found something!"

    show detective neutral at character_left zorder 2
    show assistant dark flip at character_move_back_left zorder 1

    # This will append the inventory array to include the syringe clue after Nimbus has found it
    $ inventory.append(syringe)

    d "Hmmmm. Is that a syringe?"
    show detective thinking
    d "How did we miss that?"

    show valkyrie neutral at character_right zorder 2

    v "This looks like it's medical grade - not your average doping syringe."
    v "Even if he is a god, Dionysus wouldn't be able to get his hands on something like this."
    v "Only someone who works in the medical field could get their hands on it."

    jump nimbus_questions

label post_nimbus_questions:
    show assistant neutral flip at character_left zorder 2
    show detective smile dark at character_move_back_left zorder 1
    show pegasus dark zorder 1

    a "Now back to the case at hand."
    show assistant thinking
    a "This syringe narrows down potential suspects to someone with access to medical tools, but there are tons of gods, goddesses, and other mythological creatures with connections to the medical field."

    show detective neutral at character_left zorder 2
    show assistant thinking dark flip at character_move_back_left zorder 1

    d "Yeah, you're right."
    show detective thinking
    d "We should probably head back to the office for now to look over the clues we have so far while we wait for lab results to learn the victim's identity."

    show valkyrie neutral at character_right zorder 2

    v "We'll go check in with the coroner."
    v "As soon as we get the results we'll bring them to your office."
    show detective neutral
    d "Thank you, Chief Valkyrie. And you too, Mr. Nimbus!"

    show pegasus neigh zorder 3
    show detective neutral dark at character_left zorder 2
    show valkyrie dark at character_right zorder 2

    n "Neeeiiigh!"

    show assistant neutral flip at character_left zorder 2
    show detective neutral dark at character_move_back_left zorder 1
    show pegasus dark zorder 1

    a "Detective, the chariot has arrived."

    show detective neutral at character_left zorder 2
    show assistant dark flip at character_move_back_left zorder 1

    d "Okay then, let's go."

    jump post_discovery_office
    stop music fadeout 1.0

label interrogation_room:
    scene black with fade
    pause 0.5


    # To create the layered effect of the interrogation room, we had to have all of the furniture and tech on the walls on separate layers
    scene interrogation_background
    show interrogation_chair zorder 1
    show interrogation_table zorder 3
    show interrogation_lamp zorder 4
    show interrogation_speaker zorder 6
    with fade
    play music "audio/interrogation.mp3" fadein 1.0



    show detective neutral at character_table_right zorder 5 with dissolve

    show valkyrie neutral flip at character_table_left zorder 2 with moveinleft
    show interrogation_files zorder 3 with dissolve
    v "Detective, here are the lab results you requested, and Bastet has arrived."

    d "Okay, thanks. You can let her in."

    show valkyrie salute flip
    v "Roger."
    show valkyrie neutral
    show valkyrie neutral at character_move_off_screen_left with ease
    pause 1.0
    show bastet neutral flip at character_table_left zorder 2 with moveinleft

    jump bastet_questions

label post_bastet_questions:
    show detective annoyed
    d "I guess we should stop messing around and cut to the chase."
    show detective neutral
    d "We know you're connected to the underground pegasus racing ring, the victim, and possibly the culprit."
    show bastet defensive flip
    b "What are you talking about?"
    b "Clearly you're delusional. I just told you-"
    show detective notes
    d "We found your ID at the pegasus racing ring."
    show bastet thinking flip
    b "{i}Oop...{/i}"
    show detective thinking
    d "So even if you are not the culprit, you could be a target."
    d "So for your safety, you need to answer my next question truthfully."
    show bastet defensive flip
    b "Okay fine..."
    menu:
        "Okay then. What is your involvement in the pegasus racing ring?":
            show bastet thinking flip
            b "I was brought in as a partner for the organizer."
            b "My main job was to act as the vet."
            d "The vet?"
            show bastet neutral flip
            b "Yes, the vet. Although I am not the biggest fan of pegasi, the organizer believed that my cat expertise and affinity with medicinal ointments would be of value."
            show bastet annoyed flip
            b "It might be hard to believe, but the pegasi in the underground racing ring tend to get injured."
            show detective neutral
            d "How are they getting so injured that they need a vet?"
            b "Well, there are many ways they tend to get injured."
            show bastet thinking flip
            b "Usually fatigue or getting whipped by the riders. And many get injured trying to break off their chains."
            show detective thinking
            d "So you capture pegasi, force them to race, abuse them, keep them chained up, then just fix them enough to race again?"
            show detective neutral
            d "How despicable."
            show bastet defensive flip
            b "To be clear, I'm only here to patch them up and get my money."
            b "I am not involved in all those barbaric practices."
            show detective thinking
            d "You do it all for money?"
            show bastet annoyed flip
            b "Yes. Unfortunately, getting distracted by my darling little kittens and forgetting to turn on my open sign is a frequent occurrence."

            show bastet_cafe with dissolve

            pause

            hide bastet_cafe with dissolve

            b "As you can imagine, a cat café that is closed most of the time isn't making much money."
            show detective annoyed
            d "I... Okay."
            show detective neutral
            d "I think I'm done asking you questions for now."
            show bastet neutral flip
            b "Oh thank me, I can finally go back to my kittens."
            show bastet neutral at character_move_off_screen_left with ease
            pause 1.0
            jump eir_questions

        "Okay then. What do you know about the victim, Arel Farphine?":
            show bastet neutral flip
            b "I don't know much about him personally."
            show bastet thinking flip
            b "Besides that he was the jockey for the pegasus they called Thunder Cloud."
            show detective neutral
            d "That's all you know?"
            show bastet thinking flip
            b "I was only there to act as a vet for the pegasi, so I didn't interact with the jockeys."
            b "I guess the only other thing I could tell you is that he had some serious anger issues because of the... anyways, he took his problems out on the pegasus."
            b "The pegasus was always in my medical room with all manner of bruises and lacerations."
            show detective thinking
            d "And you just kept forcing them to race?"
            show bastet defensive flip
            b "Like I said, I was just the vet."
            show bastet annoyed flip
            b "I did my job, got my money and went back to my cafe to spend time with my precious little kitty cats."

            show bastet_cafe with dissolve

            pause

            hide bastet_cafe with dissolve

            b "I wasn't about to start asking questions."
            d "What about Thunder Cloud? What else can you tell me?"
            show bastet thinking flip
            b "Not much. He was one of the better racers and went by the name Thunder Cloud because when he ran, sparks flew from his hooves and the flap of his wings sounded like roaring thunder."
            D "Thunder Cloud..."
            show detective neutral
            d "Okay, I think I'm done asking you questions for now."
            show bastet neutral flip
            b "Oh thank me, I can finally go back to my café."

            show bastet neutral at character_move_off_screen_left with ease
            pause 1.0
            jump eir_questions
