# dictionary = a changeable, unordered collection of unique key: value pairs
# fast because they use hashing, allow us to access a value quickly

capitals = {"USA":"Washington DC",
            "India":"New Delhi",
            "China":"Beijing",
            "Rusia":"Moscow"}

capitals.update({"Germany":"Berlin"})
capitals.pop('China')

# print(capitals['Rusia'])
# print(capitals['Germany'])
# Gunakan get lebih aman
print(capitals.get('USA'))
# hanya output key
print(capitals.keys())
# hanya output value
print(capitals.values())
# ouput semuanya
print(capitals.items())

for key,value in capitals.items():
    print(key,value)
capitals.clear()
