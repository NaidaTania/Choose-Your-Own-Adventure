#Not a battleship

#defining functions

def lowercase(words):
    return words.lower()

#all variables here
me = "me"
yes = ['yes','ye','ya','yeah','yep','yap','yass','y','of course','of course!','pretty much','i do','duh','yeap','sure','go in','i am']
no = ['no','mo','nope','nah','n','non','not really','kinda','sort of','a bit','i guess','barely','vaguely','somewhat','soso','i don\'t','not rly']
straight = ['straight','straight ahead','ahead','up','forward','fwd','s','go straight','go straight ahead','go ahead']
left= ['left','go left','turn left','to the left','l']
right= ['right','go right','turn right','to the right','r']
home = ['home','back','behind','nowhere']

#all repeated qn?again
library = "There's the library too. Shall we go inside?"
again = "Let's try this again."
go = "Where shall we go to?"
hallReady = "\nI'd like to bring you to my favorite spot. It's just around the corner.\nBut the HALL is right before our face.\n\nAre you ready?"
lt4Convo = "Apples is to red as LT4 is too...?"

print "Welcome!\nI\'m " + me + " and I\'ll be your guide for today!\n\nPlease type your name and hit \'enter\'"

username = raw_input('>> ')
lowercase(username)

#omitted special if case for the intended recipient :D

if username == "":
    print "\nThe silent type, eh?"
else:
    nickname = username
    me = 'Nana'
    stairsConvo = "Somehow I recall those days when we rush up and down these stairs with tons of beakers in hand lol."
    hallConvo = "\nThere's that one time when we stared at the teachers list for some reason,\nand another time when we nearly got scolded by the PE teacher for some reason.\nI forgot why XD"
    smackConvo = "There's that table where we queue for night study food so often."
    straightConsultConvo = "Here we are, the area where we spend countless nights consulting Mr Marie."
    stairsConvo2 = "Remember the hours we spent sitting on the table staring at the Chess Club wall? XD"
    wallOfFameConvo = "Look at this history of AJ...And the time we spent oogling at this for lulz."

print """\nI see.
I shall call you %s~ :3""" %(nickname)

print """\nSo, here we are, at AJ!
Do you still remember it?\n
Please type out your answer when this blinking prompt appears and hit 'enter'"""
qnRemember = lowercase(raw_input('>> '))
'''--------- tutorial remember AJ input loop ----------'''
counter = 1
if qnRemember == "":
    print "\nTutorial (for you who is a noob at " + me + "\'s \'interactive fiction\' lol"
    print "Try typing \'yes\'"
    qnRemember = lowercase(raw_input('>> '))
    if qnRemember == "":
        while counter<4 and qnRemember == "":
            counter+=1
            print again
            qnRemember = lowercase(raw_input('>> '))
            if counter == 4:
                break
            elif qnRemember != "":
                break

for x in yes:
    if (qnRemember == x ):
        print "\nI know right! How nostalgic!"
for y in no:
    if (qnRemember == y ):
        print "\nBut it wasn't that long ago!"
if (qnRemember not in yes) and (qnRemember not in no):
    print "\nRight..."
    print "Maybe a \'yes\' or a \'no\' will do next time?"

print "\nAh, but we shouldn't waste anymore time here. We must get to the HALL, fast!"
print "You do remember this back entrance, right?"
qnRemember2 = lowercase(raw_input('>> '))

if qnRemember2 in yes:
    print "\nGreat!"
elif qnRemember2 in no :
    print "\nIt's alright."
else:
    print "\n...Right."

print "Just tell me which direction you want to go to."
print "\nGoal: Get to the HALL."
print "Choose between straight ahead, left or right."
print go
goEntrance = lowercase(raw_input('>> '))
'''--------- first direction choice ----------'''

while goEntrance not in (straight+left+right+home):
    print "Straight, left, or right. I'm sure those are simple enough for you to understand, right?"
    print go
    goEntrance = lowercase(raw_input('>> '))

while goEntrance in home:
    print "\nNO."
    print again
    print go
    goEntrance = lowercase(raw_input('>> '))

