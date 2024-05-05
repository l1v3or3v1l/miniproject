# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
image Morning=im.Scale("morning.png",1920,1080)


# The game starts here.

label start:
    scene Morning
    #centered"{cps=2.5}{b}{size=60}DAY-1{/size}{/b}{/cps}"
    centered"{cps=2.5}{b}hello{/b}{/cps}"
    
    # Display the text centered on the screen
return

