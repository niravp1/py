# dictionary info
info = {'name': 'John', 'gpa': 3.5, 'age': 20}

# loop to print all keys and values
print("Keys and Values using items() method:")
for key, value in info.items():
    print(key, ":", value)
# use the update() method to change the gpa to 4.0
info.update({'gpa': 4.0})

print("\nKeys and Values using keys() method:")
for key in info.keys():
    print(key, ":", info[key])

# adds  key major with the value 
info['major'] = 'Computer Science'
#   loop and the values() method to print all values
print("\nAll values using values() method:")
for value in info.values():
    print(value)
# two different ways to delete gpa and age in the dictionary
print(info['name'], "|", info['gpa'], "|", info['major'])

del info['gpa']
info.pop('age', None)

print("\nUpdated Dictionary:")
print(info)
