from functions import *
import pygame


def checkpoint0():
    story("You slowly open your eyes and wonder why it's still so dark. ")
    story("You realise the that the floor beneath you is cold hard stone and your body is aching. ")
    story("Panic starts to grip you and you stare frantically around trying to make sense of your surroundings. ")
    decision1 = story("You can just about make out a door in front of you. Do you REACH for this door or continue to LOOK around? ", ["REACH", "LOOK"])
    if decision1 == "REACH":
        story("You grasp the door handle but to your horror it turns out to be a blade! ")
        story("You leap back but there is a deep cut running along your palm. ")
        decision2 = story("Do you IGNORE the pain and try and escape as quickly as possible or stop to BANDAGE the wound? ", ["IGNORE", "BANDAGE"])
        if decision2 == "IGNORE":
            things_to_deal_with.append("injured hand")
            story("Your hand is bleeding badly but you grit your teeth and inspect the fake door handle. ")
            story("The blade is loose and you carefully work it out with your uninjured hand. ")
            story("You now have a makeshift weapon which may come in useful. ")
            decision3 = story("Do you try to OPEN the door or continue to LOOK around the room you are currently in? ", ["OPEN", "LOOK"])
            if decision3 == "LOOK":
                decision1 = "LOOK"
            elif decision3 == "OPEN":
                pass
        elif decision2 == "BANDAGE":
            story("You try to rip off a strip of your t-shirt with your uninjured hand and wrap it round your other one. ")
            story("It stings badly but you pull it tight and the flow of blood slows. ")
            story("Just as you look up, you hear a swish and a click. The fake door handle is pulled back into the room beyond. ")
            story("You push at the door but it doesn't budge. ")
            decision4 = story("Do you try to BREAK the door down or continue to LOOK around the room you are currently in? ", ["BREAK", "LOOK"])
            if decision4 == "LOOK":
                decision1 = "LOOK"
            elif decision4 == "BREAK":
                pass
    if decision1 == "LOOK":
        pass


checkpoints = [checkpoint0]
checkpoint = 0

things_to_deal_with = []

if __name__ == "__main__":
    pygame.init()
    story("In this game you have to press enter to continue with the story. Try it now. ")
    story("Welcome to...")
    story("THE BEAR")
    decision0 = story("""At certain points you will be asked to make a decision.
    The words you are allowed to type will be in capitals. Do you understand, YES or NO? """, ["YES", "NO"])
    if decision0 == "YES":
        story("Well then, let's begin...")
        while True:
            checkpoints[checkpoint]()
    elif decision0 == "NO":
        story("This game is clearly too advanced for you, go back to Candy Crush. ")
        story("Bye bye...")
        pygame.quit()
