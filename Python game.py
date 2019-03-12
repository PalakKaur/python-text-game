#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 21:09:00 2018

@author: palakkaur
"""

"""
   DocString:
    
   A) Introduction:
   This game is inspired from the movie, Monster House(2006).
   It consists of three stages, and also has defined functions
   for start, win, and lose. Playing this game requires honesty.
    
   Round 1: Climb the stairs to the top of the hill.
   Round 2: Enter the house.
   Round 3: Save your sister.
    
   B) Known Bugs and/or Errors:
   None. 
"""

from sys import exit
import random

#Start function

def start():
      
      global player_name
      global least_fav_veggie
    
      player_name = input("> Please enter your name to begin <\n")
      player_name = player_name.capitalize()
      least_fav_veggie = input("> Now please enter one vegetable(singular) that you hate <\n")
    
      print(f"""\n\n       
                  _   __            
                  \'._(oo)           
                   `.   (_.'/     
                  .'_.'-..'     
                ~
               _m_            +-+-+-+-+-+-+-+ +-+-+-+-+-+ 
              /\ ___\         |M|o|n|s|t|e|r| |H|o|u|s|e| 
             /  \____\        +-+-+-+-+-+-+-+ +-+-+-+-+-+
             |  |""  |    
      _______|  |____|___________________________________________________

                
      Welcome, {player_name}!
      It is halloween night and your sister, Cindy, is out for a party 
      at the old house on top of the hill. She sends you a text message
      at midnight asking to rescue her and her mobile switches off after
      that. You reach the venue as soon as possible.
      Hmm. Something is weird about this place.
      It reminds you of those horror movies with scary backgroud music.
      You take a deep breath and brace yourself for the impending danger.""")
      input("\n> Press enter to start the game <")

#Round 1: Climb up the stairs
      print("""\n
      First comes the long climb up the stairs leading to the house.""")
      climb_stairs()
    
def climb_stairs():
      print(f"""
      As you're on your way up, a huge, scary tree tries to grab you.
      What would you do?
         a) Say "I'm {least_fav_veggie}" out loud and you get a free ride
            to the next stage (Be honest. THE HOUSE IS WATCHING!!)
         b) Pick your nose and stick a booger on the tree 
         c) Sing a romantic song for the tree""")
   
      choice = input(">  \n").lower()
      choice = choice.lower()
     
      if "a" in choice or "1" in choice or "eat" in choice:
        print("""\n\t Not adventerous enough, eh?
\n\n\n\t\t\tYou have cleared this stage. Let's head to the house.\n""")
        input("\n> Press enter to continue <")
        house_entrance()
  
      elif "b" in choice or "2" in choice or "nose" in choice or "booger" in choice :
        print("""\n\t Good work! The tree is a hygiene freak and is going to spend hours showering.\n\t Your way is now clear.
\n\n\n\t\t\tLet's head to the house.\n""")
        input("\n> Press enter to continue <")
        house_entrance()
  
      elif "c" in choice or "3" in choice or "sing" in choice or "song" in choice :
        print(f"""\n\t Oopsie! Looks like the tree isn't a fan of your song.\n\t Run or you will become it's dinner!\n\t Better luck next time, {player_name}!""")
        fail()
   
      else :
        print("\nInvalid input. Please try again.")
        climb_stairs()

#Round 2 : Enter the house
def house_entrance():
      print("""\n
      It's dark and quiet. Suddenly, you hear someone, "I SMELL HOOOMAN BLOOD",
      but there's nobody in sight. You try to open the door.
         """)
      input("> Press enter to continue <")
      print("\t\t\n\n      *E*L*E*C*T*R*I*C*S*H*O*C*K*")
      print("""
                                   ,/
                                 ,'/
                               ,' /
                             ,'  /_____,
                           .'____    ,'    
                                /  ,'
                               / ,'
                              /,'
                             /'
       
        """)
      input("""      That did not go quite well!
      The door knob gave you an electric shock.
\n\n> Press enter to continue <""")
      door()
    
    #Door function
def door():   
      print("""\n\n      You hear someone again. This time louder:
      "Once inside, nobody is allowed to go back, kid! Run away,
      this house isn't for the faint-hearted. I bet you can't last
      a minute." What would you say?
         a) "I want my Mommy!"
         b) "I am a warrior! I will not leave without my sister." """)
      
      choice_1 = input("> \n").lower()
      choice_1 = choice_1.lower()
      
      if "a" in choice_1 or "1" in choice_1 or "mom" in choice_1 :
            print(f"\n\t Good bye, {player_name}!\n\t Come prepared next time.")
            fail()
         
      elif "b" in choice_1 or "2" in choice_1 or "sis" in choice_1 :
            print("""\n\t "Alright! Don't say I didn't warn ya!
         But first, let's play a game.
         I will tell you 2 jokes, and because I am very funny,
         if you can control your laughter, the door opens for you.
         If not, sorry kid, you will have to leave."\n""")
            input("> Press enter for the joke <\n")
            joke_time()
      
      else:
            print("Invalid input. Please try again.")
            door()     

    #Joke time function
def joke_time():
    import random
    joke_list= ["""\n\t "What did the buffalo say to its son?......... \n\n\t BYE-SON!" """,
                        """\n\t "What happens when you have a bladder problem?.......\n\n\t Urine trouble!" """,
                        """\n\t "What do Alexander the Great and Winnie the Pooh have in common?.......\n\n\t Same middle name!" """,
                        """\n\t "Why is the ocean blue?......... \n\n\t Because all the little fish go blu, blu, blu" """,
                        """\n\t "What does a ghost wear when it is raining?......... \n\n\t BOOOOOOOOOOOOOOOOOOOTS!" """,
                        """\n\t "What does a vegan zombie eat?......... \n\n\t GRAAAAAAAAAAAAAAAAAAAAAAAAINS!" """]
    
    joke_sample = random.sample(joke_list, 2)
           
    #For loop 
    for jokes in joke_sample:
                  
                  
        print(jokes)
        print(" ")
        input("> Press enter key <")
                
        if jokes == joke_sample[0]: 
          #Did you laugh function  
          def didyoulaugh():
            reaction=input("\n      Did you laugh?(y/n):").lower()
            reaction=reaction.lower()  
            if "y" in reaction:
                print("""\n\t "Shoo away! Told you I'm funny."\n""")
                input("> Press enter to continue <")
                print("\n      And we're back to the stairs!")
                climb_stairs()
                        
            elif "n" in reaction:
                print("""\n\t "Good job!"\n""")   
                input("> Press enter key <\n")
            
            else:
                print("Invalid input. Please try again.")
                didyoulaugh()
                     
          didyoulaugh()
                      
        if jokes == joke_sample[1]:        
             didyoulaugh()       
             print("""\n\t "Fine! I will let you enter." """)             
    save_sister()


#Round 3 : Save Cindy                    
def save_sister():
    input("""
        \n\t\t\t\tYou have cleared the test. Welcome to MONSTER HOUSE! \n\n\n> Press enter to continue <\n""")
    print("""
      The door shuts on its own. It is quiet. Who would believe
      there was a party here? Was your sister really here?
      You spot a mysterious woman wearing Cindy's jacket! She was here!!
      You ask her about your sister.""")
    input("\n> Press enter to continue <")
    print(f"""\n
      {player_name}: "Hello, do you know where Cindy is?" """)
    comment()

    #Comment Function    
def comment():
      input("\n> Press enter to continue <\n")  
      comment = (random.randint(1,3))
         
      if comment == 1:
         print("""\n      Mysterious Woman: "I WANT YOUR BLOOD"\n""")
         print("""\n      You start running out of fear and end up in the basement.""")
         input("\n> Press enter to continue <")
         basement()
         
      elif comment == 2:
         print("""\n      Mysterious Woman: "Which oil would you like to be cooked in? Olive or canola?"\n""")
         print("""\n      You start running out of fear and end up in the basement.""")
         input("\n> Press enter to continue <")
         basement()
         
      else:
         print("""\n      Mysterious Woman: "HOOOOMAN! GO TO BASEMENT! HE IS HUNGRY!!"\n""")
         print("""\n      You hear a scream from the basement. It's your sister!
      Looks like you HAVE to go to the basement.""")
         input("\n> Press enter to continue <")
         basement()

    #Basement function
def basement():
      print("""\n\n      Holy moly, this is a mess! The giant furnace is trying to swallow Cindy
      and the only thing keeping her alive is the broom stick stuck in its mouth.
      What would you like to do? QUICK!!!!!
         a) Tickle the furnace
         b) Help the furnace because Cindy never gave you the TV remote
             during childhood""")
 
      furnace = input("> \n").lower()
      furnace = furnace.lower()
     
      if "a" in furnace or "1" in furnace or "tickle" in furnace :
         print("\n\t The furnace laughed its ass off(literally) and died. I am proud of you!")
         hero()
        
      elif "b" in furnace or "2" in furnace :
         print("""\n\t YOU NEED TO FIGURE OUT YOUR PRIORITIES!!!!!""")
         fail()
         
      else :
         print("Invalid input. Please try again.")
         basement()

#Winner function     
def hero():
      print(f"""\n\n\t\tCongrats, {player_name}! You saved Cindy!\n\n
            """)
      exit()

#Game Over function
def fail():
      print(f"""\n\n\n\t\t\t\tGAME OVER!""")
      play_again()
      
#Play again function      
def play_again():
      choice = input("      Would you like to play again?(y/n):").lower()
      choice = choice.lower()
      print("\n\n")
      if "y" in choice or "play" in choice :
         start()   
      
      elif "n" in choice or "exit" in choice :
         exit()
      
      else:
         print("Invalid input.")
         play_again()
    
start()                        