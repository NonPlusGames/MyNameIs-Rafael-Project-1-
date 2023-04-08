# ___________                                   .__      ___.                  
# \__    ___/___ _____    _____   ____________  |__| ____\_ |__   ______  _  __
#   |    |_/ __ \\__  \  /     \  \_  __ \__  \ |  |/    \| __ \ /  _ \ \/ \/ /
#   |    |\  ___/ / __ \|  Y Y  \  |  | \// __ \|  |   |  \ \_\ (  <_> )     / 
#   |____| \___  >____  /__|_|  /  |__|  (____  /__|___|  /___  /\____/ \/\_/  
#              \/     \/      \/              \/        \/    \/               
# coded by: Rafael Ivan Mota


from termcolor import colored

#player object to keep track of stats
class Player:
  def __init__(self):
    self.bravery=0
    self.charisma=0
    self.smarts=0
    self.stage=0

#Takes a string as an argument and outputs the same string italicized
def italics(text):
  return colored(f"\033[3m{text}\033[0m", "light_blue")

#Takes a string as an argument and outputs the same string bold
def bold(text):
  return colored(f"{text}", "light_cyan", attrs=["bold"])

#start up the instructions and then the first node of the game
def intro(stats):
  intro_text="""
Thankyou for playing [My Name Is ...]!

You will be playing a game with various choices and multiple outcomes.

Sometimes you will see a set of choices numbered like so:

1: Choice One
2: Choice Two
3: Choice Three

When you encounter this symbol [::] type in your response and press [ENTER] to make your choice.

When you encounter this symbol [->:] simply press [ENTER] to continue the story.

Please maximize the size of the console window as much as possible to prevent graphical glitches later on.

Without furthur ado"""
  input(intro_text+"->:")
  start(stats)

#updates stats based on choice selection and runs dialogue nodes based on stat values
def statCheck(choice):

  if stats.stage<=2:  
    #checks to see that the player inputs SOMETHING and that it is an integer
    try:
      choice=int(choice)
    except ValueError:
      newChoice=input(colored("Please type 1, 2, or 3 ::", "red", attrs=["bold"]))
      return statCheck(newChoice)
    if choice==1:
      stats.bravery+=1
    elif choice==2:
      stats.charisma+=1
    elif choice==3:
      stats.smarts+=1
    else:  #checks to see if the player inputs a correct number
      newChoice=input(colored("Please type 1, 2, or 3 ::", "red", attrs=["bold"]))
      return statCheck(newChoice)
  
  #print(stats.bravery, stats.charisma, stats.smarts, stats.stage)
  
  if stats.stage==0:
    stats.stage+=1
    if(choice==1):
      braveryOne()
    if(choice==2):
      charismaOne()
    if(choice==3):
      smartsOne()
      
  elif stats.stage==1:
    stats.stage+=1
    if(choice==1):
      braveryTwo()
    if(choice==2):
      charismaTwo()
    if(choice==3):
      smartsTwo()
    
  elif stats.stage==2:
    stats.stage+=1
    if(stats.bravery>=2):
      braveryPath(stats)
    if(stats.charisma>=2):
      charismaPath(stats)
    if(stats.smarts>=2):
      smartsPath(stats)

  #Because the final stage only has 2 choices, this stat check just makes sure only [1] or [2] is typed
  #The logic for the final node is handled in it's path using the returned [choice] value
  elif stats.stage==3:
    return checkOneTwo(choice)

#makes sure the passed value is a 1 or 2
def checkOneTwo(number):
  try:
    number=int(number)
  except ValueError:
    newNum=input(colored("Please type 1 or 2 ::", "red", attrs=["bold"]))
    return checkOneTwo(newNum)
  if(number>2):
    newNum=input(colored("Please type 1 or 2 ::", "red", attrs=["bold"]))
    return checkOneTwo(newNum)
  return number
  
#BRAVERY STAT NODES ----------------------------------------------------------------
def braveryOne():
  input(italics("""
Thinking back on what the Doctor had said, mixed with some innate intuition, you realize you have got to escape.

You call the nurse over.

You clock the nurse in the face with your best headbutt.  Luckily the body lands near your restraints and your hand fumbles to take the keys that are dangling from the nurses pocket.

You free yourself and throw on the nurses clothes and dash out of the infirmory. ->:"""))

