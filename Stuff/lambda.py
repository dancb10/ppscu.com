symbols = '$¢£¥€¤'
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))

