define e = Character("[player_name]")
define m = Character("Mother")
define d = Character("Dad")
define f = Character("Friend")
define t = Character("Trainer")
define u = Character("Uncle")
define fa = Character("Family")
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

    show char in:
        xpos 0.7
        ypos 0.29
    # Yawns
    e "Another day, another early start."
    hide char in
    stop music
    show mother:
        xpos 0.1
        ypos 0.21
    m "Good morning, Ethan. Breakfast is ready."
    hide mother
    show char in:
        xpos 0.7
        ypos 0.29
    e "Thanks, Mom. I'll be down in a minute."
    hide char in
    show father:
        xpos 0.7
        ypos 0.22
    d "Don't forget to grab your lunch before you go."
    hide father
    show char in:
        xpos 0.7
        ypos 0.29
    e "Got it, Dad. Thanks."

    scene Reached
    show friend:
        xpos 0.7
        ypos 0.29
    f "Hey, Ethan! Ready for another day of classes?"
    hide friend
    show char college:
        xpos 0.7
        ypos 0.29
    e "Ready as I'll ever be. How about you?"
    hide char college
    show friend:
        xpos 0.7
        ypos 0.29
    f  "Same here. Let's try to make the most of it."
    hide friend

    scene Gym
    show trainer:
        xpos 0.1
        ypos 0.3
    t "Looking good, Ethan! Keep up the great work."
    hide trainer
    show char out:
        xpos 0.7
        ypos 0.29
    e "Thanks, Coach. I'm trying to stay on track."
    hide char out
    show trainer:
        xpos 0.1
        ypos 0.3
    t "You're doing great. Just keep pushing yourself."
    hide trainer

    scene black

    u "Happy birthday, Ethan! I hope you like your gift."
    e "Wow, a laptop! Thank you so much, Uncle."
    fa "Happy birthday, Ethan!"


    scene Study

    e "Alright, time to hit the books."

    # day 2- starts

    # scene alarm 
    # play music "ring.mp3"

    # menu:
    #     "Turn off the Alarm and wakeup":
    #         $ menu_flag=True
    #         stop music 
    #         scene Ready
    #         e "getting ready"

    #     "snooze the Alarm and sleep for some more time":
    #         $ menu_flag=False
    #         stop music 
    #         scene Sleep
    #         show mother 
    #         play sound "snore.mp3" 
    #         m" wake up [e]!"
    #         show mother at left
    #         play sound "ring.mp3"
    #         m"get ready son ! you are already late"
    #         stop sound
    #         scene Readyhurry
    #         e"getting ready"

    # scene Reached
    # e"finally reached college"
    # menu:
    #     " Participate actively in discussions.":
    #         $ menu_flag=True
    #         scene Active
    #         $ socialSkills += 1
    #         $ intelligence += 1
    #         pause
    #     "Stay quiet and listen to the lecture.":
    #         $ menu_flag=False
    #         scene Silent
    #         $ intelligence += 1
    #         pause
    # play sound"ring.mp3"
    # "bell rings"
    # scene Return
    # stop sound
    # e"returning to home"
    # menu:
    #     "spend time at home":
    #         scene Tv
    #         "watching Tv"
    #         $ health -= 1
    #     "go to gym":
    #         scene Gym 
    #         "lifting weights"
    #         $ intelligence += 1
    #         $ health += 1
    #         scene Street
    #         "returning to home"
    #         scene black
    #         e"finally reached home"
    # menu:
    #     "Concentrate on your textbooks and notes.":
    #         scene Study
    #         pause
    #         $ intelligence += 1
    #     "go to club and enjoy with friends":
    #         scene Club
    #         pause
    #         $ socialSkills += 1
    #         $ health -= 1
    # scene Sleep1
    # pause