
label start:   
    $ name=renpy.input("whats your name??")
    $ name=name.strip() or "Revi"
    define e=Character("[name]")
    scene bg classroom
    ## show the stats button from screen gameUI (custom_screens.rpy)
    show screen gameUI
    jump show_choices


label show_choices:
    $ boy1.name = name
    e"What do you want to know?"      
    e"I'm Yuki. Nice to meet you."
    menu:
        "Increase [boy1.name]'s social skill by 5":
            $ boy1.Socialskill += 5
            $ boy1.Intelligence+=2
            $ boy1.Pornaddiction+=6
            $ boy1.Health+=4
            "The affection increased by 5."
        "Decrease [boy1.name]'s affection by 3":
            $ boy1.Socialskill -= 3
            "The affection is decreased by 3."
        "End game":
            return
    
    jump show_choices