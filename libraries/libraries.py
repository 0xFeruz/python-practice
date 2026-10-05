# import random
# coin = random.choice(['heads', 'tails'])

# print(coin)
# --------------------------------------------------------
# import random
# number = random.randint(0, 5)
# print(number)
# --------------------------------------------------------

import random 
cards = ['ace', 'queen', 'king']
random.shuffle(cards)

for card in cards:
    print(card)