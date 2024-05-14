## Screen with character screen button
screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/stats_%s.png"
        action ShowMenu("character_screen")
        
## Stats UI
screen character_screen():
    tag character_screen_tag
    add "UI/bg black.jpg"
    hbox:
        ## LEFT FRAME
        frame:
            #Remove hashtag in the next lineto remove the black and blue background
            background None
            style_prefix "character"
            ysize 1080
            xsize 640
            vbox:
                xalign 0.5
                yalign 0.5
               
            
            imagebutton:
                yalign 0.5
                yoffset 90
                xoffset 20
                auto "UI/return_%s.png"
                action Return()
        ## RIGHT FRAME
        frame:
            background None
            ysize 1080
            xsize 1280
            vbox:
                xalign 0.5
                xsize 600
                xoffset -300
                yoffset 100
                spacing 20
                ## Notice that we're using selectedCharacter to show the variables here.
                text "{b}Name: [selectedCharacter.name]{/b}"
                text  "{b}Age:18{/b}"

                hbox:
                    spacing 20

                    vbox:
                        spacing 10
                        text "{b}Intelligence{/b}"
                        bar value StaticValue(selectedCharacter.Intelligence, 10) xsize 300:
                            left_bar"images/bars/left1.png"
                            right_bar"images/bars/right1.png"
                        text "{b}social skills{/b}"
                        bar value StaticValue(selectedCharacter.Socialskill, 10) xsize 300:
                            left_bar"images/bars/left2.png"
                            right_bar"images/bars/right2.png" 
                        text "{b}Health{/b}"
                        bar value StaticValue(selectedCharacter.Health, 10) xsize 300:
                            left_bar"images/bars/left3.png"
                            right_bar"images/bars/right3.png"
                        text "{b}Porn Addiction{/b}"
                        bar value StaticValue(selectedCharacter.Pornaddiction, 10) xsize 300:
                            left_bar"images/bars/left4.png"
                            right_bar"images/bars/right4.png"
            add selectedCharacter.imageName xalign 1.0 yalign 0.5
            text"Hey,I'm {b}[selectedCharacter.name]{/b}" xalign 0.8 yalign 0.1

style character_button_text:
    xalign 0.5