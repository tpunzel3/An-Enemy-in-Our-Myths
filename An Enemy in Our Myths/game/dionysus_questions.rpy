# These 6 variables are used to keep track of which questions the player has asked Dionysus
# They are used later in the game to affect which questions the player can ask Eir and Bastet
# Since the player can ask Dionysus multiple questions, they are also used to make sure the player can't ask him the same question twice
default broken_glass_question = False
default ambrosia_question = False
default pets_question = False
default time_question = False
default key_question = False
default victim_question = False

# This variable keeps track of how many questions that player has asked Dionysus
default dionysus_questions_total = 0


# The label used when the detective starts interrogating Dionysus
label dionysus_questions:

    show detective notes
    d "Where were you last night?"
    di "I was at this party some elves were throwing. It was wild!"

    menu:
        "How did you hear about this party?":
            di "I was at the bar down the street and bumped into some elves who were going to the party."
            di "They asked if I wanted to go, and as the god of parties, how could I refuse!?"
        "What time did you leave for the party?":
            # The player asked Dionysus the question about time, so the variable is set to true
            $ time_question = True
            di "I was out drinking at the bar down the street around nine and I didn't get back 'til they brought me here."
            show detective neutral
            d "So you were gone from 9 p.m. and the maid came in at 7 a.m."
            d "That leaves a pretty big gap for the time of death."
            di "9 p.m.? Broooo, I meant 9 a.m."
            d "You were at the bar at 9 a.m.? On a Tuesday?"
            show dionysus tipsy
            di "It's 5 o'clock somewhere, am I right?!"
            show detective annoyed
            show assistant sideeye flip dark
            d "Oh my gods..."

    show detective notes
    menu:
        "Okay. Do you have any idea who the victim is?":
            # The player asked Dionysus the question about the victim, so the variable is set to true
            $ victim_question = True
            di "I have no idea."
            show detective neutral
            d "So you weren't supposed to meet with anyone?"
            di "I don't think so."
            d "You don't think so?"

            show assistant sideeye flip at character_left zorder 2
            show detective dark at character_move_back_left zorder 1

            a "Detective, he is the god of wine and parties."
            a "I don't think he is ever of sound mind."

            show detective annoyed at character_left zorder 2
            show assistant dark flip at character_move_back_left zorder 1

            d "You're right. We aren't going to get anywhere relying on his memory."

        "There were no signs of a break-in, so did you give anyone your key?":
            # The player asked Dionysus the question about the key, so the variable is set to true
            $ key_question = True
            di "Key? I don't have a key."
            show detective neutral
            d "You don't have a key?"

            show assistant neutral flip at character_left zorder 2
            show detective dark at character_move_back_left zorder 1

            a "A lot of buildings in the Realm of Myths don't use keys."
            a "Usually if a god owns a building, you either need the blessing of that god in order to enter the building, or you need to be let in by a resident."

            show detective thinking at character_left zorder 2
            show assistant dark flip at character_move_back_left zorder 1

            d "Interesting. So the murderer and the victim would either need to have Zeus' blessing, or have been let in by another resident."

            show assistant neutral flip at character_left zorder 2
            show detective dark at character_move_back_left zorder 1

            a "Yes. Unless the murderer was a god on the same level as Zeus, or had his blessing, they would have been smited the minute they stepped past the lobby."

            show detective neutral at character_left zorder 2
            show assistant dark flip at character_move_back_left zorder 1

            d "That is some strict security."
            show detective thinking
            d "Then how were we able to get in without being smited?"

            show assistant neutral flip at character_left zorder 2
            show detective thinking dark at character_move_back_left zorder 1

            a "Our ID badges were blessed by the gods, so we are allowed entry to all buildings. Same with the Valkyrie Force."

            show detective neutral at character_left zorder 2
            show assistant dark flip at character_move_back_left zorder 1

            d "Oh, that's handy."

