#idea 
#add lore and a story line it'll be great

#This happens before the game starts
import time
messages = [
    "Welcome to (GAME NAME)!",
    "This game is about you fighting monsters and slowly getting more powerful,",
    "finally being able to defeat the last boss.",
    "I would say similar stuff to those game ads you see online,",
    "but that's just way too cringe to put here.",
    "Anyways, enjoy this game!"
]
for line in messages:
    time.sleep(2)
    print(line)

#This happens after the player chooses a character
message = [
    "Alright, you have chosen class {class}.",
    "Now, let's test your skills by fighting a goblin!"
    ]
for line in message:
    time.sleep(2)
    print(line)
    break

#Started adding a tutorial to the first goblin battle
messages[
    "Congratulations!"
    "You have defeated your first goblin!"
    "After every battle, win or loss, you can earn items and complete quests."
    "This way, you can grow more powerful and take on stronger enemies."
]
for line in message:
    time.sleep(2)
    print(line)
    break

#this happens when the tutorial battle ends
messages = [
    "Every time you finish a battle, you can do many things!"
    "But to do those things, you first need a map."
    "Here. This is the Map of Kardalis, the continent you are on right now."
    "With this map, you now have access to shops, trades, adventures, quests, and more!"
]
for line in messages:
    time.sleep(2)
    print(line)
    break

#this happens when character reaches level 5, 10, or something
messages = [
    "Congratulations! You have reached level (number)!"
    "To allow some quick progression, we will give you an item!"
    "There are two types of items: Usables, and Equippables."
    "Usables are items that go into your inventory and can be used at any time."
    "Equippables give you a boost in stats, but only a certain amount of Equippables can be equipped at one time."
    "Have fun!"
]
for line in messages:
    time.sleep(2)
    print(line)
    break

#REMINDER ON THINGS TO ADD ("With this map, you now have access to shops, trades, adventures, quests, and more!")