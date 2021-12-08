# The label used to bring the player to the long-awaited accusation scene
label accusation:
    show black zorder 5 with fade

    show detective neutral at character_move_off_screen_left
    show assistant neutral at character_move_off_screen_left
    show valkyrie neutral at character_move_off_screen_left
    show pegasus neutral at character_move_off_screen_left

    show bastet neutral at character_move_off_screen_right
    show eir neutral at character_move_off_screen_right
    show dionysus neutral at character_move_off_screen_right

    pause 0.5
    hide black with fade

    show detective excited at character_move_middle with dissolve

    d "I've got it!"

    show valkyrie neutral flip at character_left
    with ease

    v "You do?"

    show detective smile at character_left
    show valkyrie dark flip at character_move_back_left
    show bastet annoyed at character_move_middle_back_right
    with ease

    b "Let's get on with it, then!"

    show bastet annoyed dark at character_move_back_back_right zorder 1
    show eir neutral at character_right zorder 2
    with ease

    e "This should be good."

    show bastet annoyed dark at character_move_off_screen_right
    show eir neutral dark at character_move_back_right zorder 1
    show dionysus tipsy at character_right zorder 2
    with ease

    di "Brooo!"

    show dionysus dark
    show detective smile dark
    show pegasus neigh at character_move_middle zorder 3 with ease

    n "Neigh!"

    show pegasus dark zorder 1
    show valkyrie dark flip at character_move_off_screen_left
    show detective smile dark at character_move_back_left
    show assistant neutral flip at character_left zorder 3
    with ease

    a "So detective, who is our culprit?"

    show assistant dark flip at character_move_back_left
    show detective smile at character_left zorder 3

    d "Based on all the evidence, the culprit is..."

    # Here all the characters move off the screen
    show detective smile at character_move_off_screen_left
    show assistant dark flip zorder 1 at character_5
    show pegasus dark zorder 1 at character_1

    # Except the suspects, they move into a sort of police lineup to allow the player to click on them via the accusation_buttons screen
    show dionysus neutral zorder 2 at character_2
    show eir neutral zorder 2 at character_3
    show bastet neutral zorder 2 at character_4
    with ease

    # This screen creates imagebuttons using the suspects' character sprites to allow the player to click on who they think is guilty
    show screen accusation_buttons
    show screen dark

    pause

# This label is jumped to if the player chooses Dionysus
label dionysus_accused:
    hide screen accusation_buttons
    hide screen dark

    show dionysus neutral at character_right
    show pegasus neutral at character_move_off_screen_right
    show eir neutral at character_move_off_screen_right
    show bastet neutral at character_move_off_screen_right
    show detective accusation at character_left
    with ease

    d "YOU!"
    di "{i}ME?{/i} Brooo, what are you talking about?"
    show detective smile
    d "Arel Farphine had gotten addicted to Ambrosia and wanted more."
    show detective thinking
    d "Unfortunately, you were only giving it to the racing jockeys, but his pegasus Thunder Cloud escaped so he couldn't race anymore."
    show detective neutral
    d "He asked to meet with you at your home, but when you met he threatened to go to the Valkyrie Force unless you gave him what he wanted."
    d "Having him holding it over you would 'kill the vibe' of your partying, so you decided to strike him with lightning."
    show detective thinking
    d "You went a little overboard and didn't want to get in trouble with your father, so you tried to muddle the investigation by placing evidence that would incriminate {i}all{/i} of you."

    show detective neutral
    show dionysus dark at character_move_back_right zorder 1
    show bastet neutral at character_move_middle_back_right zorder 2
    with ease

    b "That sounds like something he would do."

    show dionysus dark at character_move_off_screen_right
    show bastet dark at character_move_back_back_right zorder 1
    show eir neutral at character_right zorder 2
    with ease

    e "I agree."

    show detective dark at character_move_back_left zorder 1
    show valkyrie neutral flip at character_left zorder 2
    with ease

    v "Why am I not surprised?"

    show bastet dark at character_move_off_screen_right
    show eir dark at character_move_back_right zorder 1
    show dionysus neutral at character_right zorder 2
    with ease

    di "But how would I do that?"

    show valkyrie dark flip at character_move_back_left zorder 1
    show detective neutral at character_left zorder 2
    with ease

    d "Eir had her medical tools at the racing ring to use on the jockeys and there is no way Bastet didn't have a cat with her while she was tending to the pegasi."
    d "Which means you had access to everything."
    di "Nah bro, you got it all wrong."
    d "Valkyrie Force, take him awa-"

    hide detective with dissolve
    show dionysus shocked
    show eir shocked dark
    show valkyrie shocked flip dark
    show assistant shocked flip at character_left zorder 2
    with ease

    a "DETECTIVE!"

    show assistant shocked flip dark at character_move_back_left zorder 1
    show valkyrie shocked flip at character_left zorder 2

    v "WHAT ARE YOU DOING?! CALL AN AMBULANCE!"

    show black zorder 5 with fade

    hide assistant
    hide dionysus
    hide valkyrie
    hide eir

    D "Something... hit me... from behind..."
    D "Is this... the end..?"

    # The game ends with the detective being killed by Nimbus and a jump to the lose screen
    show lose_screen zorder 6 with fade
    pause
    # After the player views the lose screen, they move on to the credits
    jump credits

