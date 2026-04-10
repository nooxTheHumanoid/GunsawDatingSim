# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# please put variables outside of label start: for easier handling // dearev
#player character talking, can be used when it's a dialogue only line
define pct = Character("[pcname]", dynamic=True, what_prefix="\"", what_sufix="\"")
define pc = Character("[pcname]", dynamic=True)
#Security Guard talking
define sgt = Character("Security Guard")
define sgt1 = Character("Security Guard 1")
define sgt2 = Character("Security Guard 2") 
#scientist talking, lc for lab coat
define lc = Character("Scientist")
define iv = Character("Impatient Voice", color="#c20000")
#actually project submanager, because the actual manager won't come up for a long time, if ever.
define projsm = Character("Project Manager", color="#9ea1a8")

#it's me
define bwa = Character("BWA", what_color="#a44ad8", who_color="#a44ad8")

# other variables 
default pcserial = None

define pcname = "Gen"
#python:
#    pcname = renpy.input(default='Gen',length=32,(prompt="Intern"=character "\"Tell me you want to be called while you\'re here so I can put it in already.\"")
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
    
    Above you is blue. A deep blue that you've only every imagined stretching out as far as you can see past the mist hanging around you. Turning your head to the side, you can see a green, soft looking material that vaguely resembles fur. """
    
    """You're rather certain that it's what is called \"grass.\"
    
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
    
    "You" "\" Wha— \'m wake! {i}I\'m {b}awake!{/i}{/b}\"" 
    
    "You" """You scramble to get off of your face, paws slipping again on the thin film on the floor. 
    
    Now that you are awake enough to register the distinctive smell, you realize what the mist was. A minor stimulant that they used when they wanted something and didn't feel like waiting for someone to wake up. {nw=5}"""

    "You" "{i}'Wait...'{/i} you think, —{nw=3}"

    "You" "—whipping your head around as you realize that this is NOT where you fell asleep. Dread sets in. '{i}{b}Oh no.{/i}{/b}\'"

    iv "\"Subject [pcserial], approach the door of the transport pod and place your hands through the slot.\""

    "You hesitate for a moment, then approach the door. You consider crouching to see if there's anything visible on the other side, but the presence of the speaker stops that idea in its tracks."

    "You" "Instead, you reluctantly lift your hands together, placing them through the slot."

    "You" "For a moment, there's nothing, and then you flinch at the sudden feeling of cold metal around your wrists, clicking as the metal tighten around your wrists— and then your wrists snapping together where the metal sits."

    "You" "Pulling your hands back through the slot, you find the expected handcuffs around your wrists. Less expected is the way that they seem to be stuck together despite the lack of a chain. You try to seperate your wrists, but the straining just causes the metal to dig into your furr and skin."

    iv "Step back against the opposite wall, hands infront of you."

    "You" "With no other options, you comply, backing up until your tail touches the wall, and at the lack of response, until it's squished between it and your back."

    "The door hisses open, revealing two humans in the black uniforms that you've learned to associate with the kind of humans called \"security guards.\" One is holding a length of some sort of lead, while the other is carrying some type of gun."

    "The one with the lead steps towards you while the second keeps their weapon firmly aimed at you." 

    "You tilt your head in confusion as the lead somehow attaches to the cuffs without any sort of clip or being tied on, but decide it makes as much sense as the two somehow being stuck together."

    sgt1 "\"Come with us,\" the one with the lead states, walking toward the door, tugging on the rope."

    sgt2 "\"And don't try running. It'll be a shame if I have to get your blood all over the new floors.\" The human does something that makes the gun click, and the fur on your neck rises as you hurry to follow the first human."

    """The clang of the human's boots against the metal floors echos, adding to the already disorienting noise and path being taken. It's been several minutes now, and there's no sign that you'll reach the destination soon. 
    
    You can't do anything other than walk between the two guards as instructed, and they don't look like they'll appreciate you asking any questions... but the anticipation is starting to bother you."""

    scene bg hallwaygeneral

    menu onwaytointake:
        "Maybe looking around will soothe your nerves?"
        "Looking around should be fine.": 
            jump lookaroundprologue
        "Just keep walking, don't give them any excuses.":
            jump dontlookaroundprologue

        
    label lookaroundprologue:

    """This facility certainly seems to be newer than the ones you've been in before, with how shiny everything is. 
    
    The lights are bright— though not enough to cause discomfort— and none of them seem to be flickering or producing that high pitch buzz that most of the humans seem oblivious to. 
    
    The vents here-and-there seem to be smaller while still providing more than enough air flow for you to feel when passing under those in the ceiling, or when passing by the ones in the wall. 
    
    You take a deep breath of the air when passing under one— and immediately sneeze thanks to the nearly nose-blinding levels of 'new' smell. 
    
    You stumble, being pulled along by the human despite having briefly been stopped by your sneeze, but manage to recover before you can fall.
    
    Still, despite how small they seem to be, they're extremely well secured. You count eight screws securing on to the wall, and twelve in another— it seems like a rather silly amount of effort. 
    
    The metal wall panels are likewise extremely well secured, with many being outright welded together, with only a few that you can see instead being riveted in place, mostly near where the doors seem to be. Speaking of which..."""
    #If needed for any potential routes where escaping the lab is brought up, this choice could also set a variable that allows the PC to tell the RC that using the vents won't work.

    jump prologueintake

    label dontlookaroundprologue:

    """These humans already seem plenty annoyed, and you don't want to give them an excuse to take that annoyance out on {i}you{/i}. Better to keep your eyes to yourself and keep moving.
    
    It takes several more minutes, but the walk finally ends."""

    jump prologueintake

    label prologueintake:

    scene infrontoflargedoor

    """In front of you is a large electronic door— a {b}VERY{/b} large electronic door. One that's large enough that you think that, if you could back up enough to compare them, it would be almost as tall as both of the humans if they stood on eachother's shoulder."""

    "You" """You can't help but wonder \'Why are the doors so big!?\' 

    Only to jump as there a loud beep, followed by a hiss, as the door parts open. You look over and realize that you were paying so much attention to the door and its absurd size that you missed the gun wielding human scanning something into a reader on one side of the door."""

    sgt2 "The human makes a jerky motion with their gun, stating, \"What are you waiting for? get in there.\""
    
    "You" "You realize that the other human is standing on the otherside of the doorway, pulling on the lead connected to your cuffs with an expression of rapidly fading patience, and hurry through the doorway."

    """The door hisses again, then makes a dull {i}clunk{/i} behind you, having presumably shut behind you. You start to look around the room, only to jump when the human carry the lead approaches you and— without giving you time to think— 
    
    does something that makes the cuffs around your wrist stop sticking together and instead pulls some sort of connecter from the side of one and connects it to the other. 
    
    Though the lead stays attached to the cuffs, and the guard starts to pull you towards somewhere else before you even have time to process the change in restraints."""

    scene think dmv

    """You lean past them to see that you're being taken to— a line in front of a table? With a human on the other side of the table?

    Looking around, you realize that you're not the only one of your kind in the room either at one such table or being pulled to one."""

    sgt1 """The human drags you to a spot that becomes empty as the Sawian in front of you steps up to the table, and orders, 
    
    \"Stay here until that one leaves. Then you go up to where they were standing. You do that until you get up to the table. You answer whatever questions they give you. Don't do anything you aren't told to do. Got it?\""""

    """You nod hurriedly, eager to convey your understanding of the instructions.

    The human then does something to the cuffs, and the lead that they had been pulling you around by detaches from the handcuffs with no sign that it had ever been attached.

    You look around more closely now that you aren\'t actively being pulled somewhere, but find that the room— at least the part of it you can see— can effectively be summed up by what you saw when being pulled to your current spot. 
    
    Metal tables with humans with EPDAs in their hands sitting across from Experiments, seemingly asking questions and typing them into their EPDAs; a tall divider behind each table, and armed humans standing throughout the room watching and occasionally talking to eachother or an Experiment."""

    "It isn't long before it's your turn, and you step up to the desk."

    "Intern" "The human at the desk points some sort of scanner at you, which beeps. \"Registering Subject [pcserial]. Subspecies: Experiment. Identifying features: None.\"" #"identifying features" can be removed or set to a variable that describes the character customization option chosen if we end adding character creation somehow, at somepoint

    "You" "\'Rude,\' you think."

    "Intern" " They ask, \"What is your name? Or what do you want it to be?\""

    "You" "Huh?"

    "Intern" "They— he? You think he? He sighs, looking like he's tired of... everything. He speaks slowly, as if explaining to someone very young, \"Your name in the system is [pcname]. If that's not right or you want it changed, this is the time to do it.\""

    "You" "A human is asking what {b}you{/b} want? That's... unusual. {nw=2}"
    
    "You" "Unusual things with humans are scary. Slowly you ask. \"...Why does what I want matter?\""

    "Intern" "Now he looks like he wants to throw something at you, which oddly makes you feel better."

    label nameinput:

    python:
        pcname = renpy.input(default='Gen',length=32,prompt= "Tell me you want to be called while you\'re here so I can put it in already.")
        pcname = pcname.strip()

    label postname:

    "Intern" "\"That\'s certainly a choice,\" he mutters, not even giving you time to get internally offended before asking, \"Pronouns?\""
    
    pct "What?"
    
    "Intern" "\"He, she, it, they? What do you want people to call you when they talk about you? I know that we don't teach you Experiments everything, but I know your education covered {i}this{/i}.\""
