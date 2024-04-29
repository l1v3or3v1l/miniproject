define p = Character("[player_name]")
define u = Character("Uncle")
define t = Character("Text Message")

label start:

    $ intelligence = 0, health = 0, socialSkills = 0, pornAddiction = 0

    $ player_name = renpy.input("What is your name ? (default: Anandu)")

    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name = "Anandu"

    # day starts
    label day:
        # wake up
        menu:
            "Go to Gym ?"
            "Yes":
                $ health += 1
            "No":
                $ health -= 1
                $ intelligence -= 1
        # goes to college
        menu:
            "Socialise ?"
            "Yes":
                $ socialSkills += 1
                $ intelligence += 1
            "No":
                $ socialSkills -= 1
        # return home and starts studying, encounters an explicit ad pop up
        menu:
            "Continue ?"
            "Yes":
                $ pornAddiction += 1
                $ health -= 1
                $ intelligence -= 1
            "No":
                $ pornAddiction -= 1
                # spends time with family
                $ socialSkills += 1
        # sleep
        jump day
                        