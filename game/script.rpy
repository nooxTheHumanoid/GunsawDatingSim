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

#should set it so the pc didn't look around while in the hall
default lookaround0 = False

#should set it so the player didn't listen in on why the pronouns and name were asked
default listen0 = False

#should set it so the player didn't look at the epda with the profiles
default ePDAchecked0 = False

#the individual profiles
default softyprofilechecked = False
default citrusprofilechecked = False
default saw03profilechecked = False
default saw04profilechecked = False
default saw05profilechecked = False
default kelvinprofilechecked = False
default saw07profilechecked = False
default tygoprofilechecked = False
default faeprofilechecked = False
default saw10profilechecked = False
default scarlettprofilechecked = False
default duneprofilechecked = False
default saw013profilechecked = False
default bickerprofilechecked = False
default ericprofilechecked = False

#sets if the PC talked to the RC before picking a partner
default softytalk0 = False
default citrustalk0 = False
default saw03talk0 = False
default saw04talk0 = False
default saw05talk0 = False
default kelvintalk0 = False
default saw07talk0 = False
default tygotalk0 = False
default faetalk0 = False
default saw10talk0 = False
default scarletttalk0 = False
default dunetalk0 = False
default saw013talk0 = False
default bickertalk0 = False
default erictalk0 = False


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
    
    Somewhere that you've never been, blinking at the unusual sight before you.
    
    Above you is blue— a deep blue that you've only ever imagined before— that stretches out as far as you can see, past the mist hanging around you. Turning your head to the side, you can see a soft, green material that vaguely resembles fur. """
    
    """You're almost certain that this is what is called \"grass.\"
    
    A large, indistinct light hangs far, far above you. It\’s so bright that it hurts to look anywhere near it.
    
    The ground beneath you is slightly warm, and a cool breeze passes over you, just enough for you to start to fall asleep. At least, until you think you hear someone calling out to you from... somewhere? In the fog, maybe?
    
    You decide that you should get up to look for the source, and as soon as you place your paws against the ground to get up and look for them, but when you do—"""


    label wakeup:
    
    # there's apparently some specific commands that have to be created and use in order to use multiple transitions in a sequential order, particularly if doing so quickly* so this chunk is a placeholder until I can look at that.
    scene bg cargo 
    #play audio #loud horn
    #play audio #hissing 
    #with fog
    #with vpunch
    #scene bg cargo
    with hpunch
    
    """—you violently jolt awake. The blaring of the horn is loud enough to make your ears ache. You scramble to your feet as fast as possible, while also trying to cover your ears.

    Unfortunately, you're too sleep-struck to notice the thin layer of moisture that coats the floor— left behind by whatever mist had been pumped into the room.
    
    This combination, perhaps unsurprisingly, has the unfortunate result of you falling forward and gives your face an impromptu introduction to the cold, metallic, and {i}very{/i} hard floor."""

    "You" "A yelp— equal parts startled and pained— escapes you at the moment of impact. \'{i}At least the noise stopped.{/i}\' You think with groggy gratitude, wondering if going back to sleep was now an option."
    
    iv """Somewhere in the room, a speaker briefly squeals with feedback. A very annoyed voice blasts from the same location, \"Repeating wake protocol in 5, {nw=1}

    4,

    3,

    2—\""""

    "At first, your groggy mind doesn't quite understand the meaning, but as the countdown nears the end, it quickly catches up. Panic jolts you to full awareness."
    
    "You" "\" Wha— \'m wake! {i}I\'m {b}awake!{/i}{/b}\"" 
    
    "You" """You scramble to get off of your face, paws slipping again on the thin film on the floor. 
    
    Now that you are awake enough to register the distinctive smell, you realize what the mist was: a minor stimulant. Something they use when they don't feel like waiting for someone to wake up."""

    "You" "{i}'Wait...'{/i} you think, —{nw=5}"

    "You" "—whipping your head around as you realize that this is NOT where you fell asleep. Dread sets in. '{i}{b}Oh no.{/i}{/b}\'"

    iv "\"Subject [pcserial], approach the door of the transport pod and place your paws through the slot.\""

    "You hesitate for a moment, then approach the door. You consider crouching to see if there's anything visible past the slot before putting your hands through it, but the presence of the speaker stops that idea in its tracks." 

    "You" "Instead, you reluctantly lift your hands together, placing them through the slot."

    "You" "For a moment, there is nothing. Then you flinch at the sudden sensation of cold metal tightening around your wrists with a sharp click, binding them together."

    "You" "Pulling your hands back through the slot, you find the expected handcuffs around your wrists. Less expected is the way that they seem to be stuck together despite lacking a chain or hinge. You try to separate your wrists, but the straining  causes the metal to dig into your skin."

    iv "Step back against the opposite wall, paws in front of you."

    "You" "With no other options, you comply, backing up until your tail touches the wall, and at the lack of response, until it's squished against your back."

    "The door hisses open, revealing two humans in the black uniforms that you've learned to associate with the kind of humans called \"security guards.\" One is holding a wire/metallic lead, while the other carries some type of gun."

    "The one with the lead steps forward, while the second keeps their weapon firmly trained on you." 

    "The lead somehow attaches to the cuffs without any sort of clip or being tied on. You tilt your head in confusion but decide it makes as much sense as the two somehow being stuck together."

    sgt1 "\"Come with us,\" the guard orders,  walking toward the door and tugging on the lead."

    sgt2 "\"And don't try running. It'd be a shame if I had to get your blood all over the new floors.\" The human makes the gun click, and the fur on your neck rises. You hurry to follow your captor."

    """The clang of the humans’ boots echo against the metal floors, adding to the already disorienting nature of the path the three of you follow.

    The hallways feel increasingly labyrinthine as the path turns one way and then another. The route takes you through several nearly identical areas only differentiated by signs indicating their individual purposes. 

    Eventually you lose track of how many turns you've made and could swear that you passed through the same place at least three separate times. It's been several minutes now, and there's no sign that you'll reach the destination soon. 
    
    You can't do anything except  walk between the two guards as instructed, and they don't look like they'll appreciate you asking any questions... but the anticipation is starting to bother you."""


    scene bg hallwaygeneral

    menu onwaytointake:
        "Maybe looking around will soothe your nerves?"
        "Looking around should be fine.": 
            jump lookaroundprologue
        "Just keep walking, don't give them any excuses.":
            jump dontlookaroundprologue

        
    label lookaroundprologue:

    """With how shiny everything is, this facility certainly seems to be newer than the ones you've been in before.

    The lights are bright— though not uncomfortably so— and none of them seem to be flickering or producing that high pitch buzz that most of the humans seem oblivious to. 
    
    The vents here-and-there seem to be smaller, while still providing more than enough air flow for you to feel it when passing by their respective grilles.
    
    You take a deep breath of the air when passing under one— and immediately sneeze, thanks to the  nose-blinding levels of 'new' smell. 
    
    You stumble, being pulled along by the human despite having briefly been stopped by your sneeze, but manage to recover before you can fall.
    
    Still, despite how small the vents seem to be, they're extremely well secured. You count eight screws securing one to the wall, and twelve in another— it seems like a rather silly amount of effort. 
    
    The metal wall panels are likewise extremely well secured, with many being outright welded together. Only a few that you can see are instead secured in place with funny looking bolts, mostly near where the doors seem to be. Speaking of which..."""

    $ lookaround0 = True

    #If needed for any potential routes where escaping the lab is brought up, this choice could also set a variable that allows the PC to tell the RC that using the vents won't work.

    jump prologueintake

    label dontlookaroundprologue:

    """The humans already seem annoyed, and you don't want to give them an excuse to take that annoyance out on {i}you{/i}. Better to keep your eyes to yourself and keep moving.
    
    It takes several more minutes, but the walk finally ends."""

    $ lookaround0 = False

    jump prologueintake

    label prologueintake:

    scene infrontoflargedoor

    """In front of you is a large electronic door— a {b}VERY{/b} large electronic door. You think that if you could back up enough to compare them, it would be almost as tall as both of the humans if they stood on each other's shoulders."""

    "You" """You can't help but wonder {i}why{/i} the door needs to be so big in the first place.  

    Only to jump at the sound of a loud beep, followed by a drawn-out hiss, as the door parts open. You look over and realize that you were paying so much attention to the absurd size of the door that you missed the gun wielding human swipe a card through the  reader on one side of the door."""

    sgt2 "The human makes a harsh motion with their gun, tersely stating, \"What are you waiting for? get in there.\""
    
    "You" "You realize that the human holding the lead stands on the other side of the doorway, tugging your cuffs with an expression of rapidly fading patience and you hurry through the doorway."

    """The door hisses again, before shutting behind you with a dull {i}clunk{/i}. You begin  to look around the room, only to jump when the human carry the lead approaches you and— without warning— 
    
    — produces a small black device, pressing a series of buttons before swiping it over the cuffs, unbinding them. They then proceed to pull a cable from a compartment on the side of one of the cuffs, connecting the two with it. 
    
    The lead, however, remains attached to the cuffs, and the guard continues escorting you before you even have time to process the change in restraints.

    Your hands aren’t really free, but the ability to rest them at your side is an improvement over before."""

    scene think dmv

    """You lean to the side and see that you're taken to one of many lines of Experiments approaching a long, unfurnished metal counter each with a human sitting across from them, separated by tall transparent dividers. 
    
    The seated humans occasionally enter data into their E-PDAs as they question each Experiment, and guards positioned throughout the room watch with disinterest, occasionally speaking to each other or an Experiment."""

    sgt1 """The human drags you to a spot that empties as the Sawian at the front of the line steps away from the counter, walking into a hallway that’s just out of sight.The guard instructs you in a commanding tone:

    \"Wait in line until you get up to the counter. Answer whatever questions they ask you. Don't do anything you aren't told to do. Got it?\""""

    """You nod hurriedly, eager to convey your understanding of the instructions.

    The human then waves the same device over the cuffs, placing their other hand beneath the lead, which detaches from the cuffs seamlessly. The guard wraps the lead in a loop around their hand as they leave with the armed one back in the direction from which you came."""

    "It isn't long before you reach the front of the line, and you step up to the desk."

    "Intern" "The human at the desk points some sort of scanner at you, which beeps. \"Registering Subject [pcserial]. Subspecies: Experiment. Identifying features: None.\"" #"identifying features" can be removed or set to a variable that describes the character customization option chosen if we end adding character creation somehow, at somepoint

    "You" "{i}\'Rude.\'{/i}"

    "Intern" " They ask, \"What is your name? Or what do you want it to be?\""

    "You" "Huh?"

    "Intern" "They— he? You think he? He sighs, looking like he's tired of... everything. He speaks slowly, as if explaining to someone very young, \"Your name in the system is [pcname]. If you want it changed, this is the time to do it.\""

    "You" "A human is asking what {b}you{/b} want? That's... unusual."
    
    "You" "Unusual things with humans are scary. \"...Why does what I want matter?\""

    "Intern" "Now he looks like he wants to throw something at you, which oddly makes you feel better."

    label nameinput:

    python:
        pcname = renpy.input(default='Gen',length=32,prompt= "Tell me you want to be called while you\'re here so I can put it in already.")
        pcname = pcname.strip()

    label postname:

    "Intern" "\"That\'s certainly a choice,\" he mutters, not even giving you time to get offended before asking, \"Pronouns?\""
    
    pct "What?"
    
    "Intern" "\"He, she, it, they? What do you want people to refer to you as when they talk about you? I know we don't teach you Experiments everything, but I know your education covered {i}this{/i}.\""

    call pronounselection

    "Intern" "He inputs something, and then points at a sign just above the hallway that the others left through, \"Go to that sign, then wait. I assume you at least know your numbers?\" You don't get the chance to respond before he continues," 
    
    "Intern" "\"You'll wait there until you get a message displayed on your chip. Follow the directions. Then go into the room with that number.\""

    pc "'{i}It's weird that the humans are just {b}trusting{/b} me to listen.{/i}' You think, following the sign, only to turn the corner and realize that there are still plenty of armed humans in the area. \'{i}Or not.{/i}\' It\'s not like you'd directly disobey, anyway. It doesn\'t end well."


    label whypronoun:
    
    "While waiting, you realize that you can hear two humans talking."

    sgt "\"I don't get it.\" says a security guard, standing next to one of the humans sitting behind one of the desks."

    lc "The sitting human— wearing glasses and a white coat of some kind— sighs, muttering, \"You \"don't get\" a number of things.\""

    sgt "I'm serious, I really don't get it."

    menu eavesdrop0:
        "Your spikes perk slightly at the idea that you may find out what is going on here. Should you listen in?"
        "Listen in— you could find out something you wouldn't otherwise.":
            jump listen_0
        "Human business is not {i}your{/i} business. Pay attention to what you were told.":
            jump nolisten_0

    label listen_0:
    "You decide to listen in, trusting that whatever instructions your chip feeds you will be jarring enough that you won't miss it."

    lc "The human in the white coat sighs again, before seemingly resigning themself to the question, \"What? What is it that you don't understand this time?\""

    sgt "\"This part that you're doing now. I get the reason for this facility and for bringin\' them all here, but why does it matter for them to decide what they're called? The instructions have been to use \"them\" and \"it\" for ages.\""

    lc "\"Because it might matter for the study. You don't like it when people call you Sammy instead of Samson, right?\""

    sgt "\"Fuck no. Hate it, feels like they're treating me like I\'m five.\""

    lc "\"There you go.\""

    sgt "\"Huh?\""

    lc "\"For Pete\'s sake— what someone calls you can change how you feel about them. That obvious enough?\""

    sgt "\"Huh, guess it is.\""

    $ listen0 = True

    jump messagereceived

    label nolisten_0:

    "The less you know about what humans talk about the better. There\'s no reason to risk them getting mad that you happened to hear them. You'd rather just count the number of seams in the wall."

    $ listen0 = False

    jump messagereceived

    label messagereceived:

    pc "You jump when your chip abruptly \'displays\' a message— something that you still aren\'t used to— appearing in the corner of your vision. It reads out simple directional indicators as you walk down the hall."

    "\"Forward\""

    "\"Left\""

    "\"Right\""

    "\"Forward\""

    "\"Right\""

    "\"Forward\""

    "\"Right\""

    "\"Left\""

    "\"Forward\""

    pc "Now thoroughly disoriented, you find yourself in front of the door that matches the readout’s instructions. Which is closed. For a moment you aren't quite sure what to do, and then notice the scanner next to the door."
    
    "You're just about to knock on the door when it opens inwards, a human in the labcoat stepping out of it."

    lc "\"Ah good, you're the last Experiment we were waiting on. Come in here.\" She waits for you to enter the room, the door hissing closed behind you."

    
    scene genericlab

    pc """She then hands you... an EPDA? \"Here, look through the files on that.\" That was clearly directed to you, but then she presses a button on something and talks to someone clearly outside of the room,"
    
    \"Hey, do you have the SAW-11s and SAW-13s ready for transport? ...And they have all of the requested restraints on this time, right? We don't want a repeat incident. ...Alright, go ahead and start bringing them this way.\" 
    
    She ends the call and looks at you again, raising an eyebrow. \"You should really look through that while you wait.\" She walks over to and begins to interact with a large panel of buttons and dials with an indiscernible purpose."""


    menu epdaornah:
        "Look through the EPDA?"
        "If a human is being THAT insistent, I want to know why!":
            jump yesePDA
        "I don't care.":
            jump noePDA

    label yesePDA:
    pc "This... looks like profiles on other Sawians? At least, it says they're Sawians. Looking at some of them, you can't help but question the accuracy of that. Nor are you entirely sure why she's so insistent that you look at them, but... May as well now?"

    "There will be profiles here at some point."
    $ ePDAchecked0 = True
    #show screen ePDA
    #"Insert the ePDA display with the profiles"

    jump speeddatetime

    label noePDA:
    $ ePDAchecked0 = False

    pc "You opt to drop the ePDA onto the table without looking at the contents. You're fairly sure you hear the human sigh, but by the time you look at her she's doing something else, this time on a computer."

    "There will NOT be profiles here at some point."

    jump speeddatetime

    label speeddatetime:

    lc "\"Alright, come with me.\""
    if ePDAchecked0 == True:
        "She waves for you to come with her, plucking the tablet from your hand as you pass."
    else:
        "She shakes her head at your refusal to look at the contents of the ePDA as you pass."
    
    """You arrive at your destination shortly and while you aren\'t sure what you expected,  what you see certainly isn\'t it.
    
    The room is large, well lit, containing actual furniture— made out of foam, but still furniture— arranged into sets of a table with seats across from each other, or at least two seats adjacent and close enough for easy conversation. 
    
    Closest to several heavily armed humans, there\'s even some actual tables and chairs— made of metal and wood! One chair at each is unusually large, and the entire sets are bolted to the floor, but still! 
    
    There\'s even a few areas that look like shallow pits filled with piles of pillows."""

    #pc "Your shock at the presence of furniture is replaced by anxiety at the sight of the other Sawians in the room some more heavily restrained than the others."
    #Can't figure out how to attach a check/variable for these to the option to look at the profiles. 
    if ePDAchecked0 == True: 
        pc """Your shock at the presence of furniture is replaced by anxiety, but not surprise at the presence of the other Sawians depicted in the profiles on the tablet, some more heavily restrained than the others. 
        
        Given what you read, you aren't entirely surprised."""
    else:
        pc """Your shock at the presence of furniture is replaced by the far more urgent shock at the variety of the other beings in the room, some that you can just barely recognize as being other Sawians. 
        
        The fact that many of those whom you\'re not entirely convinced are Sawians are heavily restrained does not bring you any comfort."""

    "You hear the crackle of a speaker, followed by a voice."
    
    projsm """The voice is deep and monotone, conveying a degree of cold indifference that your ears had yet to have the displeasure of experiencing. 
    
    The voice says— in what can only be described as an emotionless drone— \"Your directive for this experiment is to approach another subject and \"socialize\" with them in pairs.\""""

    pc  "Your fur stands on end at the voice. Something about it is distinctly unnerving in a way that you don't fully understand, but you know one thing for certain."

    pc "{b}You never, ever, want to get the personal attention of this human.{/b}"

    projsm "\"A buzzer will sound periodically. When the buzzer sounds, change to another subject and continue to \"socialize\".\"" 
    
    projsm "\"Do not \"socialize\" in groups larger than pairs.\"" 
    
    projsm "Do not attempt to \"socialize\" with the same subject more than once—\" the voice pauses, and something close to anger finds its way to the tone, briefly, \"{i}—We will know.{/i}\"" 
    
    projsm "Just as quickly, the voice returns to its previous dull cadence." 
    
    projsm "\"Refusing to \"socialize\" is not advised.\"" 
    
    projsm "\"Do not antagonize others.\"" 
    
    projsm "\"Do not attempt to harm yourself. Do not attempt to harm others.\"" 
    
    projsm "\"Guards are present, armored, and armed with a scale of deterrents.\"" 
    
    projsm "\"Further instructions will be given at the end of the \"socialization\" phase.\""

    pc "You can hear the quotes around the word \"socialize\" every time the voice says it, and while you aren't entirely sure what that says about the person it belongs to, it certainly reinforces your desire to avoid them."

    projsm "\"First time allotment begins in 3, {nw=3}"
    
    projsm "2,{nw=3}"
    
    projsm "1.\"{nw=3}"

    "The buzzer sounds, some of the Sawians seem to have their mind already made up as they dash over to someone, while others take a moment to look around before approaching."
    
    "Others, like you, seem overwhelmed by the amount of options and remain frozen where they were when the buzzer sounded."

    #This menu will need to be tweaked to either display two columns of options, a scroll wheel, or to shift to another menu while retaining the ability to remove selected options.


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
$ softytalk0 = True
jump choosespeeddate

label speeddatedone:

"The buzzer goes off again."

projsm "\"[pcserial], enter the door on the far left.\""

pc "You follow the instructions, wondering what they plan on doing to you."

"In the room is a scientist, the one who gave you the ePDA earlier."

lc "Lucky you! You get the first pick. So, out of the other participants, who do you want to have as your partner?"

pct "What?\""

pc "You're starting to feel like a broken music player."

lc "\"Oh, right. You need to pick someone out of the group that you were just with that you want to spend a lot of time with in the future.\""

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
        lc "Are you sure? If she agrees, you aren't allowed to change partners after this, even if you decide your partner is a bad match later."
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
