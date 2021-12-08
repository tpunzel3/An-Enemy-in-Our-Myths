# The following seven variables track which clues the detective and assistant have talked about
default ambrosia_asked = False
default broken_glass_asked = False
default body_asked = False
default cat_hair_asked = False
default pegasus_shoe_asked = False
default scorches_asked = False
default syringe_asked = False

# This variable tracks the total number of clues talked about
default clues_talked = 0
# This variable tracks if the player has talked about at least one clue
default at_least_one = False

# This variable tracks if the player talked about the clues at all
default talked_about_clues = False
# This variable tracks if the player talked about Dinysus at all
default talked_about_dionysus = False

# This variable tracks the total number of Dinoysus questions talked about
default questions_talked = 0

# The following 5 variables track which Dionysus questions the detective and assistant have talked about
default party_asked = False
default key_asked = False
default ambrosia_asked_2 = False
default victim_asked = False
default pets_asked = False

# This tracks if the player has talked about at least one Dionysus question
default at_least_one_2 = False

# The label used when the detective and assistant head back to the office to talk about the clues and Dionysus questions
label post_discovery_office:
    scene black with fade
    pause 0.5
    scene office with fade
    play music "audio/office.mp3" fadein 1.0

    show detective barf at character_left with dissolve
    d "I just can’t get over how disturbing that scene was. There was never anything that gruesome back on Earth!"
    d "Most crimes were your typical stabbing or shooting, and usually all of the body parts were in the same place."

    show assistant neutral at character_right with dissolve

    a "Well detective, you {i}are{/i} in the Realm of Myths."
    a "The criminals here can express their murderous tendencies in… more creative ways."

    show detective neutral
    d "Yeah, I guess you're right."
    show assistant thinking
    a "We should probably discuss our findings at Dionysus’ penthouse while we wait for the victim’s lab results."

    show detective thinking
    menu:
        "Okay! Let's discuss the clues we found.":
            jump looking_at_clues_first
        "Okay! So how are we feeling about our conversation with Dionysus?":
            jump talking_about_dionysus

# This label is used when the player looks at clues first
label looking_at_clues_first:
    show assistant thinking
    if talked_about_dionysus:
        a "Let’s move on to what we found at the scene."
    a "Some of the things we found were: the cat hair, a pegasus shoe, broken glass, the Ambrosia drug, the body, and the scorch marks around the body."
    show detective neutral
    d "And the medical grade syringe that Nimbus found."
    show assistant neutral
    a "Did anything stand out to you about these items?"
    jump looking_at_clues

