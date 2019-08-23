import random

adjectiveList = ["Happy", "Silly", "Tiny", "Super", "Musical", "Funny"]

colourList = ['Yellow', 'Pink', 'Green', 'Blue', 'Orange']

animalList = ['Elephant', 'Unicorn', 'Giraffe', 'Dinosaur', 'Kangaroo']

adjective = random.choice(adjectiveList)
colour = random.choice(colourList)
animal = random.choice(animalList)
number = str(random.randint(1, 100))

username = adjective + colour + animal + number

print("Welcome to Random Username Generator")
print("Your random username is: " + username)
