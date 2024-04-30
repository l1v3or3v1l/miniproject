# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define m = Character("Mother")
image Ready=im.Scale("ready.png",1920,1080)
image Sleep=im.Scale("sleep.png",1920,1080)
image Readyhurry=im.Scale("readyhurry.png",1920,1080)
image Reached=im.Scale("reached.png",1920,1080)
image Silent=im.Scale("silent.png",1920,1080)
image Active=im.Scale("active.png",1920,1080)



# The game starts here.

label start:
    python:
        name=renpy.input("whats your name??")
        name=name.strip() or "Revi"
    define e=Character("[name]")
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    e"click to continue"
    $ renpy.movie_cutscene("./images/NEW.webm")
    scene alarm 
    play music "ring.mp3"
    menu:
        "Turn of the Alarm and wakeup":
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
            

        




    



        

    

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.


    # This ends the game.

    return
