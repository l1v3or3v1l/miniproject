define p = Character("[player_name]")
define u = Character("Uncle")
define t = Character("Text Message")

label start:

    $ usefulness = 3

    $ player_name = renpy.input("What is your name ? (default: Anandu)")

    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name = "Anandu"

    p "No way, Uncle! Is this for me?"

    u "Indeed it is, [player_name]. Happy 18th birthday!"

    p "I can't believe it! Thank you, Uncle. This is the best gift ever!"

    u "You deserve it, kiddo. I hope it helps you in achieving your goals."

    label friends:

        t "Hey [player_name]! We're planning to hang out tonight. You in?"

        p "[[Oh, nice! Just got a text from the gang. They're inviting me out tonight.]"

        menu:
            "Hang out with friends ?"
            "Yes":
                p "[[I text back, \"Definitely! I could use a break.\"]"
                $ usefulness += 1
                "(I hang out with my friends and return Home)"
                jump learn
            "No":
                p "[[I text back, \"I'm not sure... I have a lot on my plate right now.\"]"

        label learn:
            "(I start browsing on my PC, found many educational websites)"

            menu:
                "You come across an explicit website ad, Visit website ?"
                "Yes":
                    label website:
                        "(Some time passes, I am still engrossed by this website)"
                        menu:
                            "Would u like to exit the website ?"
                            "Yes":
                                jump friends
                            "No":
                                $ usefulness -= 1
                                if usefulness < 0:
                                    "(You go searching for extreme content, encounters child pornography)"
                                    "(Moments later, police comes busting down your door, and then arresting you.)"
                                    return
                                jump website
                "No": 
                    $ usefulness += 1
                    jump conclusion
    
    label conclusion:
        if usefulness >= 5:
            "(Becomes rich and successful)"
        else:
            "(You have a decent life with moderate pleasures and pains of life.)"

    return