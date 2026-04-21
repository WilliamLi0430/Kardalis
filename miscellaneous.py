#REMINDER ON THINGS TO ADD ("With this map, you now have access to shops, trades, adventures, quests, and more!")

import time

messages = [
    "There are three types of quests: Basic Quests, Chapter Quests, and Boss Quests."
    "Basic Quests can be done anywhere and at any time."
    "Chapter Quests can only be done in a certain chapter."
    "Boss Quests are difficult and long quests, but they reward a lot when completed."
    "Boss Quests can also be done anywhere and at any time."
]
for line in messages:
    time.sleep(2)
    print(line)
    break

messages = [
    "Hi! I'm {shopkeeper name}!"
    "After every battle you go in, my wares change!"
    "Prices on rarer items will be more expensive than others."
    "However, I can give you a discount every once in a while."
    "Here, would you like a free sample?"
    "{give free item}"
]