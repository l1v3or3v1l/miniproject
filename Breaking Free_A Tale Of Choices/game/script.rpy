﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
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



# The game starts here.

label start:
    scene yagami
    play music"death_note.mp3"
    $ name=renpy.input("whats your name??")
    $ name=name.strip() or "Revi"
    define e=Character("[name]")
    $ boy1.name = name
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    e"click to continue"
    stop music
    $ renpy.movie_cutscene("./images/NEW.webm")
    show screen gameUI
    scene alarm 
    play music "ring.mp3"
    menu:
        "Turn of the Alarm and wakeup":
            $ boy1.Intelligence+=5
            $ boy1.Socialskill+=2
            $ boy1.Health+=6
            jump choice_1
        "snooze the Alarm and sleep for some more time":
            jump choice_2
    label choice_1:
        $ menu_flag=True
        stop music 
        scene Ready
        e"getting ready"
        jump choice_done
    label choice_2:
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
        jump choice_done
    label choice_done:
        scene Reached
        e"finally reached college"
        menu:
            "Participate actively in discussions.":
                jump choice_1a
            "Stay quiet and listen to the lecture.":
                jump choice_2a
        label choice_1a:
            $ menu_flag=True
            scene Active 
            e"Participate aaaactively in discussions."
            jump choice_1_done
        label choice_2a:
            $ menu_flag=False
            scene Silent
            e"Stay quiet and listen to the lecture."
            jump choice_1_done
        label choice_1_done:
            play sound"ring.mp3"
            "bell rings"
            scene Return
            stop sound
            e"returning to home"
            menu:
                "spend time at home":
                    scene Tv 
                    "watching Tv"
                "go to gym":
                    scene Gym 
                    "lifting weights"
                    scene Street
                    "returning to home"
                    scene black
                    e"finally reached home"
        menu:
            "Concentrate on your textbooks and notes.":
                scene Study
                "studying"
            "go to club and enjoy with friends":
                scene Club 
                "chilling"
        scene Sleep1



             


        




    



        

    

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.


    # This ends the game.

    return
