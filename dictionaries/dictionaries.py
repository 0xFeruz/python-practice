# things = {'apple': 'fruit',
#           'pear': 'fruit',
#           'carrot': 'vegetable'
# }

# for thing in things:
#     print(thing, things[thing], sep=' is a ')

#--------------------------------------------------

things = [
        {'name': 'apple', 'found in': 'kitchen', 'used for': 'eating'},
           {'name': 'knife', 'found in': 'kitchen', 'used for': 'cutting'},
           {'name': 'laptop', 'found in': 'office', 'used for': 'working'},
]

for thing in things:
    print(thing['name'], thing['found in'], thing['used for'], sep=' for ')