# This label is used to loop back to, so the player can talk about all the clues
label looking_at_clues:
    show detective notes
    show assistant thinking

    # Once the player has talked about a clue, the varible is updated
    $ talked_about_clues = True

    menu:
        # The options only show up if they haven't been previously talked about
        "The Ambrosia..." if ambrosia_asked != True:
            # The number of clues talked about is incremented by one
            $ clues_talked += 1
            # The variables tracking which clues have been talked about are set to True
            $ ambrosia_asked = True
            # And since the player HAS talked about one clue, that variable is also set to True
            $ at_least_one = True

            a "What was strange about the god of intoxication having drugs in his home?"
            show detective neutral
            d "The strange part wasn't him having it, it was him saying that he had only just heard of it."
            show detective thinking
            d "I would think the god of intoxication would be all-knowing when it comes to drugs."
            show assistant neutral
            a "That is true, but I don't think Dionysus is all-knowing about anything."
            show detective neutral
            d "You're probably right about that, but I do think it's still suspicious."
            a "Yes. We must keep an eye on him."

            # If the player hasn't talked about all the clues
            if clues_talked < 7:
                # Then they jump back to the label looking_at_clues so they can ask about more clues
                jump looking_at_clues
            # If the player HAS talked about all the clues
            else:
                # But HASNT talked about Dionysus yet
                if talked_about_dionysus != True:
                    # Then the player jumps to the label to start talking about the Dionysus questions
                    jump talking_about_dionysus
                # If they HAVE talked about Dionysus already
                else:
                    # Then they've completed this part of the scene and move on to their post-talk talk
                    jump after_talking

        # The same logic is repeated for every clue
        "The body..." if body_asked != True:
            $ clues_talked += 1
            $ body_asked = True
            $ at_least_one = True

            show assistant neutral
            a "Yes I know, the body was gruesome."
            d "Not that..."
            show detective barf
            d "I mean it {i}was{/i} gruesome..."
            show detective thinking
            d "But the thing I found interesting was that the body was burnt beyond recognition, {i}and{/i} the torso was basically non-existent."
            d "This suggests they were crushed or hit by an extreme force."
            show assistant thinking
            a "That seems to be a tad excessive for a drug deal gone wrong."
            show assistant neutral
            a "I think one method of murder would have sufficed."
            d "This is looking less and less like a drug deal gone wrong and more like a crime of passion."
            show detective neutral
            d "Or in this case, a crime of true hatred."
            a "If we knew the victim's identity, that might fill in some of the holes in the story."

            if clues_talked < 7:
                jump looking_at_clues
            else:
                if talked_about_dionysus != True:
                    jump talking_about_dionysus
                else:
                    jump after_talking

        "The broken glass..." if broken_glass_asked != True:
            $ clues_talked += 1
            $ broken_glass_asked = True
            $ at_least_one = True

            show assistant thinking
            a "The broken glass?"
            show detective neutral
            d "The body was found on the balcony, so there weren't many windows, and the ones that were there weren't damaged."
            show detective thinking
            d "So where did the glass come from?"
            show assistant neutral
            a "That is true."
            show detective neutral
            d "But it {i}was{/i} Dionysus' penthouse, so that could also have just been a broken bottle."
            a "Yes, that might be the case. He might have mentioned something along those lines."
            show assistant thinking
            a "We should probably focus on the other clues for now."

            if clues_talked < 7:
                jump looking_at_clues
            else:
                if talked_about_dionysus != True:
                    jump talking_about_dionysus
                else:
                    jump after_talking

        "The cat hair..." if cat_hair_asked != True:
            $ clues_talked += 1
            $ cat_hair_asked = True
            $ at_least_one = True

            show assistant neutral
            a "The cat hair did seem out of place."
            show detective thinking
            d "And since Dionysus doesn’t have a cat, either the victim or the culprit had to have so much cat hair on them that that much fell off at the scene."
            a "That does seem like the only way, but it’s very unlikely."
            show detective neutral
            d "I agree."
            d "So, we are either looking for someone surrounded by cats, or..."
            a "Or what, detective?"
            show detective thinking
            d "It is possible that it was placed there."
            d "But if it was, the question is why?"
            show assistant thinking
            a "That is something to think about."

            if clues_talked < 7:
                jump looking_at_clues
            else:
                if talked_about_dionysus != True:
                    jump talking_about_dionysus
                else:
                    jump after_talking

        "The pegasus shoe..." if pegasus_shoe_asked != True:
            $ clues_talked += 1
            $ pegasus_shoe_asked = True
            $ at_least_one = True

            show assistant thinking
            a "Anything about it in particular?"
            show detective thinking
            d "Well, as far as I could tell, Dionysus had no reason to have a pegasus shoe in his house."
            d "Thus, it makes the most sense for it to belong to the victim."
            a "That's a fair point."
            show assistant neutral
            a "Hopefully the lab results will solve that problem."
            show detective neutral
            d "The pegasus shoe belonging to the victim would make the most sense."
            d "There is no reason for the culprit to have one and leave it."
            a "Sounds like a safe assumption."

            if clues_talked < 7:
                jump looking_at_clues
            else:
                if talked_about_dionysus != True:
                    jump talking_about_dionysus
                else:
                    jump after_talking

        "The scorch marks..." if scorches_asked != True:
            $ clues_talked += 1
            $ scorches_asked = True
            $ at_least_one = True

            show assistant thinking
            a "I also found the scorch marks to be quite strange."
            d "Yes, the area where the scorch marks were don't match up with where the victim's body was."
            a "I mean, it's possible that the victim was set on fire, flailed around, and ending up leaving the scorch marks."
            show detective thinking
            d "But then there should be scorch marks all over the place, not just in the few spots beside the body."
            d "Also, if the victim was set on fire, shouldn't the rest of the penthouse have caught fire?"
            show assistant thinking
            a "With how much alcohol is in there, I’m surprised that whole street is still standing."
            show detective neutral
            d "Exactly."
            show detective thinking
            d "But what if it wasn't a fire?"
            show assistant neutral
            a "That is an interesting theory, detective. The lab reports might help with that."

            if clues_talked < 7:
                jump looking_at_clues
            else:
                if talked_about_dionysus != True:
                    jump talking_about_dionysus
                else:
                    jump after_talking

        "The syringe..." if syringe_asked != True:
            $ clues_talked += 1
            $ syringe_asked = True
            $ at_least_one = True

            a "Yes, the syringe was interesting. Good thing Nimbus found it."
            show detective neutral
            d "Yeah, I can't believe we both missed it."
            show detective thinking
            d "But what was more interesting was the letter 'E' inscribed in the handle."
            d "'Cause like you said, all things medicine require clearance to get to."
            a "That is correct."
            a "I also believe that only those high up in the mdeical profession have customized medical tools."
            show detective neutral
            d "So, unless it was stolen, we should be looking for a prominent figure in the medical profession with an 'E' in their name."
            a "That seems like a good place to start."

            if clues_talked < 7:
                jump looking_at_clues
            else:
                if talked_about_dionysus != True:
                    jump talking_about_dionysus
                else:
                    jump after_talking

        # If at least one clue was talked about, the player can choose to skip talking about the rest and move on
        "That's all I can think of for now, let's move on." if at_least_one:
            if talked_about_dionysus != True:
                jump talking_about_dionysus
            else:
                jump after_talking