# This label is jumped to if the player chooses Eir
label eir_accused:
    hide screen accusation_buttons
    hide screen dark

    show eir neutral at character_right
    show dionysus neutral at character_move_off_screen_right
    show pegasus neutral at character_move_off_screen_right
    show bastet neutral at character_move_off_screen_right
    show detective accusation at character_left
    with ease

    d "YOU!"

    show eir defensive
    e "Are you saying {i}I{/i} did it?"
    show detective smile
    d "Exactly."
    show detective thinking
    d "Arel Farphine had gotten addicted to Ambrosia and wanted more. Only racers got any, but unfortunately for Arel, his pegasus Thunder Cloud had escaped so he couldn’t participate in the races."
    d "He asked you to give him some since you were his doctor and threatened to go to the Valkyrie force if you didn't give him what he wanted."
    show detective neutral
    d "If word of your involvement with the racing ring and the creation of Ambrosia got out, you would lose your medical license and your status as goddess of medicine."
    d "He was going to ruin your life, so you decided to ruin his."
    show detective thinking
    d "You lured him to Dionysus' penthouse with the promise of injecting Ambrosia directly into his veins for a new high."
    d "But instead, you killed him."
    show detective neutral
    d "Your medical skills and knowledge were probably very useful in getting the body into such a state."
    show detective thinking
    d "You needed to make your involvement less obvious in case your syringe was found."
    d "So, you decided to tamper with the investigation by placing evidence at the scene that would point to Bastet."

    show eir defensive dark at character_move_back_right zorder 1
    show bastet defensive at character_move_middle_back_right zorder 2
    with ease

    e "What a complete -"

    show bastet defensive dark at character_move_back_back_right zorder 1
    show eir defensive at character_move_back_right zorder 2

    e "This is crazy!"
    show detective smile
    d "Is it crazy?"
    d "Bastet probably had her cats with her while she was tending to the pegasi, making one of them an easy target."
    d "{i}And{/i} you are fully capable of bypassing Zeus' security system."
    d "So it doesn't seem crazy to me."
    e "This is crazy talk! Leopold, tell her it wasn't me!"
    d "Valkyrie Force, take her and her damn bir -"

    hide detective with dissolve
    show bastet shocked dark
    show eir shocked
    show assistant shocked flip at character_left zorder 2
    with ease

    a "DETECTIVE!"

    show assistant shocked flip dark at character_move_back_left zorder 1
    show valkyrie shocked flip at character_left zorder 2
    with ease

    v "YOU! {i}YOU'RE{/i} THE CULPRIT! HURRY, SOMEONE CALL AN AMBULANCE!"

    show black zorder 5 with fade

    hide assistant
    hide dionysus
    hide valkyrie
    hide eir

    D "Something... hit me... from behind..."
    D "Is this... the end..?"

    # The game ends with the detective being killed by Nimbus and a jump to the lose screen
    show lose_screen zorder 6 with fade
    pause
    # After the player views the lose screen, they move on to the credits
    jump credits

