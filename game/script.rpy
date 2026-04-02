# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# please put variables outside of label start: for easier handling // dearev
#player character talking
define pct = Character("[pcname]", dynamic=True, what_prefix="\"", what_sufix="\"", default="Gen")
#Security Guard talking
define sgt = Character("Security Guard")
#scientist talking, lc for lab coat
define lc = Character("Scientist")
define iv = Character("Impatient Voice", color="#c20000")

#it's me
define bwa = Character("BWA", what_color="#a44ad8", who_color="#a44ad8")

# other variables 
default pcserial = None

#sets [pcname] to Gen
#python:
#    pcname = renpy.input("Tell me you want to be called while you're here so I can put it in already.", length=32)
#    pcname = pcname.strip()
#    
#    if not pcname:
#        pcname = "Gen"

# Function to assign a randomized number between 6000 and 80000 to the pc that is assigned to them as a variable/alias, on a per playthrough basis, "pcserial". Need to figure out how to get it to save to somewhere the game can always load it?
# above has been done, see below


# The game starts here.

label start:

    # 420690
    if pcserial is None:
        $ pcserial = renpy.random.randint(6000, 80000)
        # above should assign a serial // dearev


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    #blank black screen
    scene placeholder bg black
    with Dissolve(.5)
    
    pause .5
    
    #bg freedream should be a sort of foggy, vaguely outdoors area— think something like a blue sky, green floor, hazy fog everywhere with a very bright spot in the sky
    #something that someone who has never gone outside would THINK "the outside" looks like. "freedream" below being a placeholder name for said bg

    scene bg freedream
    with Dissolve(.5, reverse=True)
    
    #narration, in the second person POV, present tense (intended, at least)
    
    """
    You open your eyes, finding yourself lying on your back—
    somewhere. 
    
    Somewhere that you've never been, blinking at the sight before you.
    
    Above you is blue. A deep blue that you've only every imagined stretching out as far as you can see past the mist hanging around you. Turning your head to the side, you can see a green, soft looking material that vaguely resembles fur. 
    
    You're rather certain that it's what is called \"grass.\"
    
    A large, indistinct light sits far, far above you, yet so bright it hurts to look anywhere near it.
    
    The ground beneath you is just slightly warm and a cool breeze passes over you just enough for you to start to fall asleep. At least, until you think you hear someone calling out to you from... somewhere. In the fog, maybe?
    
    You decide that you should get up to look for the source, and as soon as you place your paws against the ground to get up and look for them—"""

    label wakeup:
    
    # there's apparently some specific commands that have to be created and use in order to use multiple transitions in a sequential order, particularly if doing so quickly* so this chunk is a placeholder until I can look at that.
    scene bg cargo 
    #play audio #loud horn
    #play audio #hissing 
    #with fog
    #with vpunch
    #scene bg cargo
    with hpunch
    
    """—do you violently jolt awake. The blarring of the horn is loud enough to make your ears ache as you are trying to scramble to your feet as fast as possible, while also trying to cover your ears.

    Unfortunately, you're too sleep struck to notice the thin layer of moisture that coats the floor— left behind by whatever mist had been pumped into the room.
    
    This combination perhaps unsurprisingly has the unfortunate result of you falling forward and giving your face an impromptu introduction to the cold, metallic, and {i}very{/i} hard floor."""

    "You" "A yelp— equal parts startled and pained— escapes you at the moment of impact. \'{i}At least the noise stopped.{/i}\' You think with sleepy gratitude, wondering if going back to sleep was now an option."
    
    iv """Somewhere in the room, a speaker squeals with feedback briefly. A very annoyed sounding voice blasts from the same location, \"Repeating wake protocol in 5, {nw=1}

    4,{nw=.75}

    3,{nw=.50}

    2—\"{nw=.65}"""

    "At first, your groggy mind doesn't quite understand the meaning, but as the countdown nears the end it quickly catches up, and the panic jolts you to full awareness." 

    label needtolook:
    
    "You" "\" Wha— \'m wake! {i}I\'m {b}awake!{/i}{/b}\"" 
    
    "You" """You scramble to get off of your face, paws slipping again on the thin film on the floor. 
    
    Now that you are awake enough to register the distinctive smell, you realize what the mist was. A minor stimulant that they used when they wanted something and didn't feel like waiting for someone to wake up. {nw=5}"""

    "You" "{i}'Wait...'{/i} you think, —{nw=3}"

    "You" "—whipping your head around as you realize that this is NOT where you fell asleep. Dread sets in. '{i}{b}Oh no.{/ib}\'"

    iv "\"Subject [pcserial], approach the door of the transport pod and place your hands through the slot.\""

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    
    bwa "This is what I managed to get done so far. Took longer than I would have liked to get to this point, but I guess this works as a rough proof of concept?
    
    Plan on working on it again tomorrow, hopefully should either be done, or nearly done within the next 24 hrs, knock on wood."
    

    # This ends the game.

    return
