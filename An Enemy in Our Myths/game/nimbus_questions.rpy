# The label used when the detective is asking Nimbus questions
label nimbus_questions:

    menu:
        "Really?":
            show assistant neutral flip at character_left zorder 2
            show detective dark at character_move_back_left zorder 1
            a "Yes, Detective."
            a "Even in the Realm of Myths, only those in the medical profession are trusted with access to medical tools."
        "Ah yes, of course.":
            show pegasus neutral zorder 3
            show detective dark at character_left zorder 2
            show valkyrie dark at character_right zorder 2

    # show assistant dark flip at character_left zorder 2
    show valkyrie dark at character_right zorder 2
    show pegasus neigh zorder 3

    n "Neigh!"

    show pegasus dark zorder 1
    show valkyrie neutral at character_right zorder 2

    v "Great job, partner. Your first big case and you found a lead!"

    show detective thinking at character_left zorder 2
    show assistant dark flip at character_move_back_left zorder 1

    menu:
        "Ah yes, good work for your first case, Mr. Nimbus! Is this really your first case?":
            show pegasus neigh zorder 3
            show detective thinking dark at character_left zorder 2
            show valkyrie dark at character_right zorder 2

            n "Neeiigh."

            show pegasus dark zorder 1
            show valkyrie neutral at character_right zorder 2

            v "Yes, he recently transferred to the Valkyrie Force's investigation division."

            show detective thinking at character_left zorder 2

            d "Oh wow, where did he transfer from?"
            v "He used to be part of the Valkyrie Force's personal guard divison."

            menu:
                "Personal guard division?":
                    show assistant neutral flip at character_left zorder 2
                    show detective thinking dark at character_move_back_left zorder 1

                    a "The Valkyrie Force is split into multiple divisions."
                    a "Chief Valkyrie here is the head of the investigation division, which deals with all manners of criminal investigations."

                    show detective neutral at character_left zorder 2
                    show assistant dark flip at character_move_back_left zorder 1

                    d "Oh, I see!"
                    v "The personal guard division is assigned to protect and serve various high ranking gods and goddesses."
                    v "Nimbus here was part of Zeus' personal guard."

                    show detective thinking
                    menu:
                        "Zeus' personal guard? That sounds important. Why did he transfer?":
                            v "Nimbus was injured on the job, and they said that it could be a security risk having an injured member on the personal guard."
                            v "So he was transferred to the investigation division."

                            show pegasus neigh zorder 3
                            show detective thinking dark at character_left zorder 2
                            show valkyrie dark at character_right zorder 2

                            n "Neeeigh!"

                            show pegasus dark zorder 1
                            show detective smile at character_left zorder 2

                            d "Well, I'm happy to be working with you, Mr. Nimbus!"
                            jump post_nimbus_questions

                        "Zeus' personal guard seems like a lot of work.":
                            jump post_nimbus_questions

                "Wow, personal guard. That's impressive!":
                    jump post_nimbus_questions

        "Ah, yes. Good work for your first case, Mr. Nimbus!":
            jump post_nimbus_questions