# This label is jumped to if the player chooses Bastet
label bastet_accused:
    hide screen accusation_buttons
    hide screen dark

    show bastet neutral at character_move_middle_back_right
    show dionysus neutral at character_move_off_screen_right
    show eir neutral at character_move_off_screen_right
    show pegasus neutral at character_move_off_screen_right
    show detective accusation at character_left
    with ease

    d "YOU!"

    show bastet defensive
    b "{i}Hissss!{/i}"

    show detective neutral

    d "Arel Farphine had gotten addicted to 'Amborsia' and the side effects were taking a toll on his mental and emotional state."
    show detective thinking
    d "Because of that, he was getting more and more abusive towards the pegasus he rode, Thunder Cloud."
    show detective neutral
    d "You felt bad and decided to help him escape."
    d "Without another pegasus to ride, he couldn't race, and thus couldn't get his fix of Ambrosia."
    show detective thinking
    d "He figured out you were the reason he couldn't race, so he threatened your cats unless you have him what he wanted."
    show detective neutral
    d "You told him to meet with you at Dionysus' penthouse under the guise that all the Ambrosia was kept there."
    show detective thinking
    d "But you real plan was to kill him with fire for threatening your cats."
    d "And since you also happen to be an Egyptian sun goddess, I think you are more than capable of burning the body to a crisp."
    show detective neutral
    d "You didn't want to get in trouble and get taken away from your cats, so you had planned to pin it on Dionysus from the beginning."
    d "But being worried about any loose cat hair being found, you decided to place evidence pointing to Eir as well, to remove suspicion from yourself."

    show bastet defensive dark at character_move_back_back_right zorder 1
    show dionysus neutral at character_right zorder 2
    with ease

    di "Woah, that is wiiiiiild!"

    show bastet defensive dark at character_move_off_screen_right
    show dionysus dark at character_move_back_right zorder 1
    show eir neutral at character_right zorder 2
    with ease

    e "You are one conniving little kitty."

    show dionysus dark at character_move_off_screen_right
    show eir dark at character_move_back_right zorder 1
    show bastet defensive at character_move_middle_back_right zorder 2
    with ease

    b "This is absolutely absurd!"
    show detective smile
    d "Is it absurd?"
    d "Eir had her medical tools at the racing ring to use on the jockeys, which you could easily steal."
    d "{i}And{/i} you are fully capable of bypassing Zeus' security system, which means you could easily pull this off."
    b "You fool! You have this all wrong!"
    d "Valkyrie Force, take this cat to the pou-"

    hide detective with dissolve
    show bastet shocked
    show eir shocked dark
    show valkyrie shocked flip dark
    show assistant shocked flip at character_left zorder 2
    with ease

    a "DETECTIVE!"

    show assistant shocked flip dark at character_move_back_left zorder 1
    show valkyrie shocked flip at character_left zorder 2
    with ease

    v "IT WAS {i}YOU!{/i} SOMEONE CALL AN AMBULANCE!"

    show black zorder 5 with fade

    hide assistant
    hide dionysus
    hide valkyrie
    hide eir

    D "Something... hit me... from behind..."
    D "Is this... the end..?"

    # The game ends with the detective being killed by Nimbus and a jump to the lose screen
    show lose_screen zorder 6 with fade
    pause
    # After the player views the lose screen, they move on to the credits
    jump credits

