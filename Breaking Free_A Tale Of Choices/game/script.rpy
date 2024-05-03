define e = Character("[player_name]")
define m = Character("Mother")
image Ready=im.Scale("ready.png",1920,1080)
image Sleep=im.Scale("sleep.png",1920,1080)
image Readyhurry=im.Scale("readyhurry.png",1920,1080)
image Reached=im.Scale("reached.png",1920,1080)
image Silent=im.Scale("silent.png",1920,1080)
image Active=im.Scale("active.png",1920,1080)
image Return=im.Scale("return.png",1920,1080)
image Tv=im.Scale("tv.png",1920,1080)
image Gym=im.Scale("gym.png",1920,1080)
image Sleep1=im.Scale("sleep1.png",1920,1080)
image Study=im.Scale("study.png",1920,1080)
image Street=im.Scale("street.png",1920,1080)
image Club=im.Scale("club.png",1920,1080)


label start:

    $ intelligence = 0
    $ health = 0
    $ socialSkills = 0
    $ pornAddiction = 0

    $ player_name = renpy.input("What is your name ? (default: Anandu)")

    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name = "Anandu" 

    e "click to continue"
    $ renpy.movie_cutscene("./images/NEW.webm")

    $ day = 1
    scene black
    centered "{size=*3} Day [day] {/size}"

    scene alarm 
    play music "ring.mp3"
    menu:
        "Turn off the Alarm and wakeup":
            $ menu_flag=True
            stop music 
            scene Ready
            e "getting ready"

        "snooze the Alarm and sleep for some more time":
            $ menu_flag=False
            stop music 
            scene Sleep
            show mother 
            play sound "snore.mp3" 
            m" wake up [e]!"
            show mother at left
            play sound "ring.mp3"
            m"get ready son ! you are already late"
            stop sound
            scene Readyhurry
            e"getting ready"

    scene Reached
    e"finally reached college"
    menu:
        " Participate actively in discussions.":
            $ menu_flag=True
            scene Active
            $ socialSkills += 1
            $ intelligence += 1
            pause
        "Stay quiet and listen to the lecture.":
            $ menu_flag=False
            scene Silent
            $ intelligence += 1
            pause
    play sound"ring.mp3"
    "bell rings"
    scene Return
    stop sound
    e"returning to home"
    menu:
        "spend time at home":
            scene Tv
            "watching Tv"
            $ health -= 1
        "go to gym":
            scene Gym 
            "lifting weights"
            $ intelligence += 1
            $ health += 1
            scene Street
            "returning to home"
            scene black
            e"finally reached home"
    menu:
        "Concentrate on your textbooks and notes.":
            scene Study
            pause
            $ intelligence += 1
        "go to club and enjoy with friends":
            scene Club
            pause
            $ socialSkills += 1
            $ health -= 1
    scene Sleep1



    # # day 2- starts
    # $ day += 1

    # label day:
    #     scene black
    #     centered "{size=*3} Day [day] {/size}"
    #     # wake up
    #     menu:
    #         "Go to Gym ?"
    #         "Yes":
    #             $ health += 1
    #         "No":
    #             $ health -= 1
    #             $ intelligence -= 1
    #     # goes to college
    #     menu:
    #         "Socialise ?"
    #         "Yes":
    #             $ socialSkills += 1
    #             $ intelligence += 1
    #         "No":
    #             $ socialSkills -= 1
    #     # return home and starts studying, encounters an explicit ad pop up
    #     menu:
    #         "Continue ?"
    #         "Yes":
    #             $ pornAddiction += 1
    #             $ health -= 1
    #             $ intelligence -= 1
    #         "No":
    #             $ pornAddiction -= 1
    #             # spends time with family
    #             $ socialSkills += 1
    #     # sleep
    #     $ day += 1
    #     jump day
                        