def braveryTwo():
  input(italics("""
You wait for the person to run in the elevator.  
For a second they hesitated and that is all it took for you to run in and incapacitate them.  It was almost too easy.

You find a key card on them and swipe the monitor.  Suddenly the elevator starts moving and stops on the floor that was blocked off.  You quickly dash out the elevator. ->:"""))

def braveryPath(stats):
  input(italics("You take advantage of the fact that they have lowered their guard and lunge at the criminal closest to you.")+" ->:")
  print(italics("You quickly disarm him and use his body as a shield as you spray and pray his weapon across the group.  Most of them go down.  You run up to attack on of the men left standing."))
  input(bold("*BLAM*")+" ->:")
  input(italics("You are left reeling as you try to recover from a blow to the back.  As things start coming into focus, a fist lands square on your face.")+ " ->:")
  input(bold("(Blink)")+"->:")
  print("criminal 1: 'What do we do now?'")
  print(italics("You are on the floor among a pile of bodies."))
  print("""criminal 2: 'IT's THE DAMN BOSS WE'RE TALKIN' ABOUT HERE!
criminal 3: 'But they just tried to KILL US ... and fer the most part succeded.'
criminal 4: 'tsk...'
  """)
  input(bold("(Blink)")+"->:")
  input(italics("""
You fell that you are lying ontop the body of a guard and notice that he has a belt with some interesting items on it.

You slowly move your arm under him and try to feel around for anything.

You smile as you feel a slightly bumpy ball with a ring near the top.

You pull the pin. ->:"""))
  input(bold("JUMP UP!")+"->:")
  input(bold("RUN")+"->:")
  print(bold("*BOOOOOOOM*"))
  input(italics("""
  ...
  ...
The elevator shakes as it drops.

You let out an exhausted breath of air as it beeps and notifies you that you have reached the hangar. ->:"""))
  input(italics("""
There is a open space infront of you with many craft.

'This is it.' you think to yourself...'your chance to escape.'

You run into one of the ships and figure out how to start it up.  It is surprisingly easy for you to do so.

You hit the ignition and blast out of there.

However, as your ship leaves you notice some beeping on your short range sensors alerting you that someone must have taken the second ship. ->:"""))
  print(italics("The speakers click on,")+" Boss, stop running.  Your mission is complete now. Return to us.  We know it must be difficult to accept but you were working for us...it's all ok now.")
  print(bold("1: And now I am just a liability.  I am sorry gentlemen, but I'll be leaving now.  I'll send in my official resignation by mail."))
  print(bold("2: No way I'm gonna be manipulated by the likes of you!"))
  choice=input(bold("::"))
  choice=statCheck(choice) #FOURTH STAGE STAT CHECK
  if choice==1:
    name=input(italics("""
I punch the 2 way monitor. 

And turn the shuttle around.

With expert aim I take out their front weapons and engines.

With one last shot the whole area of space was reduced to particles.

I turn the ship around suddenly remembering.

How could I forget my name :: """))
    print(italics(bold(f"The galaxy must have missed it's ACE PILOT {name} all these years.")))
  if choice==2:
    name=input(italics("""
    I flew the shuttle around the mother ship and in the moment that I was situated opposite the other craft I turned on the invisibility cloak.  

As soon as the other craft finally made it to the other side I programmed a probe to shoot back the other side of the ship and have it ping the Guards.  They would never be the wiser. 

As they flew off on a wild goose chase.  I turned and flew the other direction laughing the whole way.

I had forgotten.  It is amazing that they were able to outsmart me, but never again.

I'll burn my name into the Galaxy's memory... :: """))
    print(italics(bold(f"{name} The Genius Strategist.")))
    
  
