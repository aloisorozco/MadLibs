#MadLibs

#Mad Libs is a word game where one player asks others for a list of words to replace for blanks in a story, before reading the story aloud. Usually the story is very comic and funny.

#print("hello",end="")
import random
import time
from termcolor import colored
import sys
#sys.modules[__name__].__dict__.clear()
#clears every variable


madLibs = [["My","(relative)","went","to","(city/country)","with","Juan.","There","they","bought","a","(noun)","for","(number)","dollars.","They","also","drank","(type of liquid/drink)","with","(name)","and","they","(verb at the past tense)","all","day","long."],["Easter","is","my","favourite","holiday.","I","love","it","when","my", "mom", "prepares", "my","favourite","dish:","(food)",".", "It", "is", "so", "(adjective)","." ,"My", "dad" ,"always", "(action)", "in", "the" ,"living", "room" ,"while" ,"my" ,"brother" ,"watches." ,"The" ,"egg", "hunt" ,"is" ,"always" ,"(adjective)","." ,"The" ,"best", "thing", "to","do" ,"is" ,"to", "(verb)", "(adverb)","."],["Fortnite is","(adjective)",". It is a battle royale game filled with lots of","(adjective)","(noun)",". It is","(adjective)","to play! Unlike PUBJ, a","(adverb)","(adjective)","battle royale game, Fortnite is casual. Getting wins in Fortnite is like","action","."],["Zoos are","(adj)","!","(Adj)","animals such as monkeys, elephants, and penguins are awesome to","(verb)", "at. My","(noun)","always","(verb)","(noun)","for lunch. I wish they would be more","(adj)",". They","(verb)","me","(adverb)","."],["There are many ways to cheat on a test. First, you can","(verb)","next to the smartest person in your class. You can also steal the test beforehand and copy down all the answers. Also, you could correct your own test and have the","(adj)","score in the class. That","(noun)",",","(name)","will think you're so","(adj)","."],["Nature is so","(adj)",". It really brings me","(adj)","pleasure. I love the smell of","(adj)","air. Camping is a fun way to experience the beauties of nature. The sunset is so","(adj)","and I love","(action)",". But, by far, the most fun thing of camping, is","(verb ending in -ing)","(noun)","around the campfire."]]



x = True
while x == True:
  play_or_not = input("Would you like to play a quick game of Mad Libs!?")
  print('\n' * 1)
  time.sleep(1)
  if play_or_not == "Y" or play_or_not == "y" or play_or_not == "Yes" or play_or_not == "yes":
    break
  elif play_or_not == "N" or play_or_not == "n" or play_or_not == "No" or play_or_not == "no":
    "Alright. Quitting program..."
    quit()
  else:
    "Enter Y or N."
    continue


while True:
  instructions_or_not = input("Would you like to know how to play Mad Libs?")
  print('\n' * 1)
  time.sleep(1)
  if instructions_or_not == "Y" or instructions_or_not == "y" or instructions_or_not == "Yes" or instructions_or_not == "yes":
    print(colored("How to play:",'red'),end="")
    print(" The program will ask you for various words that you will need to input. Once you have inputed all the needed words, the program will display a story with your words inserted into the story. You can input all types of silly stuff to get a good laugh at the final result.")
    print('\n' * 2)
    time.sleep(2)
    break
  elif instructions_or_not == "N" or instructions_or_not == "n" or instructions_or_not == "No" or instructions_or_not == "no":
    break
  else:
    "Enter Y or N."
    continue


