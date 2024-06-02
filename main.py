from person import Person

# Python Delete Property

person = Person("John")
print(person.name)
print(person.__dict__)

del person.name
print(person.__dict__)
# print(person.name) # AttributeError: 'Person' object has no attribute '_name'