# The label used to jump to to talk about the Dionysus questions
label talking_about_dionysus:
    show detective neutral
    show assistant neutral
    d "Okay! So how are we feeling about our conversation with Dionysus?"
    a "I don't think there was anything too shocking."
    d "I would agree that talking to him seemed pretty useless. I mean, {i}men{/i}, am I right?"
    show assistant sideeye
    a "Detective..."
    show detective neutral
    d "I know, back to the case..."
    show assistant thinking
    a "Did you find anything he said to be particularly interesting?"

# The label used to jump to to loop, ensuring the player can talk about all the Dionysus questions
label talking_about_dionysus_questions:
    # This variable is update to confirm the player has talked about Dionysus
    $ talked_about_dionysus = True
    show detective notes
    show assistant thinking
    menu:
        # If the player has yet to talk about this questions asked to Dionysus
        "The party..." if party_asked != True:
            # Once the player asks the question, the corresponding variable is updated
            $ party_asked = True
            # Since the player has now talked about at least one question, this variable is updated
            $ at_least_one_2 = True
            # The number of Dionysus questions talked about is incremented by one
            $ questions_talked += 1

            show assistant neutral
            a "Yes, the party seemed a little too convenient."
            show detective neutral
            d "Yes, partying all day is a very convenient alibi."
            a "True, but it's Dionysus we are talking about."
            d "Yes, him partying all day isn't surprising."
            show detective thinking
            d "The part that surprises me is that someone else was throwing a party all day."
            show assistant thinking
            a "It {i}is rather{/i} inconceivable that someone else would be throwing a party all that time."
            show assistant neutral
            a "But then again, the elves can get a little wild."
            show detective neutral
            d "Really? Do you know from experience?"
            show assistant sideeye
            a "Detective......"

            # If the player hasn't talked about all the Dionysus questions
            if questions_talked < 5:
                # Then the loop back up
                jump talking_about_dionysus_questions
            # If they have talked about all the Dionysus questions
            else:
                # But have not yet talked about the clues
                if talked_about_clues != True:
                    # Then they move on to talking about the clues
                    jump looking_at_clues_first
                # If they have talked about the clues
                else:
                    # Then they move on to their post-talk talk
                    jump after_talking

        # The same logic applies to all the Dionysus questions that the player can talk about
        "The key..." if key_asked != True:
            $ key_asked = True
            $ at_least_one_2 = True
            $ questions_talked += 1

            show assistant thinking
            a "How so?"
            show detective neutral
            d "Like you said, only those blessed by Zeus can enter without being smited, but Dionysus claimed to not know the victim."
            show detective thinking
            d "So either the victim or culprit are blessed by Zeus, which means they knew each other well enough to let the other in, or Dionysus is lying."
            show assistant neutral
            a "Unfortunately, both of those are real possibilites."
            a "Hopefully we can find out the victim's identity soon."

            if questions_talked < 5:
                jump talking_about_dionysus_questions
            else:
                if talked_about_clues != True:
                    jump looking_at_clues_first
                else:
                    jump after_talking

        "The Ambrosia..." if ambrosia_asked_2 != True:
            $ ambrosia_asked_2 = True
            $ at_least_one_2 = True
            $ questions_talked += 1

            show assistant neutral
            a "The drug's effects are very mysterious."
            show detective thinking
            d "But I was thinking more along the lines of how Dionysus talked about it."
            show assistant thinking
            a "What do you mean?"
            show detective neutral
            d "Well, first he claimed to not know much about it, saying he wanted to try it."
            show assistant neutral
            a "That in itself is strange, for the god of intoxication to not know about a drug."
            a "And he did start listing off side effects which someone who only just heard of the drug wouldn't know."
            d "I do believe he was lying about his knowledge of Ambrosia."
            show detective thinking
            d "However, the thing I don’t understand is why he immediately claimed the drugs as his own instead of trying to pin it on the victim."
            show detective neutral
            show assistant thinking
            a "That {i}is{/i} very out of character for him."
            show assistant neutral
            a "We should definitely have the Valkyrie keep an eye on him."

            if questions_talked < 5:
                jump talking_about_dionysus_questions
            else:
                if talked_about_clues != True:
                    jump looking_at_clues_first
                else:
                    jump after_talking

        "The victim..." if victim_asked != True:
            $ victim_asked = True
            $ at_least_one_2 = True
            $ questions_talked += 1

            show assistant neutral
            a "Dionysus not knowing the victim does seem odd."
            show detective thinking
            d "The thing I don't understand is that it seemed like the victim was there for the Ambrosia."
            d "So were the victim and culprit working together to get the Ambrosia?"
            d "Were they both trying to get it and happened to run into each other?"
            d "If so, why didn't the culprit take it with them?"
            d "And if they were trying to steal Dionysus' stash, how did they know he had a stash?"
            d "Also, if they were just after the drug, and Dionysus didn't know them, why would they try to steal from a god living in Zeus' death trap of a building?"
            show assistant thinking
            a "That is a lot of unanswered questions."
            a "Really doesn't seem like the victim was your everyday drug thief."
            show assistant neutral
            a "We really need to find out the victim's identity."

            if questions_talked < 5:
                jump talking_about_dionysus_questions
            else:
                if talked_about_clues != True:
                    jump looking_at_clues_first
                else:
                    jump after_talking

        "The pets..." if pets_asked != True:
            $ pets_asked = True
            $ at_least_one_2 = True
            $ questions_talked += 1

            show assistant neutral
            a "Yes, why was there so much cat hair if Dionysus claims to not own a cat?"
            show detective thinking
            d "And where did the pegasus shoe come from?"
            d "There are just a lot of things that don't make sense about the situation."
            show assistant thinking
            a "If Dionysus was telling the truth, then the cat hair and pegasus shoe must have come from the culprit."
            show detective neutral
            d "Yeah, but how did so much cat hair end up in his house if he doesn't own one?"
            d "And who would just carry around a pegasus shoe?"
            d "It just doesn't make much sense."
            show assistant neutral
            a "It's our job to make sense of it. We must remain vigilant."

            if questions_talked < 5:
                jump talking_about_dionysus_questions
            else:
                if talked_about_clues != True:
                    jump looking_at_clues_first
                else:
                    jump after_talking

        # If at least one Dionysus question was talked about, the player can choose to skip talking about the rest and move on
        "I think that’s enough about Dionysus for now." if at_least_one_2:
            if talked_about_clues != True:
                jump looking_at_clues_first
            else:
                jump after_talking