# This label is jumped to if the player chooses Nimbus
label pegasus_accused:
    hide screen accusation_buttons
    hide screen dark

    show pegasus neutral at character_move_off_screen_right
    show dionysus neutral at character_move_off_screen_right
    show eir neutral at character_move_off_screen_right
    show bastet neutral at character_move_off_screen_right
    show assistant dark flip at character_move_off_screen_left
    show detective accusation at character_left
    with ease

    d "YOU!"

    show detective accusation at character_move_off_screen_left
    show valkyrie shocked flip at character_left
    with ease

    v "Detective..."

    show valkyrie shocked flip dark at character_move_back_left zorder 1
    show assistant thinking flip at character_left zorder 2
    with ease

    a "Are you pointing at..."

    show valkyrie shocked flip dark at character_move_off_screen_left
    show assistant thinking dark flip at character_move_back_left zorder 1
    show detective smile at character_left zorder 2
    show pegasus neutral at character_4
    with ease

    d "Yes! The culprit is Nimbus!"

    show pegasus neutral at character_move_off_screen_right
    show eir neutral at character_right
    with ease

    e "The pegasus?"

    show eir dark at character_move_back_right zorder 1
    show bastet thinking at character_move_middle_back_right zorder 2
    with ease

    b "You have definitely lost it."

    show eir dark at character_move_off_screen_right
    show bastet thinking dark at character_move_back_back_right zorder 1
    show dionysus tipsy at character_right zorder 2
    with ease

    di "Oooo sick, a pegasus. We should go for a fly!"

    show dionysus neutral
    show assistant thinking dark flip at character_move_off_screen_left
    show detective smile dark at character_move_back_left zorder 1
    show valkyrie thinking flip at character_left zorder 2
    with ease

    v "Why would it be Nimbus?"

    show valkyrie thinking flip dark at character_move_back_left zorder 1
    show detective smile at character_left zorder 2

    d "Well, I believe our friend's name 'Nimbus' is actually just a nickname."
    d "It's short for Cumulonimbus..."

    show valkyrie thinking flip dark at character_move_off_screen_left
    show detective smile dark at character_move_back_left zorder 1
    show assistant flip at character_left zorder 2
    with ease

    a "Thunder Cloud."

    show assistant dark flip at character_move_back_left zorder 1
    show detective smile at character_left zorder 2

    d "Exactly."
    d "Nimbus here is our escaped pegasus. The same one that was ridden and abused by our victim, Arel Farphine."
    show detective thinking
    d "Arel had gotten addicted to Ambrosia and his emotional and mental states were getting worse and worse."
    d "He took his aggression out on his pegasus, Nimbus."
    show detective neutral
    d "Nimbus had enough and managed to escape, but that wasn't his last encounter with our victim."
    show detective thinking
    d "Since he couldn't race, Arel stopped getting his fix of Ambrosia and was getting more and more desperate."
    d "Nimbus knew about all this and decided to use Arel's addiction to lure him to Dionysus' penthouse where he could exact revenge against his abuser."

    show dionysus dark at character_move_back_right zorder 1
    show bastet thinking at character_move_middle_back_right zorder 2

    b "But if he just wanted revenge against the abusive elf, why did he bring us into this?"

    show dionysus neutral at character_move_off_screen_right
    show bastet thinking dark at character_move_back_back_right zorder 1
    show eir neutral at character_right zorder 2
    with ease

    e "I was wondering the same thing."
    d "Nimbus wanted revenge, not just against his abuser, but against the ones who were responsible for the situation he was in."
    d "You three are responsible for the abuse the pegasi endured, and in order to expose the racing ring and free the other pegasi, he left us a trail that led to you."

    show assistant dark flip at character_move_off_screen_left
    show detective smile dark at character_move_back_left zorder 1
    show valkyrie thinking flip at character_left zorder 2
    with ease

    v "But detective, Nimbus transferred from Zeus' guard."
    v "We have the paperwork to prove it. The timeline doesn't match up."

    show valkyrie thinking flip dark at character_move_back_left zorder 1
    show detective smile at character_left zorder 2

    d "I was wondering the same thing, but then I remembered the broken chains."

    show detective smile dark at character_move_back_left zorder 1
    show valkyrie thinking flip at character_left zorder 2

    v "The broken chains?"

    show valkyrie thinking dark at character_move_back_left zorder 1
    show detective smile at character_left zorder 2

    d "Only one pegasus escaped, but I started to wonder {i}why{/i} only one escaped?"
    d "The answer: only one of them went through the intense training required to be part of a god's personal guard."

    show detective smile dark at character_move_back_left zorder 1
    show valkyrie thinking flip at character_left zorder 2

    v "You mean..."

    show valkyrie thinking flip dark at character_move_back_left zorder 1
    show detective smile at character_left zorder 2

    d "Nimbus was always able to escape."
    d "He stayed willingly in order to race, but what he didn't sign up for was the abuse."

    show valkyrie thinking flip dark at character_move_off_screen_left
    show detective smile dark at character_move_back_left zorder 1
    show assistant thinking flip at character_left zorder 2
    with ease

    a "But how could he be a part of Zeus' personal guard and no one noticed he was gone for such a long time?"

    show assistant dark flip at character_move_back_left zorder 1
    show detective thinking at character_left zorder 2

    d "Well, if we look at the logs for Zeus' guard, I am sure we will see that Nimbus had gone on a sabbatical for a while."
    d "And I'm sure the logs will also say that he was injured on the job the day he returned."

    show assistant dark flip at character_move_off_screen_left
    show detective smile dark at character_move_back_left zorder 1
    show valkyrie thinking flip at character_left zorder 2
    with ease

    v "So he hid the injuries he got from Arel and pretended they were sustained on the job?"

    show valkyrie thinking flip dark at character_move_back_left zorder 1
    show detective smile at character_left zorder 2

    d "Exactly. He needed to get transferred to the Valkyrie Force, but being injured on your vacation would be too suspicious."

    show detective smile dark at character_move_back_left zorder 1
    show valkyrie thinking flip at character_left zorder 2

    v "But why transfer?"

    show valkyrie thinking flip dark at character_move_back_left zorder 1
    show detective smile at character_left zorder 2

    d "He knew the Valkyrie Force was looking into the racing ring and wanted to keep tabs on his enemies."
    d "Isn't that right, Nimbus?"

    show detective smile dark
    show eir neutral dark
    show pegasus neigh at character_move_middle zorder 3

    n "Neigh?"

    show pegasus dark zorder 1
    show detective smile

    d "Don't be scared, Nimbus. Speak up, I know you can."

    show valkyrie thinking flip dark at character_move_off_screen_left
    show detective smile dark at character_move_back_left zorder 1
    show assistant neutral flip at character_left zorder 2
    with ease

    a "Detective, I know you're new to the Realm of Myths, but pegasi can't ta-"

    show assistant shocked flip dark
    show eir shocked dark
    show bastet shocked dark
    show pegasus angry zorder 3

    n "You're a good, and very annoying detective, I'll give you that."

    show pegasus dark zorder 1
    show detective smile dark at character_move_off_screen_left
    show assistant shocked flip dark at character_move_back_left zorder 1
    show valkyrie shocked flip at character_left zorder 2
    with ease

    v "Nimbus you can talk?!"

    show valkyrie shocked flip dark
    show pegasus angry zorder 3

    n "Yes I can. And that {i}damn{/i} detective was right about everything."

    show pegasus dark zorder 1
    show valkyrie shocked flip

    v "But how..."

    show valkyrie shocked flip dark
    show pegasus angry zorder 3

    n "It's simple, really."
    n "I lured him to Dionysus' penthouse, which was easy for me since I was a part of Zeus' guard."
    n "I had Zeus' blessing, so I could get past the penthouse's security."
    n "Then I had planned to confront him about the abuse he inflicted on me."

    show pegasus dark zorder 1
    show valkyrie neutral flip

    v "I {i}meant{/i} how can you talk, but I guess we're moving straight to what happened."
    v "If you were just going to confront him, then how did he end up dead?"

    show valkyrie dark flip
    show pegasus angry zorder 3

    n "Well Chief, it turns out when you decide to confront your abuser the pain, fear, and trauma all mixes together and sends you into a blinding rage."
    n "And as a pegasus blessed by Zeus, blinding rage turns into-"

    show pegasus dark zorder 1
    show assistant dark at character_move_off_screen_left
    show valkyrie dark flip at character_move_back_left zorder 1
    show detective neutral at character_left zorder 2
    with ease

    d "Electrically charged hooves with a {i}lot{/i} of force behind them."

    show detective neutral dark
    show pegasus angry zorder 3

    n "Exactly, Miss Annoying Detective."
    n "I just got up on my hind legs and stomped, and stomped, and stomped, until I couldn't stomp anymore."
    n "The rest is like you said."

    show pegasus dark zorder 1
    show detective neutral dark at character_move_back_left zorder 1
    show valkyrie neutral flip at character_left zorder 2

    v "Nimbus..."

    show valkyrie dark flip at character_move_back_left zorder 1
    show detective neutral at character_left zorder 2

    d "Chief Valkyrie..."

    show pegasus dark zorder 1
    show detective neutral dark at character_move_back_left zorder 1
    show valkyrie sad flip at character_left zorder 2

    v "Nimbus..."
    v "Valkryie, arrest Nimbus for the murder of Arel Farphine."

    show valkyrie sad flip dark
    show pegasus sad zorder 3

    n "I'm sorry, Chief."

    show pegasus sad dark zorder 1
    show valkyrie sad flip

    v "I am too..."

    show valkyrie sad flip dark zorder 2
    show pegasus sad zorder 3

    n "My only regret is..."
    show pegasus angry
    n "THAT I DIDN'T GET TO STOMP THE REST OF YOU SO CALLED 'GODS' WHO ARE RESPONSIBLE."
    n "I HOPE YOU ALL ROT IN TARTARUS!"

    show pegasus angry dark zorder 2
    show valkyrie sad flip zorder 3
    v "Take him away."

    show detective neutral dark at character_move_off_screen_left
    show valkyrie sad flip dark at character_move_off_screen_left
    show eir shocked dark at character_move_off_screen_right
    show bastet shocked dark at character_move_off_screen_right
    with ease

    hide pegasus
    show nimbus_arrest
    with dissolve
    pause

    hide nimbus_arrest with dissolve