if goEntrance in left:
    print "\nAh, the Elementz Lab.\nI used to self study a lot here. Gazing at this mini garden always puts my heart at ease~\n"
    print library
    goLibrary = lowercase(raw_input('>> '))
    if goLibrary in yes:
        print "\nThat's a trick question.\nGet back on track %s!" %(nickname)
        print again
        goLibrary = lowercase(raw_input('>> '))
        if goLibrary in yes:
            print "\nI said no."
        else:
            print "\nFinally."
    elif goLibrary in no:
        print "\nGood call."
    else:
        print "\n...Right."
    print "We should focus on task at hand."
    print "\nThere's the canteen to our right, the best place in the entire school~"
    print "\nBut if we go straight and take the stairs, we'll reach the hall immediately."
    print go
    goLeftIntersection = lowercase(raw_input('>> '))
    if goLeftIntersection in left:
        print "\nThere's Ohana, our \'home\', the Good News Cafe, and some other stuff there, but not now.\nLet's go back and head straight instead.\n"
        print go
        goLeftIntersection = lowercase(raw_input('>> '))
        counter2 = 1
        while goLeftIntersection in left:
            counter2+=1
            print "\nI said HEAD STRAIGHT"
            print go
            goLeftIntersection = lowercase(raw_input('>> '))
            if counter2 > 3:
                print "\nFUCK IT"
                break
        goLeftIntersection = 'straight'
    if goLeftIntersection in right:
        print '\n...I know I said there\'s the canteen, but that doesn\' mean we have to go here y\'know...\n'
        print 'Porridge --- $2.50'
        print 'Mantou ----- $0.50'
        print 'Egg tart --- $0.50'
        print "Since we\'re here anyway, anything you want?\n"
        yourOrder = lowercase(raw_input('>> '))
        if yourOrder in no:
            print '\nIf you say so...'
        elif yourOrder in 'porridge,mantou,egg tart':
            print '\nKay here\'s your %s.' %(yourOrder)
        elif yourOrder in 'all,everything,all of them':
            print '\nSure, but you\'re paying~'
        else:
            print '\nNo. Imma give you a mantou. It\'s my favorite~'
        print 'Now let\'s get back on our mission.'
        goLeftIntersection = 'straight'
    else:
        print "\nUp the stairs we go!"
        print stairsConvo
        print "Ah, the HALL toilet place as well as a bunch of club walls!"
        print stairsConvo2
        print hallReady
        lowercase(raw_input('>> '))
        #Enter final HALL scene

elif goEntrance in straight:
    print "\nWelcome to the...hall?\nWe don't really spend much time here."
    print hallConvo
    print "\nAnyway, the way to the HALL is to the left."
    print go
    straightIntersection = lowercase(raw_input('>> '))
    if straightIntersection in right:
        print "\nDo you have something to do in the General Office?"
        straightGenOffice = lowercase(raw_input('>> '))
        if straightGenOffice in yes:
            print '\nIt can wait.'
        elif straightGenOffice in no:
            print '\nWhy are we even here then?!'
        print "Step back. We're taking the stairs.\n\n"
        print straightConsultConvo
        print "The tables, the teacher's room, the pigeon holes...It brought back so much memories."
        print hallReady
        lowercase(raw_input('>>'))
        #Enter final HALL scene (need to modify for repetition with below)

    elif straightIntersection in straight:
        print "\nSMACK!!\nIf you're trying to smack your head against the centre pillar then congratulations, you did it!"
        print "Okay, so there's a list of achievements and trophies."
        print smackConvo
        print "There's the canteen, but I'm not hungry. Are you?"
        straightHungry = lowercase(raw_input('>> '))
        if straightHungry in yes:
            print "\nHere, a candy. Now let's hurry to the HALL!"
        elif straightHungry in no:
            print "\nWhat are we doing here let's go to the HALL!"
            print straightConsultConvo
            print "\nThe tables, the teacher's room, the pigeon holes...It brought back so much memories."
            print hallReady
            lowercase(raw_input('>> '))
            #Enter final HALL scene (need to modify look above)
    elif straightIntersection not in left:
        print "\nLet's take the easiest route."
    else:
        print "\nTo your left, you can see the holy statue that is AJ's idk-why-they-made-it-phallic-shaped statue!"
        print "To your right, there's the canteen, but you're not hungry so let's pass that."
    print "Up the stairs we go!"
    print stairsConvo
    print "\nAh, the HALL toilet place as well as a bunch of club walls!"
    print stairsConvo2
    print hallReady
    lowercase(raw_input('>> '))
    #Enter final HALL scene (it the same as left path how to loop there...)

elif goEntrance in right:
    print "\nGuess we're taking the 2nd floor route then."
    print "\nHere we are, right before LT4."
    print lt4Convo
    lt4Ans = lowercase(raw_input('>> '))
    print "Yes that. Apples is to red as LT4 is to %s" %(lt4Ans)
    print "If that doesn't make sense you're responsible for it %s!" %(nickname)
    print "Anyway,", go
    rightLT4 = lowercase(raw_input('>> '))
    if rightLT4 in left:
        print "We're so not doing chem lecture now."
        print go
        rightLT4 = lowercase(raw_input('>> '))
    elif rightLT4 in home:
        print "The only way is to go 'straight' or 'right'."
        print go
        rightLT4 = lowercase(raw_input('>> '))
    elif rightLT4 in right:
        print wallOfFameConvo
        print straightConsultConvo
        print "\nThe tables, the teacher's room, the pigeon holes...It brought back so much memories."
        print hallReady
        lowercase(raw_input('>> '))
        #Enter final HALL scene
    elif rightLT4 in straight:
        print "Ah...my second favorite spot lol."
        print "We have some really nice memories here, mostly mugging."
        print library
        lowercase(raw_input('>> '))
        print "\nNo. Hall is just right there. We're going straight!\nLet's go!"
        print "\nAh, the HALL toilet place as well as a bunch of club walls!"
        print stairsConvo2
        print hallReady
        lowercase(raw_input('>> '))
        #Enter final HALL scene
    else:
        print again
        rightLT4 = lowercase(raw_input('>> '))

#THE HALL SCENE LOL oh quizzes along the way yep that'll do :D
print """Let's go inside! Prepare yourself!!
This is a very anticlimatic way to end this game lol
No matter, my main intention is just to make a gift.
So...Happy Birthday!
\n~This is The End of the game.
Please press enter one last time to end game."""
raw_input('>> ')

