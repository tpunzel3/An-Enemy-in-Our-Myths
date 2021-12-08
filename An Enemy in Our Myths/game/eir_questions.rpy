# The label used when the detective starts interrogating Eir
label eir_questions:
    show valkyrie neutral flip at character_table_left with moveinleft
    v "Detective, Eir has arrived."
    d "Okay, let her in."
    show valkyrie salute flip
    v "Roger."
    show valkyrie neutral
    show valkyrie neutral at character_move_off_screen_left with ease
    pause 1.0
    show eir happy flip at character_table_left zorder 2 with moveinleft

    e "Hello detective, how can I help you?"
    show detective neutral
    d "Well Eir, there has been a murder."
    show eir shocked flip
    e "Oh my, how can I help?!"
    d "We believe that you might be connected to the victim, and potentially the culprit."
    d "So we wanted to ask you a few questions."
    show eir neutral flip
    e "Oh, really? I'll try helping as best I can."
    d "We appreciate the cooperation."
    d "The last goddess we had in here was a real-"
    hide interrogation_speaker
    show interrogation_speaker at speaker_bounce
    pause 0.5
    A "Detective! Get to the questions."
    d "Right, sorry, let's get started."
    show detective notes

    menu:
        # If the player asked Dionysus about the time of the murder, this question will appear
        "Where were you between 9 a.m. yesterday and 7 a.m. this morning?" if time_question:
            e "I have been working mostly night shifts at the hospital this week, so I didn't get home from work until around 10 a.m. yesterday."
            e "And I'm embarrased to say I was sleeping most of the day."
            show detective thinking
            d "Did you have another night shift last night?"
            e "Well actually, last night little Leopold here was feeling a little under the weather, so I had to stay home to look after him."

            show eir_cottage with dissolve

            pause

            hide eir_cottage with dissolve

            show detective neutral
            d "Is he okay now? Should we get him some water?"
            e "He's okay for now... he has a rare medical condition that doesn't have a cure... but I will find it."
            d "Oh... I'm sorry to hear that."
            d "Well, let's get these questions out of the way so he can get some rest."
            show detective notes

        "Where were you yesterday?":
            e "Well, I spent most of the day at my cottage taking care of Leopold."
            e "He hasn't been feeling good, so I stayed home to take care of him."

            show eir_cottage with dissolve

            pause

            hide eir_cottage with dissolve

            show detective neutral
            d "I'm sorry to hear that. Is he feeling better?"
            e "It comes and goes. He has a rare illness and I’ve been working on a cure, but everything I’ve tried only helps for a little while."
            d "You are working on a cure? By yourself?"
            show detective thinking
            d "Why not look after him at the hospital?"
            e "As the Norse goddess of medicine, I am more than capable of finding a cure for my little bird here."
            e "Plus those damn doctors don't-"
            show eir shocked flip
            e "Oh my, I am so sorry. The fatigue must be getting to me."
            show eir neutral flip
            show detective neutral
            d "Oh, no worries... Let's get through these other questions so you can get home."
            show detective notes

        # If the player DID NOT ask Dionysus about the time of the murder, this question will appear
        "Did you commit a murder between yesterday and 7 a.m. this morning?" if time_question != True:
            show eir shocked flip
            e "Oh my! Isn't that a little too forward, detective?"
            show detective neutral
            d "Maybe, but I would like you to answer seriously."
            show eir neutral flip
            e "Well then, no, I did not commit a murder."
            e "I was much too busy making a cure for little Leopold here to commit a murder."

            show eir_cottage with dissolve

            pause

            hide eir_cottage with dissolve

            d "Okay then. That was pretty simple, let's move on."

    show detective notes
    menu:
        "So I hear you are a pretty prominent figure in the medical community; is that correct?":
            e "Well, I wouldn't call myself a prominent figure, but as the Norse goddess of medicine, I suppose some would look towards me for guidance."
            show detective thinking
            d "And I believe that, in the Realm of Myths, one of the perks of being a prominent member of the medical community is that you get your own customized tools, correct?"
            show eir defensive flip
            e "Yes. May I ask how this is relevant to your investigation?"
            d "Yes, I'll answer that in a moment. But first, could you please describe your customized medical tools?"
            show eir neutral flip
            e "They are a simple silver with my initial 'E' engraved in them."
            d "Do you keep track of your tools?"
            e "Yes. I'm the only one with access to them."
            show detective neutral
            d "Well, thank you for confirming our suspicions."
            show eir defensive flip
            e "What suspicions?"
            d "In the stables of the illegal pegasus racing ring, we found a medical grade scalpel that matches that description."
            show eir shocked flip
            e "The what?"
            d "The illegal pegasus racing ring."
            show detective thinking
            d "Does that ring any bells?"
            show eir neutral
            e "I'm sorry, I don't think it does."
            e "But that sounds just awful..."
        "Again, thank you for your cooperation. Let's see... Have you ever been to Dionysus' penthouse?":
            e "Dionysus' penthouse?"
            e "No, I don't think I have."
            show detective thinking
            d "Am I correct in assuming that as someone who works at the hospital, you have access to medical grade tools?"
            e "Yes..."
            d "Do all hospital staff have access to all the medical tools?"
            show eir neutral flip
            e "Well, the higher up doctors such as myself have our own customized tools that only we are allowed access to."
            d "And how have yours been customized?"
            e "All of my tools are made of a bright silver steel from my times as a Valkyrie."
            e "And they all have an 'E' engraved on them."
            d "And I assume you keep a tight lock on your medical grade tools?"
            show eir defensive flip
            e "Yes, only I have access to them."
            e "The cabinet I store them in is protected by my magic, preventing anyone else from accessing them."
            show detective neutral
            d "So just to be clear, you have customized medical tools that only you can access?"
            e "Yes..."
            e "May I ask how this is relevant to the case?"
            d "We found a syring at Dionysus' penthouse next to the victim. The syringe was medical grade, made out of steel, and had an 'E' engraved on the handle."
            show eir neutral flip
            e "Really? I don't think any of my tools are missing."
            e "I wonder how it got there?"

    show detective annoyed
    d "Cut the crap, Eir!"
    show eir shocked flip
    e "Oh my, detective. Whatever do you mean?"
    d "We know you are involved in the underground pegasus racing ring."
    d "We found your ID, along with Bastet's and Dionysus', at the ring."
    show eir defensive flip
    e "Damn it, why couldn't you have just said that from the beginning?!"
    show detective neutral
    d "Wait... what?"
    e "Using my patient voice is exhausting."
    show eir neutral flip
    e "So if you knew all of this already, why did you need me here?"
    d "The victim was a jockey at these races, so you could either be involved in the murder, or be a potential next victim."
    d "So we would like you to answer truthfully."
    show eir defensive flip
    e "I didn't murder anyone if that's what you want to know."
    d "That's great, but I'm asking the questions now."
    show detective thinking
    menu:
        "What is your involvement with the underground pegasus racing ring?":
            e "I was a doctor for the jockeys."
            d "The jockeys needed a doctor?"
            show eir neutral flip
            e "Well, when you're riding a pegasus that doesn't want to be ridden, a variety of accidents can happen."
            show detective neutral
            d "So the pegasi would fight back?"
            e "Not so much fighting, more like they would try to throw the jockey off or try to stomp them."
            show detective thinking
            d "Stomp them?"
            e "Yeah. That was one of the worst injuries that came to my table."
            e "The jockey almost lost an arm."
            d "So the pegasi were trying to escape and you stopped them?"
            e "All {i}I{/i} did was treat the jockeys and get my money."
            e "The jockeys were the ones that handled the pegasi."
            d "Money?"
            e "Leopold has a rare illness and it takes money to pay the hospital bills."
            show screen dark
            D "Hospital bills? I thought she was making a cure..."
            hide screen dark
            show detective neutral
            d "Okay, Eir. I think that's all the questions I have for you."
            show eir defensive flip
            e "Finally. What a waste of time."
            show eir defensive
            pause 0.5
            show eir defensive at character_move_off_screen_left with ease
        "What do you know about the victim, Arel Farphine?":
            show eir neutral flip
            e "The victim was Arel?"
            d "Yes. Did you know him well?"
            e "Not on a personal level, but he was the jockey that ended up on my table the most."
            e "His pegasus would always try to fight him off and it would lead to some pretty serious injuries, and probably brain damage."
            show detective thinking
            d "What do you mean by that?"
            show eir defensive flip
            e "Arel was very aggressive and overall seemed unstable."
            e "And it didn't help when we stopped..."
            show detective neutral
            d "Stopped what?"
            show eir defensive flip
            e "Oh, nothing. He just seemed to get more aggressive when he stopped racing."
            show detective thinking
            d "Why did he stop racing?"
            show eir neutral flip
            e "Not sure. I think it had something to do with his pegasus."
            e "What did they call him? 'Thunder' something."
            d "Thunder Cloud?"
            e "That sounds right."
            show eir defensive flip
            e "But I didn't interact much with the pegasi, so I don't know much about that."
            show screen dark
            D "She's acting stranger than before."
            hide screen dark
            show detective neutral
            d "Well Eir, I think that is all the questions I had for now."
            d "We'll be in contact if anything else comes up."
            e "Could you not? I have things to do."
            e "Let's go, Leopold."
            show eir defensive
            show eir defensive at character_move_off_screen_left with ease
            show detective annoyed
            d "Crazy a-"
            show interrogation_speaker at speaker_bounce
            A "DETECTIVE!"
            show detective neutral
            d "Yeah, yeah. I know..."
    show interrogation_speaker at speaker_bounce
    A "Detective, the chariot is ready to take us to the office."
    show detective smile
    d "Okay, time to solve this case."
    show detective smile flip
    show detective smile flip at character_move_off_screen_right with ease

    stop music fadeout 1.0
    show black zorder 10 with fade
    pause 0.5

    jump post_interrogation_office
