# The variable used to track whether the player skipped straight to the accusation or not
default skipped_to_accusation = False

# The label that brings the player to the final penthouse scene
label penthouse_final:

    scene penthouse_empty with dissolve
    play music "audio/interrogation.mp3" fadein 1.0

    show detective neutral at character_move_off_screen_left
    show assistant neutral at character_move_off_screen_left
    show valkyrie neutral at character_move_off_screen_left
    show pegasus neutral at character_move_off_screen_left

    show bastet neutral at character_move_off_screen_right
    show eir neutral at character_move_off_screen_right
    show dionysus neutral at character_move_off_screen_right

    show bastet annoyed at character_right with ease

    b "Why are we here?"

    show bastet annoyed dark at character_move_off_screen_right
    show eir defensive at character_right
    with ease

    e "Yes, why {i}are{/i} we here?"
    e "My little Leopold here is feeling under the weather, so I should really get going."

    show eir defensive dark at character_move_back_right
    show dionysus tipsy at character_right
    with ease

    di "Broooo, who's having a party? This is lit!"

    show valkyrie neutral flip at character_left with ease

    v "Dionysus, this is your house, and it is {i}not{/i} a party."
    show dionysus neutral
    v "And Eir, you're stuck here for now, so you can cut the crap about your damn bird."

    show dionysus dark at character_move_back_right
    show eir defensive at character_right zorder 2
    with ease

    e "Ugh, fine."
    v "And I think all of you should already know why you're here."

    show eir defensive dark
    show valkyrie dark flip
    show pegasus neigh at character_move_middle zorder 3
    with ease

    n "Neeeigh!"

    show pegasus dark zorder 1
    show valkyrie dark flip at character_move_back_left
    show detective smile at character_left zorder 2
    with ease

    d "That's right!"

    show valkyrie neutral flip at character_left zorder 2
    show detective smile dark at character_move_back_left

    v "Oh! Detective, Pan, you have arrived."

    show dionysus dark at character_move_off_screen_right
    show eir defensive dark at character_move_back_right
    show bastet annoyed at character_move_back_right zorder 3
    with ease

    b "Oh great, you again."

    show valkyrie dark flip at character_move_back_left zorder 1
    show detective smile at character_left zorder 2
    with ease

    d "Yes, it {i}is{/i} me again."
    show detective neutral
    d "Now, let's get right to it. Someone in this room has committed..."
    d "A murder!"
    b "And? Can you hurry up already?"
    b "I want to get back to my lovely little kittens."

    menu:
        "Fine! That takes all the fun out of this, but I'll cut to the chase.":
            # Sets the variable to true to know the player skipped to the accusation
            $ skipped_to_accusation = True
            jump accusation_screen
        "No! You will sit here and wait until I am done. And now I'm gonna take my time.":
            jump penthouse_final_continued