#CHARISMA STAT NODES ----------------------------------------------------------------
def charismaOne():
  print(italics("""
Thinking back on what the Doctor had said, mixed with some innate intuition, you realize you have got to escape. 
You call the nurse over.

While a bit nervous the nurse seems eager to talk to you.
  """))
  print("I have been taking care of you these 5 years you know."+italics(" she begins and you share in an embarising conversation on the details of your internment."))
  input(italics("""
After, you tell the nurse that it's their turn to talk about themselves for your amusment.  The nurse flushes but humors you and starts talking about life here on the Yamamoto.  

She is a great source of information and gives you the major details you wanted to hear about the star cruiser and it's current mission transporting a group of prisoners to a nearby penal colony.

You thank the nurse for spending the time to talk to you and mention that you feel your retraints are little too tight and beggining to feel uncomfortable. 

The nurse obliges and is maybe a little too generous in the loosining and gives you a little wink.  You ask them if it wouldn't be too much trouble to get you some snacks, it would help you start to feel up to talking with the Doctor.

As soon as the nurse leaves, you slip right out of your restraints and sneak out the infirmory. ->:"""))

def charismaTwo():
  input(italics("""
You climb up the sides of the elevator and use both arms and legs to stay in place.  The person running down the hallway runs in and swipes a card onto the monitor and the elvator starts moving.

It stops on the floor that was blocked off and the person runs out of the elevator.  

You try your best to quietly drop down, stretch your muscles a little, and sneak out the elevator. ->:"""))

def charismaPath(stats):
  print(italics("You decide to go along with this charade and convince them you are this 'Boss' they are talking about."))

  print("Boss, we got everyone on this floor already... what's the plan?")

  input(italics("You tell them that they did a good job and that it is time to head out of here.")+" ->:")
  print("Sure Boss, we just gotta head to the hangar.  There's supposed to be a shuttle we can jack down there.")
  input(italics("""
With that you take elevator again with the group of hooligans as they hoot and holler now that they think they have been reunited with their Boss.

The elevator beeps as it notifies you that you have reached the hangar. ->:"""))
  print(italics("""
The doors open to an incredible scene. There are huge craft in the far back.  They look like just the ticket out of here.  

Unfortunately, just in front of those lovely archangels, a horde of guards stood with iron sights aimed straight at us.
  """))
  print("guards: 'SURRENDER!' " + italics("they yell."))
  print("criminals: 'What should we do, Boss?'")
  print(bold("1: Let's get 'em men!  To be honest, I don't know what the hell is going on.  But they really piss me off for some reason.  So let's show 'em Hell!"))
  print(bold("2: Fight THEM! Believe in yourselves. There is nothing in this universe that can stop your ferocious nerve, your nerves of steel.  Fight and protect your Boss!"))
  choice=input(bold("::"))
  choice=statCheck(choice) #FOURTH STAGE STAT CHECK
  if choice==1:
    input(italics("""
The ensuing battle was grueling.  

I lost many a man.

But we fought hard.

Me and my crew....my crew? ->:"""))
    name=input("""
We flew off in the shuttle, at least what was left of us.

I had forgotten.  

I mad a promise to myself that I would never allow that to happen again.

The Galaxy had been missing him for 5 years.

Missing me :: """)
    print(italics(bold(f"Space Pirate {name}.")))
  if choice==2:
    input(italics("""
The ensuing battle was grueling.  

Both sides certainly fought hard.

It was hard to tell who was winning as I expertly weaved myself through the battle field and snuck onto the ship.


They were all fools. ->:"""))
    name=input("""
I flew off in the shuttle.

Everything went according to plan.

I had forgotton, but it seems I was able to kill two birds with one stone.
The Criminal Group that I had convinced I was their one and only Boss over 5 years ago.  
And the Secret Organization that I originally worked for and set me up.

Hopefully no one knows how I did it and who was here.
I've gone by many aliases; Midnight, Ghost, 29619.  But they will never know my true name... :: """)
    print(italics(bold(f"Ace Agent {name}.")))

#SMARTS STAT NODES ----------------------------------------------------------------
def smartsOne():
  input(italics("""
Thinking back on what the Doctor had said, mixed with some innate intuition, you realize you have got to escape.

Without thinking you begin to meditate quitely in the bed.  Eventually the machines monitoring your health start to beep wildly.  The nurse notices this and runs out the room presumably to get the Doctor.

You let out a breath and feel your blood rushing again. The monitors return to normal.

You dislocate your arm and slip right out of the restraints.  In one of the drawers you find some tranquilizer (presumably incase you broke your restraints) and you wait behind the curtain.  Not long after, the Doctor rushes in, you inject the liquid without warning and the Doctor topples over.  

You don the white coat and the rest of the attire and calmly walk out of the infirmory. ->:"""))