#The below is from the pronoun tool and apparently needs to be added specifically here?
    call pronounselection

    "Intern" "He inputs something, and then points at a sign, \"Go to that sign, then wait. I assume you at least know your numbers?\" You don't even get the chance to nod or shake your head before he continues," 
    
    "Intern" "\"You'll wait there until you get a message display on your chip. Follow the directions. Then go to the room with that number.\""

    pc "'{i}It's weird that the humans are just {b}trusting{/b} me to listen.{/i}' You think, following the sign, only to turn the corner and realize that there are still plenty of armed humans in the area. \'{i}Or not.{/i}\' Well, not like you'd be very likely to directly disobey, anyway. It doesn't end well."

    label whypronoun:
    
    "While waiting, you realize that you can hear two humans talking."

    sgt "\"I don't get it.\" says a security guard, standing next to one of the humans sitting behind one of the desks."

    lc "The sitting human— wearing glasses and a white coat of some kind— sighs, muttering, \"You \"don't get\" a number of things.\""

    sgt "I'm serious, I really don't get it."

    menu eavesdrop0:
        "Your spikes perk slightly at the idea that you may find out what is going on here. Should you listen in?"
        "Listen in— you could find out something you wouldn't otherwise.":
            jump listen1
        "Human business is not {i}your{/i} business. Pay attention to what you were told.":
            jump nolisten1

    label listen1:
    "You decide to listen in, trusting that whatever instructions your chip feeds you will be jarring enough that you won't miss it."

    lc "The human in the white coat sighs again, before seemingly resigning themself to the question, \"What? What is it that you don't understand this time?\""

    sgt "\"This part that you're doing now. I get the reason for this facility and for bringin\' them all here, but why does it matter for them to decide what they're called? The instructions have been to use \"them\" and \"it\" for ages.\""

    lc "\"Because it might matter for the study. You don't like it when people call you Sammy instead of Samson, right?\""

    sgt "\"Fuck no. Hate it, feels like they're treating me like I\'m five.\""

    lc "\"There you go.\""

    sgt "\"Huh?\""

    lc "\"For pete sake— what someone calls you can change how you feel about them. That obvious enough?\""

    sgt "\"Huh, guess it is.\""

    jump messagereceived

    label nolisten1:

    "The less you know about what humans talk about the better. There\'s no reason to risk them getting mad that you happened to hear them. You'd rather just count the number of seams in the wall."

    jump messagereceived

    label messagereceived:

    pc "You jump when your chip abruptly \'displays\' a message— something that you still aren\'t used to— appearing at the bottom of your vision."

    "\"Forward\""

    "\"Left\""

    "\"Right\""

    "\"Forward\""

    "\"Forward\""

    "\"Right\""

    "\"Right\""

    "\"Left\""

    "\"Forward\""

    pc "Now thoroughly disoriented, you find yourself in front of the door that matches. Which is closed. For a moment you aren't quite sure what to do, and then realize that there's a scanner next to the door."
    
    "You're just about to knock on the door when it opens from the inside, a human in the labcoat stepping out of it."

    lc "\"Ah good, you're the last Experiment we were waiting on. Come in here.\" She waits for you to enter the room, the door hissing closed behind you."
    
    scene genericlab

    lc """She then hands you... an EPDA? \"Here, look through the files on that.\" That was clearly directed to you, but then she presses a button on something and talks to someone clearly outside of the room,"
    
    \"Hey, you have the SAW-11 and SAW-13 ready for transport? ...And they have all of the requested restraints on this time, right? We don't need a repeat. ...Alright, go ahead and start bringing them this way.\" 
    
    She ends the call and looks at you again, raising an eyebrow. \"You should really look through that while you wait.\" She walks off to do something, messing with some sort of series of dials and keypads."""

    menu epdaornah:
        "Look through the EPDA?"
        "If a human is being THAT insistent, I want to know why!":
            jump yesePDA
        "I don't care.":
            jump noePDA

    label yesePDA:
    pc "This... looks like profiles on other Sawians? At least, it says they're Sawians. Looking at some of them, you can't help but question the accuracy of that. Nor are you entirely sure why she's so insistent that you look at them, but... May as well now?"

    "There will be profiles here at some point."
    #$ set profilesyes = True
    #show screen ePDA
    #"Insert the ePDA display with the profiles"

    jump speeddatetime

    label noePDA:
    #$ set profilesno = True

    pc "You opt to drop the ePDA onto the table without looking at the contents. You're fairly sure you hear the human sigh, but by the time you look at her she's  doing something else, this time on a computer."

    "There will NOT be profiles here at some point."

    jump speeddatetime

    label speeddatetime:

    lc "\"Alright, come with me.\""
    #$ if profilesyes == True then "She waves for you to come with her, plucking the tablet from your hand as you pass.":
    #$ if else then "She shakes her head at your refusal to look at the contents of the ePDA as you pass."
    
    """You go through the door first and...
    
    You aren\'t sure what you expected, as the door hisses shut behind you, but what you see certainly isn\'t it.
    
    The room is large, well lit, with what looks like actual furniture— made out of foam, but still furniture— arranges into sets of two seats and a table, or at least two seats side by side. 
    
    Closest to several heavily armed humans, there\'s even some actual tables and chairs— made of metal and wood! One chair unusually large, and the entire set bolted to the floor, but still! 
    
    There\'s even a few areas that look like piles of pillows."""

    pc "Your shock at the presence of furniture is replaced by anxiety at the sight of the other Sawians in the room—— and some of them are certainly more heavily restrained than any of the others."
    #Can't figure out how to attach a check/variable for these to the option to look at the profiles. 
    #$if profilesyes 
    #"replaced by anxiety, but not surprise at the presence of the other Sawians depicted in the profiles on the tablet, and some of them are certainly more heavily restrained than any of the others. Given what you read, you aren't entirely surprised."
    #$if profilesno "replaced by the far more urgent shock at the variety of the other beings in the room, some that you can just barely recognized as being other Sawians. The fact that many of those you\'re not #entirely convinced are Sawians are heavily restrained does not bring you any comfort."

    "You hear a crackle, followed by a voice."
    
    projsm """The voice is deep, and somehow lacking any sort of mood or indicator about what the person it belongs to is like, and if going by what little tone is present, you would think they were reading off of a list of supplies for a dorm. 
    
    That meaning the voice says— in what can only be described as an emotionless drone— \"Your directive for this experiment is to approach another subject and \"socialize\" with them in pairs.\""""

    pc  "Your fur stands on end at the voice. Something about it is distinctly unnerving in a way that you don't fully understand, but you know one thing for certain.{nw=2} "
    
    pc "{b}You never, ever, want to personally get the attention of this human.{/b}"

    projsm "\"A buzzer will sound periodically. When the buzzer sounds, change to another subject and continue to \"socialize\".\"" 
    
    projsm "\"Do not \"socialize\" in groups larger than pairs.\"" 
    
    projsm "Do not attempt to \"socialize\" with the same subject more than once—\" the voice pauses, and something close to anger finds its way to the tone, briefly, \"{i}—We will know.{/i}\"" 
    
    projsm "Just as quickly, the voice goes back to sounding utterly bored by the matter." 
    
    projsm "\"Failing to \"socialize\" is not advised.\"" 
    
    projsm "\"Do not start conflicts.\"" 
    
    projsm "\"Do not attempt to harm yourself. Do not attempt to harm others.\"" 
    
    projsm "\"Guards are present, armored, and armed with a scale of deterrents.\"" 
    
    projsm "\"Further instructions will be given at the end of the \"socialization\" phase.\""

    pc "You can hear the quotes around the word \"socialize\" everytime the voice says it, and while you aren't entirely sure what that says about the person the voice belongs to, it certainly reinforces your desire to avoid them."

    projsm "\"First time allotment begins in 3, {nw=1}"
    
    projsm "2,{nw=1}"
    
    projsm "1.{nw=1}\""

    "The buzzer sounds, and some of the Sawians seem to have someone specific in mind as they practically run towards someone. Some take a moment to look around before approaching someone."
    
    "Others, like you, seem overwhelmed by the amount of options and remain frozen to where they were when the buzzer sounded."

    #This menu will need tweaked to either display two columns of options, a scroll wheel, or to shift to another menu while retaining the ability to remove selected options. 

    menu choosespeeddate:
        "Among the available participants, who should you approach?"
        "There's another Experiment like me here. Something feels oddly familiar about them.":
            jump Softyintro
        "(N/A)":
            jump placeholderchoice
        "(N/A) ":
            jump placeholderchoice
        "Done":
            jump speeddatedone
        
