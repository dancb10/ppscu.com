symbols = '$¢£¥€¤'
tuple(ord(symbol) for symbol in symbols)

import array
array.array('I', (ord(symbol) for symbol in symbols))


colors = ['white', 'black', 'yellow']
sizes = ['S', 'M', 'L', 'XL']

for tshirt in ('%s %s' % (color,size) for color in colors for size in sizes):
    print(tshirt)