def smartsTwo():
  input(italics("""
You realize that whoever was running to the elevator might be dangerous so you open the panel under the monitor and rip out a few cords.  The elevator flashes an orange light and makes a sharp clicking sound.  

The person running finally makes it to the elevator. After a few seconds they start banging on the door and then run off furthur down the hallway.  

With that bullet dodged, you get to work on the monitor.  Resetting it, jerry rigging this to that, and finnally getting it started again.  It heads straight for the floor that was blocked off and you tentativly get out the elevator. ->:"""))

def smartsPath(stats):
  print(italics("""
Disregarding what the hooligans are saying, you head back into the elevator.
You fiddle around with the console again and lock the door."""))
  print("Boss where ya goin... you just gonna leave us like this!?")
  print(italics("You keep working on the console and try to block out the banging on the door."))
  input(bold("*BANG*")+" ->:")
  print("Boss, what the hell are ya up to?")
  input(bold("*BAANG*")+" ->:")
  print(italics("Almost there..."))
  input(bold("*BAAANGGG*")+" ->:")
  print("Alright, that's enough.  Let's take care of 'em boys!")
  input(bold("*BLAKAKABLAKABLAKA*")+" ->:")
  input(italics("""
You look up as the sounds of gunshots die down. 

The elevator screeches as it flies down the shaft.  It beeps as it notifies you that you have reached the hangar. ->:"""))
  print(italics("""
There is a open space infront of you with many craft.

'This is it.' you think to yourself...'your chance to escape'.

You run into one of the ships and figure out how to start it up.  It is surprisingly easy for you to do so.

You hit the ignition and blast out of there.

However, as your ship leaves you notice some beeping on your short range sensors alerting you that someone must have taken the second ship.
  """))
  print(italics("The speakers click on, ")+"Boss, where the hell do you think you're going!")
  print(bold("1: I have no idea, but I do know you ain't coming!"))
  print(bold("2: (No response. Gotta figure a way out of this.)"))
  choice=input(bold("::"))
  choice=statCheck(choice) #FOURTH STAGE STAT CHECK
  if choice==1:
    name=input(italics("""
I punch the 2 way monitor. 

And turn the shuttle around.

Taking expert aim, I destroy their front weapons and engines.

With one last shot, the whole area of space was reduced to particles.

I turn the ship around suddenly remembering.

How could I have forget my name ::"""))
    print(italics(bold(f"Ace Pilot {name}.")))
  if choice==2:
    name=input(italics("""
I flew the shuttle around the mother ship and in the moment that I was situated opposite the other craft I turned on the invisibility cloak.  

As soon as the other craft finally made it to the other side I programmed a probe to shoot back the other side of the ship and have it ping the criminals.  They would never be the wiser. 

As they flew off on a wild goose chase.  I turned and flew the other direction laughing the whole way.

I had forgotten.  It is amazing that the Organization was able to outsmart me, but never again.

My exploits will burn into the Galaxy's memory my name ::"""))
    print(italics(bold(f"{name} The Genius Strategist.")))
    