label penthouse_final_continued:
    show eir defensive at character_right zorder 3
    show bastet annoyed dark at character_move_back_back_right zorder 1

    e "Way to go, Bastet."

    show eir defensive dark at character_move_back_right zorder 1
    show bastet defensive at character_move_back_right zorder 3

    b "{i}Hisss!{/i}"

    show eir defensive at character_right zorder 3
    show bastet defensive dark at character_move_back_back_right zorder 1

    e "Oh, bite me!"

    show eir defensive dark at character_move_back_right zorder 1
    show bastet defensive at character_move_back_right zorder 3

    b "Keep talking and getting bitten will be the least of your worries!"

    show eir defensive dark at character_move_off_screen_right
    show bastet annoyed dark at character_move_back_back_right zorder 1
    show dionysus tipsy at character_right zorder 3
    with ease

    di "Y'all should grab a drink. Seems a little tense in here."

    show valkyrie dark flip at character_move_off_screen_left
    show detective neutral dark at character_move_back_left zorder 1
    show assistant annoyed flip at character_left zorder 3
    with ease

    a "Can you all be quiet!"

    show dionysus neutral
    show assistant dark flip at character_move_back_left zorder 1
    show detective neutral at character_left zorder 2
    with ease

    d "Thank you, Pan. Now, let's get started from the beginning."
    show detective notes
    d "My assistant and I were called in to investigate a murder that took place here in Dionysus' penthouse. The victim was an elf named Arel Farphine."

    show bastet annoyed dark at character_move_off_screen_right
    show dionysus dark at character_move_back_right zorder 1
    show eir neutral at character_right zorder 2
    with ease

    e "We know all of this already."
    show detective neutral
    d "And?"
    show eir defensive
    e "...."
    show detective notes
    d "Now that we have an understanding of the situation, I will continue."
    d "We spoke to Dionysus at the scene, although he wasn't very helpful."
    d "However, we found it intriguing that he claimed to not know anything except that the Ambrosia drug found at the scene belonged to him."
    d "Maybe he was too drunk to think of a better excuse, but I digress."
    show detective thinking
    d "He also seemed to know about the effects of the Ambrosia, saying that its effects make users feel like they're a god."
    d "So why would a god, who knew this already, want to try the drug?"
    show detective smile
    d "Shocker! He was lying. And he also lied about not knowing the victim."

    show dionysus tipsy at character_right zorder 2
    show eir defensive dark at character_move_back_right zorder 1

    di "Whaaat? Broooo, that's crazyyy!"

    show eir defensive dark at character_move_off_screen_right
    show dionysus dark at character_move_back_right zorder 1
    show bastet defensive at character_move_middle_back_right zorder 2
    with ease

    b "So he lied about the drugs and not knowing the victim."
    b "Clearly, he is the culprit. Arrest him so I can leave."
    show detective neutral
    d "Well, you might recall that all of you lied about not knowing the victim. But we have your ID badges from the racing ring which say otherwise."
    show bastet annoyed
    b "Oh..."

    show dionysus dark at character_move_off_screen_right
    show bastet annoyed dark at character_move_back_back_right zorder 1
    show eir defensive at character_right zorder 2
    with ease

    e "Well, the murder took place at this house, so clearly he is more involved in the murder!"
    e "I have nothing to do with it!"

    show eir defensive dark at character_move_back_right zorder 1
    show bastet defensive at character_move_middle_back_right zorder 2

    b "Same! I didn't kill him!"

    show eir defensive dark at character_move_off_screen_right
    show bastet defensive dark at character_move_back_back_right zorder 1
    show dionysus neutral at character_right zorder 2
    with ease

    di "I didn't kill anyone, unless they died of fun at one of my parties."
    di "Death can really kill the vibes of some parties."
    d "I hate to break it to you, but none of you are out of the woods just yet."
    show detective notes
    d "We found evidence at the scene of the murder and the pegasus stables that places each of you at both scenes."

    show detective neutral
    show dionysus dark at character_move_back_right zorder 1
    show bastet defensive at character_move_middle_back_right zorder 2

    b "I already told you I was barely involved with the racing ring. I just tended to the pegasi."
    b "But I had nothing to do with the elf's murder!"

    show dionysus dark at character_move_off_screen_right
    show bastet defensive dark at character_move_back_back_right zorder 1
    show eir neutral at character_right zorder 2
    with ease

    e "I was only involved with the racing ring for the money, and all I did was heal the jockeys!"
    show eir defensive
    e "Why would I kill someone?"

    show eir defensive dark at character_move_off_screen_right
    show bastet defensive dark at character_move_back_back_right zorder 1
    show dionysus neutral at character_right zorder 2
    with ease

    di "Brooo I was partying. And killing some dude would really kill the partying vibes."
    d "You are right. None of you seem to have any reason to kill Arel Farphine."
    d "But clearly someone did."

    menu:
        "And that is -":
            jump accusation

        "Without a reason, we had to take a closer look at the evidence.":
            jump penthouse_final_continued_2