# The label used to move on from talking about the clues or Dionysus questions
label after_talking:
    show detective neutral
    show assistant neutral

    v "{i}*Knock knock*{/i} Detective, it's Chief Valkyrie."
    d "Please come in."

    show detective neutral at character_move_middle_back_left
    show assistant neutral at character_move_middle
    with ease
    show valkyrie neutral at character_move_middle_back_right with moveinright


    v "Nice to see you again. This time I know the victim's identity."

    show detective excited

    menu:
        "Fantastic! Who is our mystery victim?":
            v "Our 'mystery victim' is named Arel Farphine."
        "Oh, thank the gods. We were getting nowhere! And the victim is?":
            show assistant sideeye
            a "Detective! Please be more professional."
            show assistant neutral
            show detective neutral
            d "Sorry. Chief Valkyrie, please share the victim's identity."
            v "His name is Arel Farphine."

    show detective thinking
    menu:
        "That's an interesting name. Where is he from?":
            v "He is an elf of Norse origins."
        "That sounds Norse. Is he Norse?":
            v "That is correct."
            show detective excited
            d "NICE!"
            show assistant annoyed
            a "DETECTIVE!"
            show detective neutral
            d "Oh sorry, please continue."
            v "It's fine. He's an elf of Norse origins."

    show detective smile
    show assistant neutral
    menu:
        "Great work! This should help clear up a lot of the questions I had!":
            v "I think this will clear up some of your questions, but it also makes thing more complicated."
            show detective neutral
            d "Oh... yay..."
            show assistant sideeye
            a "Detective."
            d "Sorry."
        "Finding out the victim's identity so fast is great. The case should be a breeze.":
            v "Sorry Detective, but I don't think that is going to be the case here."
            show detective neutral
            d "Oh no."

    menu:
        "So what is the story with our new friend Mr. Farphine?":
            v "First, I need to tell you about the underground pegasus racing ring."
            d "The what?"
        "Well, lay it on me. How complicated is this going to be?":
            v "I need to start by bringing you up to speed on the underground racing ring."
            d "Oh... {i}That{/i} complicated."

    v "For months now, the Valkyrie Force has been investigating an underground pegasus racing ring."
    show valkyrie thinking
    v "We recently found a potential location for the races, but we were waiting to make our move, until today."
    d "Sorry, I'm stuck on the underground racing ring."
    show detective thinking
    d "What exactly is it?"
    show valkyrie neutral
    v "To put it simply, a group has been capturing pegasi and forcing them to race so the bored, rich citizens of the Realm of Myths can bet on them for sport."
    show assistant thinking
    a "I heard rumors from some forest sprites, but you can never tell if they are telling the truth."
    show detective neutral
    d "When do you talk to forest sprites?"
    show assistant sideeye
    a "..."
    show assistant neutral
    a "Chief Valkyrie, you were saying?"
    v "Unfortunately, the rumors are true."
    v "As a Valkyrie, I am infuriated by the thought of the pegasi, who've been our trusted companions for so long, being captured, abused, and forced to race for the enjoyment of others."
    show detective neutral
    d "That's just terrible."
    show detective smile
    d "We will do anything we can to help!"
    v "Well actually, you are already helping."
    show detective thinking
    d "I take it that {i}this{/i} is where our victim, Arel Farphine, comes in."
    v "Correct. Farphine was a pegasus jockey in the underground racing ring."
    show valkyrie thinking
    v "The reason we got the results back so fast is because he was already in our system for a recent RUI."
    show detective thinking
    d "RUI?"
    show assistant thinking
    a "Riding under the influence."
    show assistant neutral
    show valkyrie neutral
    v "Particularly under the influence of wine and Ambrosia."
    show detective neutral
    d "That seems like an oddly specific combination."
    show detective thinking
    d "I guess we can move Dionysus to the top of our suspect list."
    show assistant thinking
    a "Should we pay him another visit?"
    show detective neutral
    d "The Valkyrie currently have him under surveillance."
    d "If he is more involved than I think he is, it would be better to gather more evidence first."
    v "Glad you think so. The Valkyrie Force is currently preparing to move on the location we believe to be the home of the pegasus racing ring."
    v "We were hoping you would join us, as it may prove to be useful for your current case."
    show detective smile
    show assistant neutral
    d "Solving a murder and taking down an underground pegasus racing ring?"
    d "Sounds like a typical Wednesday afternoon."
    v "Alright, then come with me."

    show black with fade
    pause 0.5

    stop music fadeout 1.0
    jump racing_ring