#GAME START NODE ----------------------------------------------------------------
def start(stats):
  print(italics("Your eyes slowly open."))
  input(bold("(Blink)")+"->:")
  input(bold("(Blink)")+"->:")
  print(italics("A nurse notices your movement and rushes to your side."))
  input(bold("(Blink)")+"->:")
  print("DOCTOR!")
  input(bold("(Blink)")+"->:")
  print(italics("You wake up to see someone dressed in a white coat, you suppose that must be the Doctor."))
  print("Well, well... good morning sunshine.  How are you feeling?")
  print(italics("You blink again."))
  print("Now now, let's not wake up on the wrong side of the bed after a 5 year nap.  You have been quite the mystery for us and I think you owe us a little thanks....well maybe we are rushing things lets continue this later on...nurse?")
  input(bold("(Blink)")+"->:")
  print(italics(
    """You wake up and feel considerably better.  You still feel like there are mothballs in your mouth but you find the strength to ask the nurse for some water.

The Doctor comes in not too long after."""
  ))
  print("Feeling a bit more talkitive this time I hope?"+italics(" He smiles."))
  print("Why don't we start easy...how about your name, simple enough right?"+italics(" That same shitty smile."))
  print(italics("You decide to just give him what he wants."))
  input(bold("...")+"->:")
  print(italics("Huh?"))
  print("Come come now, I have been waiting 5 years you know.")
  print(italics("That was weird.  You could have sworn you had said something just now.  You work yourself up to tell this man your name."))
  input(bold("...")+"->:")
  print(italics("What's going on here?"))
  print("Fine, don't talk.  If I were you I would play nice. See I am a  humanitarian, but there are some people here that are very interested in you... can't say the same for them...well anyway let's continue this later.")
  print(italics("""
What the?  Ok calm down.  My name....my name.... my name.

Nothing.

Great.

Come on... something, anything, WHO AM I!

Suddenly, something starts to sprout in your mind.  A lingering feeling.  
  """))
  print(bold("1: That's right, I think I was pretty brave!"))
  print(bold("2: Ahh yes, I was cunningly charismatic."))
  print(bold("3: I am sure I was very smart!"))
  choice=input(bold("::"))
  statCheck(choice) #FIRST STAGE STAT CHECK
  print(italics("""
The hallway is empty.  You take a few more steps and are immediatly blasted by the sound of alarms and flashing red lights.  

You thought you were done for, but no one came running down the hallway.  There was definitly commotion but it sounded way off.  

The urge to escape grows even stronger in you. 

You think there there must be a way out of here, as you run down the hallway.

Moments later you stumble upon an elevator.

The display shows a list of floors to go to.  

There is a floor that is blocked of from the rest and the display won't let you access it.   

From the distance you can hear someone running towards the elevator.
  """))

  print(bold("1: Who is that coming!?"))
  print(bold("2: Let me just find a nice place to hide for a second."))
  print(bold("3: I'll just open it up and get it to work."))
  choice=input(bold("::"))
  statCheck(choice) #SECOND STAGE STAT CHECK
  print(italics("""
The scene before you is gruesome.  There is blood and viscera everywhere.  

You hear wooping and screaming up ahead.  There is not much you can do as the sound gets louder and you see some shapes running at you.

You take a step back and hear another bellow.
  """))
  input("WOOOOOOOHAHA!->:")
  print(italics("This is it..."))
  input("THERE! ANTOHER ONE! RIP THEIR HEART OUT GENTS!!! ->:")
  input("wait is that...HOLD! ... BOSS?!? ->:")
  print(italics("Huh?"))
  print("Boss it's you! We did it boys, we found 'em, yearghahhahaha!'")
  print("Boss, where ya been?  We been lookin' for ya fer years and look at cha', here right when we need ya!")
  
  #This player prompt dynamically displays a number of options based on previous choices
  #To ensure the numbering is correct, it will increment [number] only if there are more options and adjust what gets printed accordingly
  #A 'dict' (basically hashmap) [option] is created so that the new input order can be mapped and the value that gets passed on to [statCheck] is manually adjusted to match other instances of the stat check.
  brave="No clue who these guys are.  If they are responsible for this I have to teach them a lesson."
  charisma="Hrm, I have no idea what's going on, but these guys might come in handy."
  smarts="They think I'm their leader? These guys are definitely dangerous...gotta get outta here."
  number=1
  option={}
  if stats.bravery>=1:
    print(bold(f"{number}: {brave}"))
    option[number]="brave"
    number+=1
  if stats.charisma>=1:  
    print(bold(f"{number}: {charisma}"))
    option[number]="charisma"
    number+=1
  if stats.smarts>=1:
    print(bold(f"{number}: {smarts}"))
    option[number]="smarts"
  choice=input(bold("::"))
  choice=checkOneTwo(choice) #make sure player types 1 or 2

  #THIRD STAGE STAT CHECK
  if option[choice]=="brave":
    statCheck(1) 
  if option[choice]=="charisma":
    statCheck(2) 
  if option[choice]=="smarts":
    statCheck(3) 

    
#begin the game
stats=Player() #player object containing stat values and stage position
intro(stats)
print("THE END! THANKS FOR PLAYING!")