# import random
# coin = random.choice(['heads', 'tails'])

# print(coin)
# --------------------------------------------------------
# import random
# number = random.randint(0, 5)
# print(number)
# --------------------------------------------------------

# import random 
# cards = ['ace', 'queen', 'king']
# random.shuffle(cards)

# for card in cards:
#     print(card)

#---------------------------------------------------------

# import statistics
# values = [1, 3, 5, 2, 7, 8, 12]
# print(statistics.mean(values))

#----------------------------------------------------------

# import sys

# if len(sys.argv) < 2:
#     sys.exit('too few arguments')

# for arg in sys.argv[1:]:
#     print('hello, my name is', arg)
# ------------------------------------------------------------------

# import cowsay
# import sys

# if len(sys.argv) == 2:
#     cowsay.cow('hello, ' + sys.argv[1])
#------------------------------------------------------------------
import sys

def main():
    if len(sys.argv) == 2:
        hello(sys.argv [1])
        goodbye(sys.argv [1])


def hello(name):
    print(f"hello, {name}")
    
def goodbye(name):
    print(f"goodbye, {name}")    

main()