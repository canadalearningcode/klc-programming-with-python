import random

listeAdjectifs = ["Joyeux", "Drôle", "Mini", "Super", "Musical", "Merveilleux"]

listeCouleurs = ["Jaune", "Rose", "Vert", "Bleu", "Orange"]

listeAnimaux = ["Éléphant", "Licorne", "Girafe", "Dinosaure", "Kangourou"]

adjectif = random.choice(listeAdjectifs)
couleur = random.choice(listeCouleurs)
animal = random.choice(listeAnimaux)
nombre = str(random.randint(1, 100))

nomUtilisateur = adjectif + couleur + animal + nombre

print("Voici un générateur de nom d’utilisateur aléatoire")
print("Ton nom d’utilisateur aléatoire est : " + nomUtilisateur)