label penthouse_final_continued_2:
    show detective notes
    d "The medical tools, the cat hair and collar, and the bottles of wine..."
    show detective neutral
    d "All of these were found at the murder scene as well as the pegasus stables."
    d "And they all clearly point to you three being involved in the murder."

    show dionysus dark at character_move_back_right zorder 1
    show bastet defensive at character_move_middle_back_right zorder 2

    b "I told you one of my cats went missing!"

    show dionysus dark at character_move_off_screen_right
    show bastet defensive dark at character_move_back_back_right zorder 1
    show eir defensive at character_right zorder 2
    with ease

    e "And my medical tools were stolen! So why do you still think we are involved?"
    e "Anyone could have stolen my tools and her cat in order to frame us."
    e "So why do you still think it's one of us? For all you know, some random street rat was trying to frame us!"
    d "Not that that charming personality of yours would keep anyone from wanting to frame you, but there {i}is{/i} a reason it has to be someone in this room."
    d "Zeus' security system."

    show bastet defensive dark at character_move_off_screen_right
    show eir defensive dark at character_move_back_right zorder 1
    show dionysus neutral at character_right zorder 2
    with ease

    di "What's Pops got to do with this?"
    d "Zeus owns this building, and with that, his powers act as a security system that will smite anyone who gets past the front desk without having his blessing or being accompanied by someone with his blessing."
    d "That is, anyone that isn't a god on a similar level as Zeus."
    show detective notes
    d "Knowing that, and the evidence found at the scene, narrows down our suspect list to those in this room right now."

    show eir defensive dark at character_move_off_screen_right
    show dionysus dark at character_move_back_right zorder 1
    show bastet defensive at character_right zorder 2
    with ease

    b "So you really think one of us murdered this elf?"
    show detective neutral
    d "Oh did I offend you? I’m sorry, please forgive me for thinking someone involved in illegally capturing, abusing, and racing pegasi to promote the drug they are selling could also be capable of murder."

    show dionysus dark at character_move_off_screen_right
    show bastet defensive dark at character_move_back_back_right zorder 1
    show eir neutral at character_right zorder 2
    with ease

    e "Selling drugs? What are you talking about?"
    d "We found evidence of the drug Ambrosia at both the murder scene and the stables."
    d "Plus, our victim Arel was arrested for riding under the influence not long before his murder."

    show eir neutral dark at character_move_back_right zorder 1
    show bastet annoyed at character_right zorder 2

    b "And what does an elf being on drugs have to do with us?"
    show detective thinking
    d "Well, the elf was a jockey at the races you organize."
    d "The drug he was using was found at the race track."
    show detective neutral
    d "So, my guess is, it was probably used as payment to keep the jockeys interested and quiet about the whole thing."

    show bastet annoyed dark at character_move_back_right zorder 1
    show eir defensive at character_right zorder 2

    e "This is ridiculous!"

    show eir defensive dark at character_move_back_right zorder 1
    show bastet defensive at character_right zorder 2

    b "First you accuse us of murder, and now you accuse us of being drug dealers."
    b "Why would we need to sell drugs?"

    menu:
        "You're right, our focus is the murder. And I believe the murderer is -":
            jump accusation
        "I'm not just accusing you of murder and selling drugs. I'm also accusing you of {i}making{/i} the drug!":
            jump penthouse_final_continued_3

