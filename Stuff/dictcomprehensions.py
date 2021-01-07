from pprint import pprint
DIAL_CODES = [
         (86, 'China'),
         (91, 'India'),
         (1, 'United States'),
         (62, 'Indonesia'),
         (55, 'Brazil'),
         (92, 'Pakistan'),
         (880, 'Bangladesh'),
         (234, 'Nigeria'),
         (7, 'Russia'),
         (81, 'Japan'),
     ]

dictionary = { country: code for code,country in DIAL_CODES  }
pprint(dictionary)

dictionary2 = { code: country.capitalize() for code, country in DIAL_CODES if code > 60 }
pprint(dictionary2)

dictionary2.__contains__(55)

d1 = dictionary2.copy()

d4=list(zip(d1.keys(),d1.values()))
d5=dict(zip(d1.keys(),d1.values()))

print(d4, ' ', d5)
