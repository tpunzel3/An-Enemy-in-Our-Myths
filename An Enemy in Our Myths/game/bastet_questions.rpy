# The label used when the detective starts interrogating Bastet
label bastet_questions:
    b "So why exactly am I here?"
    d "Well Bastet, there has been a murder."
    show bastet annoyed flip
    b "Aww, that's too bad."
    b "So why am I here?"
    d "There was a murder and we believe you are involved."
    show bastet thinking flip
    b "Well I'm not, so can I leave?"
    b "My precious cats are all alone at the café."

    menu:
        "Listen here you little-":
            show detective annoyed
            show bastet defensive flip
            hide interrogation_speaker
            show interrogation_speaker at speaker_bounce
            pause 0.5

            A "Detective!"
            d "Yeah, yeah, I know. Back to the questions."
            show bastet annoyed flip
            show detective thinking
        "That's not how this works.":
            d "You are a suspect in this case and we will be the ones to determine the extent of your involvement."
            d "So, if you are done interrupting me, I will begin asking the questions."
            show bastet annoyed flip
            b "Okay, fine. Get on with it then."
            show detective thinking


    menu:
        # If the player asked Dionysus about the time of the murder, this question will appear
        "Okay, what were you doing between 9 a.m. yesterday and 7 a.m. this morning?" if time_question:
            b "Oh wow. You have the time of death narrowed dow to a 22 hour time frame."
            b "Impressive... oh 'great detective'..."
            show detective neutral
            d "Drop the attitude and answer the question."
            show bastet thinking flip
            b "Fine. I woke up at 10 a.m. and went to open my café."
            b "Then I spent time with my darling kittens, had myself a little cat nap around 1 p.m., woke up at 5 p.m., and closed my café around 6 p.m."
            b "I went home to enjoy some spicy tuna around 7:30 p.m. and went to sleep by 8 p.m."
            b "I woke up {i}today{/i} at 1 p.m. to the Valkyrie waiting at my door, and now I am here wasting my time talking to you."
            show bastet annoyed flip
            show detective thinking
            d "So you run a café, but didn’t get up until 1 p.m.? Interesting."

        "Okay, where were you yesterday?":
            b "Oh my, asking the {i}big{/i} questions now, oh 'great detective'?"
            show detective neutral
            d "Will you just answer the question?"
            b "Oh, you're not even gonna ask for a time frame? What kind of detective..."
            show detective annoyed
            d "{i}Just answer the damn question!{/i}"
            show bastet thinking flip
            b "Okay. I spent my day at the café with all my precious little felines."
            d "Can anyone confirm your story?"
            b "Well, I was so distracted by my lovely little kitty cats that I forgot to turn on my open sign. So no one came to the café."
            show detective neutral
            d "Well that seems awfully convenient, and very unhelpful."
            show bastet neutral flip
            b "Well, that's too bad."
            show bastet annoyed flip
            b "Maybe you should stop wasting my time and get back to whatever it is you do."

        # If the player DID NOT ask Dionysus about the time of the murder, this question will appear
        "Okay, did you commit a murder between yesterday and this morning?" if time_question != True:
            b "Really, detective?"
            show detective neutral
            d "It was worth trying."
            b "That was you trying, detective?"
            show detective thinking
            d "Well, you haven't answered the question."
            show bastet defensive flip
            b "{i}NO!{/i}"
            b "You imbecile, I didn't commit a murder! Not yet, anyway!"
            b "But keep asking these ridiculous questions and that might change!"
            show detective neutral
            d "Sheesh, okay."
            show detective thinking

    menu:
        "Next question! Have you ever been to Dionysus' penthouse?":
            show bastet annoyed flip
            b "I can't say that I have?"
            show detective thinking
            d "Oh, really? Then why is there cat hair in his penthouse?"
            show bastet defensive flip
            b "I didn't realize that {i}I'm{/i} the detective now!"
            show bastet annoyed flip
            b "If I had to guess, I would say that a cat was in there."
            d "So you agree that the cat whose hair was there would have needed to be in the penthouse?"
            show bastet defensive flip
            b "Yes, how else would cat hair get there?"
            show bastet annoyed flip
            b "Really, you are pretty slow for a detective."
            show detective neutral
            d "Well, Goddess of cats, since you agree that the cat in question needed to be in the penthouse in order for it’s hair to be at the scene, would you care to explain why you were in his penthouse?"
            show bastet defensive flip
            b "What are you talking about?"
            d "The cat hair we found has been tested and is a perfect match for you!"
            show bastet thinking flip
            b "Oh, well I do go to plenty of parties."
            b "Perhaps one of them was at Dionysus' penthouse."
            show bastet neutral flip
            b "But that doesn't mean I committed a murder there."
            d "Oh, how convenient."
        "Next question! If I say 'underground pegasus racing ring,' does that mean anything to you?":
            show bastet annoyed flip
            b "Underground what? I've never heard of it?"
            d "Oh really?"
            show detective thinking
            d "Then why was there a cat collar at the illegal underground racing ring?"
            show bastet defensive flip
            b "What? Like I'm the only one in the Realm of Myths with cats?"
            show detective neutral
            d "The collar has an Egyptian inspired design and matches your look."
            show bastet annoyed flip
            b "That doesn't prove anything."
            d "It doesn't?"
            show bastet defensive flip
            b "{i}No,{/i} it doesn't."
            b "There are many reasons why that collar could be there!"
            show detective thinking
            d "Like what?"
            show bastet thinking flip
            b "Well, one of my cats went for a walk the other day, and when she returned she was missing her collar."
            b "I thought she had just lost it, but maybe your culprit took it."
            show detective neutral
            d "That sounds like a convenient story."
            show bastet annoyed flip
            b "Convenient or not, that's the truth."
            d "We will see about that."

    jump post_bastet_questions
