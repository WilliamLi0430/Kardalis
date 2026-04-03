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