while True:
  while True:
    print(colored("1. My relative's trip" ,'red'))
    print(colored("2. Easter" ,'green'))
    print(colored("3. Fortnite" ,'blue'))
    print(colored("4. Zoos!" ,'magenta'))
    print(colored("5. How to cheat on a test" ,'cyan'))
    print(colored("6. The beauties of nature" ,'yellow'))
    mad_libs_num = int(input("Enter the number of the Mad Libs you would like to play:"))
    mad_libs_num = mad_libs_num - 1
    if mad_libs_num == 0 or mad_libs_num == 1 or mad_libs_num == 2 or mad_libs_num == 3 or mad_libs_num == 4 or mad_libs_num == 5:
      break
    else:
      print("Please enter a number between 1 to 6.")
  print('\n' * 1)
  time.sleep(1)
  print(colored("REMINDER:" ,'red') ,end="")
  print(" You may enter" ,end="")
  print(colored(" \"EXAMPLE\"" ,'red') , end="")
  print(" in all caps at any point of the game to get an example of what type of word the program demands.")
  print('\n' * 2)
  time.sleep(2)

  if mad_libs_num == 0:
    z = True
    while z == True:
      ex = 0
      relative_ex = ["brother","sister","dad","grandmother"]
      ex = random.randrange(4)
      relative = input("Enter a relative:")
      print('\n' * 1)
      if relative == "EXAMPLE" or relative == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(relative_ex[ex],'magenta'))
        continue
      else:
        break
    a = True
    while a == True:
      ex = 0
      city_country_ex = ["Paris","Canada","Iran","London"]
      ex = random.randrange(0,4)
      city_country = input("Enter a city/country:")
      print('\n' * 1)
      if city_country == "EXAMPLE" or city_country == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(city_country_ex[ex],'green'))
        continue
      else:
        break
    b = True
    while b == True:
      ex = 0
      noun_ex = ["purse","cat","hat","soda"]
      ex = random.randrange(0,4)
      noun = input("Enter a noun:")
      print('\n' * 1)
      if noun == "EXAMPLE" or noun == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(noun_ex[ex],'yellow'))
        continue
      else:
        break
    c = True
    while c == True:
      number = input("Enter a number:")
      print('\n' * 1)
      if number == "EXAMPLE" or number == "\"EXAMPLE\"":
        print("Here's an example:",end="")
        print(colored(" 10",'grey'))
        continue
      else:
        break
    d = True
    while d == True:
      ex = 0
      type_of_liquid_ex = ["beer","wine","soda","water"]
      ex = random.randrange(0,4)
      type_of_liquid = input("Enter a type of liquid/drink:")
      print('\n' * 1)
      if type_of_liquid == "EXAMPLE" or type_of_liquid == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(type_of_liquid_ex[ex],'cyan'))
        continue
      else:
        break
    e = True
    while e == True:
      ex = 0
      name_ex = ["James","Tom","John","Mr. White"]
      ex = random.randrange(0,4)
      name = input("Enter a name: ")
      print('\n' * 1)
      if name == "EXAMPLE" or name == "\"EXAMPLE\"":
        print("Here's an example:",end="")
        print(colored(name_ex[ex],'cyan'))
        continue
      else:
        break
    f = True
    while f == True:
      ex = 0
      verb_ex = ["sung","slept","talked"]
      ex = random.randrange(0,3)
      verb = input("Enter a verb at the past tense:")
      print('\n' * 1)
      if verb == "EXAMPLE" or verb == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(verb_ex[ex],'blue'))
        continue
      else:
        break
    print('\n' * 5)
    madLibs[0][1] = relative
    madLibs[0][4] = city_country
    madLibs[0][11] = noun
    madLibs[0][13] = number
    madLibs[0][18] = type_of_liquid
    madLibs[0][20] = name
    madLibs[0][23] = verb
    for word in madLibs[0]:
      if word == relative or word == city_country or word == noun or word == number or word == type_of_liquid or word == name or word == verb:
        print(colored(word, 'magenta'),end=" ")
      else:
        print(word,end=" ")
  
  #####################################
  if mad_libs_num == 1:
    z = True
    while z == True:
      ex = 0
      food_ex = ["lasagna","burger","soup","rice and chicken"]
      ex = random.randrange(0,4)
      food = input("Enter food:")
      print('\n' * 1)
      if food == "EXAMPLE" or food == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(food_ex[ex],'magenta'))
        continue
      else:
        break
    a = True
    while a == True:
      ex = 0
      adjective_ex = ["delicious","yummy","healthy","exciting"]
      ex = random.randrange(0,4)
      adjective = input("Enter an adjective:")
      print('\n' * 1)
      if adjective == "EXAMPLE" or adjective == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(adjective_ex[ex],'yellow'))
        continue
      else:
        break
    b = True
    while b == True:
      ex = 0
      action_ex = ["sings karaoke","watches TV","plays guitar","plays the piano"]
      ex = random.randrange(0,4)
      action = input("Enter an action:")
      print('\n' * 1)
      if action == "EXAMPLE" or action == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(action_ex[ex],'grey'))
        continue
      else:
        break
    c = True
    while c == True:
      ex = 0
      adjective2_ex = ["awesome","exciting","amazing","cool"]
      ex = random.randrange(0,4)
      adjective2 = input("Enter another adjective:")
      print('\n' * 1)
      if adjective2 == "EXAMPLE" or adjective2 == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(adjective2_ex[ex],'green'))
        continue
      else:
        break
    d = True
    while d == True:
      ex = 0
      verb_ex = ["wait","rush","eat","demand"]
      ex = random.randrange(0,4)
      verb = input("Enter a verb:")
      print('\n' * 1)
      if verb == "EXAMPLE" or verb == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(verb_ex[ex],'cyan'))
        continue
      else:
        break
    e = True
    while e == True:
      ex = 0
      adverb_ex = ["patiently","peacefully","cheerfully","wholeheartedly"]
      ex = random.randrange(0,4)
      adverb = input("Enter an adverb:")
      print('\n' * 1)
      if adverb == "EXAMPLE" or adverb == "\"EXAMPLE\"":
        print("Here's an example:",end="")
        print(colored(adverb_ex[ex],'magenta'))
        continue
      else:
        break
    madLibs[1][15] = food
    madLibs[1][20] = adjective
    madLibs[1][25] = action
    madLibs[1][39] = adjective2
    madLibs[1][48] = verb
    madLibs[1][49] = adverb
    for word in madLibs[1]:
      if word == food or word == adjective or word == action or word == adjective2 or word == verb or word == adverb:
        print(colored(word, 'magenta'),end=" ")
      else:
        print(word,end=" ")

  #####################################
  #Fortnite is (adjective). It is a battle royale game filled with lots of (adjective) (noun). It is (adj) to play! Unlike PUBJ, a (adverb) (adj) battle royale game, Fortnite is more casual. Getting wins in Fortnite, is like (action).

  if mad_libs_num == 2:
    z = True
    while z == True:
      ex = 0
      adjective_ex = ["awesome","amazing","great"]
      ex = random.randrange(0,3)
      adjective = input("Enter an adjective:")
      print('\n' * 1)
      if adjective == "EXAMPLE" or adjective == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(adjective_ex[ex],'magenta'))
        continue
      else:
        break
    a = True
    while a == True:
      ex = 0
      adjective2_ex = ["action-pacted","crazy","exciting"]
      ex = random.randrange(0,3)
      adjective2 = input("Enter an adjective:")
      print('\n' * 1)
      if adjective2 == "EXAMPLE" or adjective2 == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(adjective2_ex[ex],'yellow'))
        continue
      else:
        break
    b = True
    while b == True:
      ex = 0
      noun_ex = ["action","fun","warfare","diversity"]
      ex = random.randrange(0,4)
      noun = input("Enter a noun:")
      print('\n' * 1)
      if noun == "EXAMPLE" or noun == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(noun_ex[ex],'grey'))
        continue
      else:
        break
    c = True
    while c == True:
      ex = 0
      adjective3_ex = ["awesome","exciting","amazing","cool"]
      ex = random.randrange(0,4)
      adjective3 = input("Enter another adjective:")
      print('\n' * 1)
      if adjective3 == "EXAMPLE" or adjective3 == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(adjective3_ex[ex],'green'))
        continue
      else:
        break
    d = True
    while d == True:
      ex = 0
      adverb_ex = ["really","extremely","horrifyingly","terribly"]
      ex = random.randrange(0,4)
      adverb = input("Enter an adverb:")
      print('\n' * 1)
      if adverb == "EXAMPLE" or adverb == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(adverb_ex[ex],'cyan'))
        continue
      else:
        break
    e = True
    while e == True:
      ex = 0
      adjective4_ex = ["bad","terrible"]
      ex = random.randrange(0,2)
      adjective4 = input("Enter an adjective:")
      print('\n' * 1)
      if adjective4 == "EXAMPLE" or adjective4 == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(adjective4_ex[ex],'magenta'))
        continue
      else:
        break
    f = True
    while f == True:
      ex = 0
      action_ex = ["climbing Mount Everest","drinking water","finding gold on the beach"]
      ex = random.randrange(0,3)
      action = input("Enter an action:")
      print('\n' * 1)
      if action == "EXAMPLE" or action == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(action_ex[ex],'magenta'))
        continue
      else:
        break
    madLibs[2][1] = adjective
    madLibs[2][3] = adjective2
    madLibs[2][4] = noun
    madLibs[2][6] = adjective3
    madLibs[2][8] = adverb
    madLibs[2][9] = adjective4
    madLibs[2][11] = action
    for word in madLibs[2]:
      if word == adjective or word == adjective2 or word == noun or word == adjective3 or word == adjective3 or word == adverb or word == adjective4 or word == action:
        print(colored(word, 'magenta'),end=" ")
      else:
        print(word,end=" ")

  
  #####################################
  #There are many ways to cheat on a test. First, you can (verb) next to the smartest person in your class. You can also steal the test beforehand and copy down all the answers. Also, you could correct your own test and have the (adj) score in the class. That (noun), (name) will think you're so (adj).
  if mad_libs_num == 4:
    while True:
      ex = 0
      verb_ex = ["sit","stand","watch"]
      ex = random.randrange(0,3)
      verb = input("Enter a verb:")
      print('\n' * 1)
      if verb == "EXAMPLE" or verb == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(verb_ex[ex],'magenta'))
        continue
      else:
        break
    while True:
      ex = 0
      adjective_ex = ["perfect","best","horrible"]
      ex = random.randrange(0,3)
      adjective = input("Enter an adjective:")
      print('\n' * 1)
      if adjective == "EXAMPLE" or adjective == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(adjective_ex[ex],'magenta'))
        continue
      else:
        break
    while True:
      ex = 0
      noun_ex = ["girl","cat","watch"]
      ex = random.randrange(0,3)
      noun = input("Enter a noun:")
      print('\n' * 1)
      if noun == "EXAMPLE" or noun == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(noun_ex[ex],'magenta'))
        continue
      else:
        break
    while True:
      ex = 0
      name_ex = ["Jessie","Ayla","John"]
      ex = random.randrange(0,3)
      name = input("Enter a name:")
      print('\n' * 1)
      if name == "EXAMPLE" or name == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(name_ex[ex],'magenta'))
        continue
      else:
        break
    while True:
      ex = 0
      adjective2_ex = ["hot","yummy","smart"]
      ex = random.randrange(0,3)
      adjective2 = input("Enter an adjective:")
      print('\n' * 1)
      if adjective2 == "EXAMPLE" or adjective2 == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(adjective2_ex[ex],'magenta'))
        continue
      else:
        break
    madLibs[4][1] = verb
    madLibs[4][3] = adjective
    madLibs[4][5] = noun
    madLibs[4][7] = name
    madLibs[4][9] = adjective2
    for word in madLibs[4]:
      if word == verb or word == adjective or word == noun or word == name or word == adjective2:
        print(colored(word, 'magenta'),end=" ")
      else:
        print(word,end=" ")
    
  
  #####################################
  #Zoos are (adj)! (Adj) animals such as monkeys, elephants, and penguins are awesome to (verb) at. My (noun) always (verb) (noun) for lunch. I wish they would be more (adj). They (verb) me (adverb).
  if mad_libs_num == 3:
    adjective_ex = ["awesome","delicious","scary","horrible","fat","sunny"]
    noun_ex = ["brother","animal","purse","cat","racket","controller"]
    verb_ex =["run","sing","throw","act","eat","make"]
    adverb_ex = ["extremely","horribly","terribly","very","kindly","slowly"]
    while True:
      ex = random.randrange(0,6)
      adjective = input("Enter an adjective:")
      print('\n' * 1)
      if adjective == "EXAMPLE" or adjective == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(adjective_ex[ex],'magenta'))
        continue
      else:
        break
    while True:
      ex = random.randrange(0,6)
      adjective2 = input("Enter another adjective (capitalize the first letter):")
      print('\n' * 1)
      if adjective2 == "EXAMPLE" or adjective2 == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(adjective_ex[ex],'magenta'))
        continue
      else:
        break
    while True:
      ex = random.randrange(0,6)
      verb = input("Enter a verb:")
      print('\n' * 1)
      if verb == "EXAMPLE" or verb == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(verb_ex[ex],'magenta'))
        continue
      else:
        break
    while True:
      ex = random.randrange(0,6)
      noun = input("Enter a noun:")
      print('\n' * 1)
      if noun == "EXAMPLE" or noun == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(noun_ex[ex],'magenta'))
        continue
      else:
        break
    while True:
      ex = random.randrange(0,6)
      verb2 = input("Enter a verb:")
      print('\n' * 1)
      if verb2 == "EXAMPLE" or verb2 == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(verb_ex[ex],'magenta'))
        continue
      else:
        break
    while True:
      ex = random.randrange(0,6)
      noun2 = input("Enter a noun:")
      print('\n' * 1)
      if noun2 == "EXAMPLE" or noun2 == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(noun_ex[ex],'magenta'))
        continue
      else:
        break
    while True:
      ex = random.randrange(0,6)
      adjective3 = input("Enter an adjective:")
      print('\n' * 1)
      if adjective3 == "EXAMPLE" or adjective3 == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(adjective_ex[ex],'magenta'))
        continue
      else:
        break  
    while True:
      ex = random.randrange(0,6)
      verb3 = input("Enter a verb:")
      print('\n' * 1)
      if verb3 == "EXAMPLE" or verb3 == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(verb_ex[ex],'magenta'))
        continue
      else:
        break
    while True:
      ex = random.randrange(0,6)
      adverb = input("Enter an adverb:")
      print('\n' * 1)
      if adverb == "EXAMPLE" or adverb == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(adverb_ex[ex],'magenta'))
        continue
      else:
        break  
    madLibs[3][1] = adjective
    madLibs[3][3] = adjective2
    madLibs[3][5] = verb
    madLibs[3][7] = noun
    madLibs[3][9] = verb2
    madLibs[3][10] = noun2
    madLibs[3][12] = adjective3
    madLibs[3][14] = verb3
    madLibs[3][16] = adverb
    for word in madLibs[3]:
      if word == adjective or word == adjective2 or word == verb or word == noun or word == verb2 or word == noun2 or word == adjective3 or noun == verb3 or word == adverb:
        print(colored(word, 'magenta'),end=" ")
      else:
        print(word,end=" ")
      
  
  #####################################
  #Nature is so (adj). It really brings me (adj) pleasure. I love the smell of (adj) air. Camping is a fun way to experience the beauties of nature. The sunset is so (adj) and I love (action). But, by far, the most fun thing of camping, is (verb ending in -ing) (noun) around the campfire.
  if mad_libs_num == 5:
    adjective_ex = ["awesome","delicious","scary","horrible","fat","sunny"]
    action_ex = ["drinking water","bringing a horse to water","eating ice cream on a sunny day","lying to my mom","crying into my pillow","playing Fortnite"]
    verb_ending_in_ing_ex =["running","dancing","thinking","lying","eating","taking"]
    noun_ex = ["brother","animal","purse","cat","racket","controller"]
    while True:
      ex = random.randrange(0,6)
      adjective = input("Enter an adjective:")
      print('\n' * 1)
      if adjective == "EXAMPLE" or adjective == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(adjective_ex[ex],'magenta'))
        continue
      else:
        break
    while True:
      ex = random.randrange(0,6)
      adjective2 = input("Enter another adjective:")
      print('\n' * 1)
      if adjective2 == "EXAMPLE" or adjective2 == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(adjective_ex[ex],'magenta'))
        continue
      else:
        break
    while True:
      ex = random.randrange(0,6)
      adjective3 = input("Enter another adjective:")
      print('\n' * 1)
      if adjective3 == "EXAMPLE" or adjective3 == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(adjective_ex[ex],'magenta'))
        continue
      else:
        break
    while True:
      ex = random.randrange(0,6)
      adjective4 = input("Enter another adjective:")
      print('\n' * 1)
      if adjective4 == "EXAMPLE" or adjective4 == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(adjective_ex[ex],'magenta'))
        continue
      else:
        break
    while True:
      ex = random.randrange(0,6)
      action = input("Enter an action:")
      print('\n' * 1)
      if action == "EXAMPLE" or action == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(action_ex[ex],'magenta'))
        continue
      else:
        break
    while True:
      ex = random.randrange(0,6)
      verb_ending_in_ing = input("Enter an verb ending in -ing:")
      print('\n' * 1)
      if verb_ending_in_ing == "EXAMPLE" or verb_ending_in_ing == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(verb_ending_in_ing_ex[ex],'magenta'))
        continue
      else:
        break
    while True:
      ex = random.randrange(0,6)
      noun = input("Enter a noun:")
      print('\n' * 1)
      if noun == "EXAMPLE" or noun == "\"EXAMPLE\"":
        print("Here's an example: ",end="")
        print(colored(noun_ex[ex],'magenta'))
        continue
      else:
        break
    madLibs[5][1] = adjective
    madLibs[5][3] = adjective2
    madLibs[5][5] = adjective3
    madLibs[5][7] = adjective4
    madLibs[5][9] = action
    madLibs[5][11] = verb_ending_in_ing
    madLibs[5][12] = noun
    for word in madLibs[5]:
      if word == adjective or word == adjective2 or word == adjective3 or word == adjective4 or word == action or word == verb_ending_in_ing or word == noun:
        print(colored(word, 'magenta'),end=" ")
      else:
        print(word,end=" ")
  
