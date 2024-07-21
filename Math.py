import math

from unicodedata import name

pi = 3.14
x = 1
y = 2
z = 3
# Round = nearest int
print(round(pi))
# Ceil = round a number up to the nearest
print(math.ceil(pi))
# Floor = round a number down to the nearest
print(math.floor(pi))
# Absolute = give a positive number
print(math.fabs(pi))
# Pow = raise a base number to a power (pangkat)
print(math.pow(pi, 2))
# Square Root sqrt
print(math.sqrt(pi))
# Largest Number
print(max(x,y,z))
# Lowest Number
print(min(x,y,z))

# ==============================================================================

# Slicing = create substring by extracting elements from another string
#             indexing[] or slice()
#             [start:stop:step]
# start = 0, mulai huruf yang mau diambil
# stop, stop berhenti huruf + 1 karena sifatnya ekslusif
# step, pemutusan huruf
# reverse = -1

name = "Frida Sisilia"
first_name = name[:5]
last_name = name[6:]
nama_acak = name[0:13:2] #tiap lompat 2 dihapus
reversed_name = name[::-1]
print(first_name)
print(last_name)
print(nama_acak)
print(reversed_name)

website1 = "http://google.com"
website2 = "http://wilfridasisilia.com"
slice = slice(7, -4)
print(website1[slice])
print(website2[slice])