label penthouse_final_continued_3:
    b "Are you serious?!"

    show eir defensive dark at character_move_off_screen_right
    show bastet defensive dark at character_move_back_back_right zorder 1
    show dionysus tipsy at character_right zorder 2
    with ease

    di "Woah, that sounds rad!"

    show bastet defensive dark at character_move_off_screen_right
    show dionysus dark at character_move_off_screen_right zorder 1
    show eir neutral at character_right zorder 2
    with ease

    e "Why would we make a drug?"
    d "You each have your reasons. Eir, you mentioned Leopold had an rare, unknown illness, correct?"
    e "And?"
    d "Well, my guess is that you were trying to make a cure for Leopold and stumbled upon what would be Ambrosia."
    d "Realizing the potential it had, you tried presenting it to the hospital board - but they wouldn't endorse any research into it because of the risks."
    d "So instead you went to Bastet, who is also the goddess of ointments, hoping that you could have a breakthrough with her help."
    show eir defensive
    e "...."

    show dionysus dark at character_move_off_screen_right
    show eir defensive dark at character_move_back_right zorder 1
    show bastet annoyed at character_move_middle_back_right zorder 2
    with ease

    b "Why would I get involved with her drug schemes?"
    d "You needed money because your café is on the verge of going bankrupt. Probably because you keep forgetting to open it..."
    show bastet defensive
    b "{i}Hissss!{/i}"

    show eir defensive dark at character_move_off_screen_right
    show bastet defensive dark at character_move_back_back_right zorder 1
    show dionysus tipsy at character_right zorder 2
    with ease

    di "Woah, y'all made that stuff? That's siiiiick!"
    d "You're not innocent, Dionysus."
    show dionysus neutral
    show detective thinking
    d "As someone who only parties, it would be hard to afford a place like this - unless {i}your father{/i} owns the building."
    d "My guess is Zeus was getting fed up with your behavior and was going to cut you off."
    d "You needed money without giving up your party lifestyle, and Eir and Bastet needed someone to take care of distribution and advertising."
    show detective smile
    d "And who better than the god of parties and intoxication to distribute and get word out about a new drug?"
    di "Woah..."
    d "And the pegasus races served as a way to fund and advertise the entire operation."
    show detective thinking
    d "Am I wrong?"

    di "...."

    show bastet defensive dark at character_move_off_screen_right
    show dionysus dark at character_move_off_screen_right zorder 1
    show eir defensive at character_right zorder 2
    with ease

    e "...."

    show dionysus dark at character_move_off_screen_right
    show eir defensive dark at character_move_back_right zorder 1
    show bastet defensive at character_move_middle_back_right zorder 2
    with ease

    b "...."
    show detective smile
    d "That's what I thought."
    show detective neutral
    d "So would one of you like to confess?"
    b "Fine! You're right. But I didn't kill him!"

    show bastet defensive dark at character_move_back_back_right zorder 1
    show eir defensive at character_right zorder 2

    e "Even {i}if{/i} what you said is true, that doesn't give us a reason to murder the jockey."

    show bastet defensive dark at character_move_off_screen_right
    show eir defensive dark at character_move_back_right zorder 1
    show dionysus neutral at character_right zorder 2
    with ease

    di "Broooo I just want to party. I didn't kill anyone."
    d "Well the evidence clearly points to one of you."
    show detective notes
    d "The murderer had to have access to Eir's medical tools, Bastet's cat, and Dionysus' wine and penthouse."
    d "They had to be able to bypass Zeus' security system and have a way to get the victim in the penthouse."
    show detective neutral
    d "The murderer is the only one who could do all these things."

    show detective neutral dark at character_move_back_left zorder 1
    show assistant neutral flip at character_left zorder 2

    a "Detective, all the clues point to the three of them, but all of the clues mean any of them could have been the culprit."
    a "And they could all bypass the security system."

    show assistant dark flip at character_move_back_left zorder 1
    show detective thinking at character_left zorder 2

    d "Yes, all the clues..."
    show screen dark
    D "Ambrosia, a syringe, cat hair, unusual scorch marks, broken glass, the pegasus shoe, more Ambrosia at the stables, pegasus whips, a broken wine bottle, a cat collar, a scalpel, the broken chains, the missing pegasus, the easily found ID cards..."
    D "All of these clues point to the three suspects in front of me, but it feels like I'm missing something."
    hide screen dark

    show detective neutral dark at character_move_back_left zorder 1
    show assistant neutral flip at character_left zorder 2

    a "Detective?"

    jump accusation
