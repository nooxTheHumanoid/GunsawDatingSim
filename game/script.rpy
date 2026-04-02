# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#player character talking
define pct = Character("[pcname]", dynamic=True, what_prefix="\"", what_sufix="\"", default="Gen")

#sets [pcname] to Gen
#python:
#    pcname = renpy.input("Tell me you want to be called while you're here so I can put it in already.", length=32)
#    pcname = pcname.strip()
#    
#    if not pcname:
#        pcname = "Gen"

    



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg placeholder

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    

    # This ends the game.

    return