label post_arrest:
    show bastet annoyed at character_move_middle_back_right
    with ease
    b "Finally, we can leave!"

    show bastet annoyed dark at character_move_back_back_right zorder 1
    show eir happy at character_right zorder 2
    with ease

    e "Glad that's over."

    show bastet annoyed dark at character_move_off_screen_right
    show eir happy dark at character_move_back_right zorder 1
    show dionysus tipsy at character_right zorder 2
    with ease

    di "Siiiiick. Anyone wanna go for drinks?"

    show dionysus neutral
    show valkyrie neutral flip at character_left

    v "Not so fast, you three. You're coming with me."

    show eir happy dark at character_move_off_screen_right
    show dionysus dark at character_move_back_right zorder 1
    show bastet defensive at character_move_middle_back_right zorder 2
    with ease

    b "But the detective's case is closed."

    show valkyrie dark flip at character_move_back_left zorder 1
    show detective smile at character_left zorder 2
    with ease

    d "Yes, my murder case is closed."
    d "But now the Valkyrie Force has neough evidence to use agsinst you."

    show dionysus dark at character_move_off_screen_right
    show bastet defensive dark at character_move_back_back_right zorder 1
    show eir defensive at character_right zorder 2
    with ease

    e "What?!"

    show eir defensive dark at character_move_back_right zorder 1
    show bastet defensive at character_move_middle_back_right zorder 2

    b "What are you saying?"

    show eir defensive dark at character_move_off_screen_right
    show bastet defensive dark at character_move_back_back_right zorder 1
    show dionysus neutral at character_right zorder 2
    with ease

    di "So no drinks?"
    d "Chief Valkyrie, take it away."

    show detective smile dark at character_move_back_left zorder 1
    show valkyrie neutral flip at character_left zorder 2
    show dionysus shocked
    show bastet shocked dark

    v "Dionysus, Eir, and Bastet, you are under arrest for your involvement in the organization of illegal sports betting events, money laundering, and the creation and distribution of a controlled substance."
    v "You will also be facing charges for your crimes against the pegasi, which include multiple counts of illegal capturing, aiding and abetting pegasi abuse, and the infliction of severe mental and emotional trauma."
    v "Valkyrie, take them away!"

    show eir defensive dark at character_move_off_screen_right
    show dionysus shocked dark at character_move_off_screen_right zorder 1
    show bastet defensive at character_move_middle_back_right zorder 2
    with ease

    b "No! I can't go to jail, my precious kittens will be left all alone!"

    show dionysus dark at character_move_off_screen_right
    show bastet defensive dark at character_move_off_screen_right
    show eir defensive at character_right zorder 2
    with ease

    e "I can't go to jail! I'll lose my medical license!"

    show eir defensive dark at character_move_off_screen_right
    show dionysus shocked at character_right zorder 2
    with ease

    d "So we aren't going to party?"

    show dionysus neutral at character_move_off_screen_right
    show valkyrie neutral at character_move_off_screen_left
    show detective smile at character_right
    show assistant neutral flip at character_left
    with ease

    a "Good work on the case, detective."
    a "I had no idea it was Nimbus. He managed to hide his bloodlust so well."
    show assistant thinking flip
    a "When did you realize it was him?"
    d "When I realized that the clues weren't to cover up the real suspect, but were for us to uncover the racing ring."
    show assistant neutral flip
    a "So that's why the clues clearly pointed to those three."
    a "Nimbus wanted us to catch them. But he must have known that he would get caught too..."
    show assistant thinking flip
    a "Did he want to get caught?"
    show detective thinking
    d "I can’t say for certain, but the one piece of evidence that didn’t clearly point to those three was the pegasus shoe found at the penthouse."
    show detective smile
    d "I don't know if it was intentional, but something tells me that pegasus shoe is the glass slipper that would only fit Nimbus."
    show detective neutral
    a "So he wanted to get caught? And what do you mean by glass slipper?"
    d "Oh, it's just an old story from back on Earth."
    show detective neutral
    d "Anyway, I think I'm about to say something that I never thought I would say, and will probably never say again."
    show assistant thinking flip
    a "And that is?"
    show detective annoyed
    d "I think Dionysus had the right idea..."
    show detective smile
    d "Wanna go get a drink?"
    show assistant annoyed flip
    a "After a day like this, I could definitely use one."
    show assistant neutral flip
    d "Then it's settled. I've heard there is a good place to get drinks across the street from here."
    show detective thinking
    d "I wonder if they'll have Diet Bepper?"
    show assistant annoyed flip
    a "Detective, that's a soda from Earth, they won't have-"
    show assistant neutral flip
    a "Well, I didn't think a pegasus could talk, so maybe they {i}will{/i} have it."
    d "Yay! Another case closed for Detective Amelia O’Finnigan!"
    show detective thinking
    d "I wonder what's next?!"
    show detective excited
    d "Maybe one of the gods is a serial killer!"
    d "Oh! Or maybe there is a nymph trafficking ring that needs to be taken down!"
    d "Or maybe we can go after Zeus and his-"
    show detective smile
    show assistant annoyed flip
    a "Detetive, let's take it one step at a time..."

    # The game ends with the detective and assistant being successful in solving their case and going out for drinks afterward
    show win_screen zorder 6 with fade
    pause
    # After the player views the win screen, they move on to the credits
    jump credits

label credits:
    # Black dissolves in to get rid of the win/lose screen
    show black zorder 7 with dissolve
    pause 0.5

    # The credits image fades in and then starts to scroll up
    show credits picture at credits_start zorder 7 with dissolve
    show credits picture at credits_move
    # The MoveTransition allows you to set the move time
    with MoveTransition(30.0)
    # After the credits are done scrolling, the music starts to fade out
    stop music fadeout 1.0
    # After 5 seconds, the game fades to black then ends
    pause 5.0
    show black zorder 10 with dissolve
    pause 0.5

    # The return function ends the game by returning to the main menu
    # Any unsaved progress will be lost.
    return