label dionysus_questions_2:
    show detective notes
    menu:
        # This question is only shown if the player hasn't asked it yet
        "We found evidence of broken glass, but the windows were fine. Any idea where the broken glass came from?" if broken_glass_question != True:
            # The player asked Dionysus the question about the broken glass, so the variable is set to true
            $ broken_glass_question = True
            # The question counter is incremented by one
            $ dionysus_questions_total += 1

            di "Oh, that was probably some wine or beer bottles."
            show assistant sideeye flip dark
            di "I mean, when you're turnt up, cleaning is the last thing on your mind."
            show detective annoyed
            d "I thought that was the case."

            # If the player has already asked two questions, then it moves on to the post_questions label
            # But if not, then it loops back to the dionysus_questions_2 label and allows the player to ask another question
            if dionysus_questions_total < 2:
                jump dionysus_questions_2
            else:
                jump post_questions

        # This question is only shown if the player hasn't asked it yet
        "We have found evidence of what we believe to be 'Ambrosia'. Do you know anything about it?" if ambrosia_question != True:
            # The player asked Dionysus the question about the Ambrosia, so the variable is set to true
            $ ambrosia_question = True
            # The question counter is incremented by one
            $ dionysus_questions_total += 1

            di "Uhhh... Naaaah brooo."
            show assistant sideeye flip dark
            di "I have never seen or heard of a drug like that before..."
            show detective neutral
            show assistant dark flip
            d "So you're telling me that the great god of wine, partying, intoxication, and insanity hasn't heard of this drug?"
            show assistant sideeye flip dark
            di "Yeah..."
            d "Well, it's impressive that you knew it was a drug when I just called it Ambrosia."
            show detective thinking
            d "I assumed you would have thought it was just the nectar of the gods."
            di "Well uh..."
            di "Okay... I know what Ambrosia is, but I was just..."
            show detective neutral
            d "Holding it for a friend?"
            di "Okay fine."
            di "I heard some rumors about Ambrosia at some parties and it sounded like it could be a good time, so I was planning to try it out."
            show detective notes
            d "So how exactly does Ambrosia work?"
            di "Well, I haven't used it... but they say just a little bit can make you feel invincible."
            di "You can run for days and you don't even feel like you need to eat or drink."
            show detective thinking
            d "So basically, it makes you feel like a god."
            di "Which is why they call it Ambrosia."
            show detective neutral
            d "'The nectar of the gods.'"
            show assistant sideeye flip dark
            di "Amazing isn't it?"
            show detective annoyed
            d "Yeah, amazing."
            show assistant dark flip
            show detective neutral
            d "Now tell me, god of parties and intoxication - a drug that does something so 'amazing' has to have major side effects."
            show detective notes
            d "So what are they?"
            di "Word on the street is that no one is sure about all the effects."
            di "But I have heard that it can really mess with your head."
            d "Mess with your head?"
            di "Like, you enter a blind rage, and after the effects wear off, you don't remember anything."
            di "It's wild."
            show detective thinking
            d "Hmm. So if Dionysus is actually innocent, then this could have been someone trying to get their hands on his stash."

            # If the player has already asked two questions, then it moves on to the post_questions label
            # But if not, then it loops back to the dionysus_questions_2 label and allows the player to ask another question
            if dionysus_questions_total < 2:
                jump dionysus_questions_2
            else:
                jump post_questions

        # This question is only shown if the player hasn't asked it yet
        "Do you have any pets?" if pets_question != True:
            # The player asked Dionysus the question regarding pets, so the variable is set to true
            $ pets_question = True
            # The question counter is incremented by one
            $ dionysus_questions_total += 1

            di "Pets?"
            show detective neutral
            d "Yes, pets. Particularly cats or a pegasus?"
            di "Cats or a pegasus?"
            di "Haha... No, why?"
            d "We found cat hair and a pegasus shoe in your penthouse."
            show detective thinking
            d "But we didn't find evidence anywhere else of you having a pet."
            show assistant sideeye flip dark
            di "Oh. Yeah, I don't have any pets."
            di "No idea how those could have gotten here."
            show assistant dark flip
            show detective neutral
            d "Okay then..."

            # If the player has already asked two questions, then it moves on to the post_questions label
            # But if not, then it loops back to the dionysus_questions_2 label and allows the player to ask another question
            if dionysus_questions_total < 2:
                jump dionysus_questions_2
            else:
                jump post_questions
