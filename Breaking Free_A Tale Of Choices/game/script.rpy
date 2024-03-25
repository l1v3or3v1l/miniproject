define p = Character("[player_name]")
define u = Character("Uncle")
define t = Character("Text Message")

label start:

    $ usefulness = 0

    $ player_name = renpy.input("What is your name ? (default: Anandu)")

    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name = "Anandu"

    p "No way, Uncle! Is this for me?"

    u "Indeed it is, [player_name]. Happy 18th birthday!"

    p "I can't believe it! Thank you, Uncle. This is the best gift ever!"

    u "You deserve it, kiddo. I hope it helps you in achieving your goals."

    t "Hey [player_name]! We're planning to hang out tonight. You in?"

    p "[[Oh, nice! Just got a text from the gang. They're inviting me out tonight.]"

    menu:
        "Hang out with friends ?"
        "Yes":
            p "[[I text back, \"Definitely! I could use a break.\"]"
            $ usefulness += 1
        "No":
            p "[[I text back, \"I'm not sure... I have a lot on my plate right now.\"]"

    p "[[I ]"
    return