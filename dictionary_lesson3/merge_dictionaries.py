dict1 = {'username': 'x', 'email': 'x@y.com', 'location': 'mumbai'}
dict2 = {'firstname': 'nick', 'lastname': 'prince'}

dict3 = {'username': 'x', 'email': 'x@y.com', 'location': 'mumbai'}
dict4 = {'firstname': 'nick', 'lastname': 'prince'}

# using update() method
dict1.update(dict2)
print(dict1)

# using ** method (Aprpriate method of merging)
# Assign a new dictionary and put the values of other dictionaries
dict = {**dict3, **dict4}

print(dict)