label placeholderchoice:

"Why are you here?"
jump choosespeeddate

label Softyintro:

"This is empty right now, please comeback later."
jump choosespeeddate

label speeddatedone:

"The buzzer goes off again."

projsm "\"[pcserial], enter the door on the far left.\""

pc "You follow the instructions, wondering what they plan on doing to you."

"In the room is a scientist, the one who gave you the ePDA earlier."

lc "Lucky you! You get first pick. So, out of the other participants, who do you want to have as your partner?"

pct "What?"

pc "You're starting to feel like a broken music player."

lc "\"Oh, right. You need to pick someone out of the group that you were just with, that you want to spend a lot of time with in the future.\""

lc "\"You'll do exercises with them, eat together, and sleep in the same room... in most cases, at least. You'll find out why after everyone is paired off.\""

#The same thing as is the case for the speeddating portion will need to be done for this menu.

menu routechoice:
    lc "So, who do you want to be paired up with?"
    "Softy.":
        jump softypartnercheck
    "N/A":
        jump placeholder
    "N/A":
        jump placeholder
    "N/A":
        jump placeholder
    "N/A":
        jump placeholder

label softypartnercheck:
    menu softypartner:
        lc "Are you sure? You can't change partners after this, even if you decide your partner is a bad match."
        "I'm sure.":
            jump softyroutestart
        "Let me think it over again.":
            jump routechoice
        

    label placeholder:
    lc "That Sawian currently doesn't exist."
    jump routechoice

    label softyroutestart:
bwa """This is where it ends for now. Hopefully, this gives enough context on the room and scenario that everyone feels comfortable starting their route(s).  

It\'s important to make sure that no one uses any labels that overlap, since renpy treats all rpy files as being a single one, afaik. 

This has the benefit of every route being able to be set in it's own rpy file, though. The same thing applies to variables, afaik, at least if the variable is present in this section."""



    

    # This ends the game.

return
