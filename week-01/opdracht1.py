# Oefening 1
# Print de volgende zin "Hello World"




# Oefening 2
# Verander de waarde van de onderstaande variabelen.
# Print deze daarna 1 voor 1 uit

naam = "Yusuf"
leeftijd = 17
woonstad = "Tiel"
Game = "RainbowSixSiege"
Uur = 1000
Cijfer = 8


# Oefening 3
# Gebruik nu bovenstaande variabelen om zinnen te bouwen
# Bijvoorbeeld print("Hallo mijn naam is ", naam) of print(f"Mijn naam is {naam}")

print(f"Mijn naam is {naam}" f" ik ben {leeftijd} jaar oud" f" En ik woon in {woonstad}.") 

# Oefening 4
# Maak variabelen aan voor je favoriete game, hoe veel uur je deze hebt gespeeld en welk cijfer je dit spel zou geven
# Print deze daarna in zinnen uit, bijvoorbeeld "Mijn favoriete game is Minecraft" "Ik heb deze game 150 uur gespeeld", "Ik geef deze game een 8.5"

print(f"Mijn favoriete game is {Game}" f"en ik heb {Uur} ervan gespeeld" f" ik geef de spel een {Cijfer} van een 10.")

# Oefening 5
# Maak twee variabelen aan, number1 en number2
# Bereken daarna de som (+), het verschil (-) en het product (*) uit van deze nummers.
# Print daarna de uitkomsten uit

number1 = 10 
number2 = 20 

print(f"{number1} + {number2} = 30 ")
print(f"{number2} - {number1} = 10")
print(f"{number1} * {number2} = 200 ")


# Oefening 6
# Maak een simpel game character met minimaal de volgende variabelen: name, health, level, damage
# Print deze vervolgens uit
# Zorg er daarna voor dat je character 20 damage neemt, print nu de nieuwe waarde van zijn health uit

gamename = "dirk"
health = 50
level = 10 
damage = 300

print(f"name: {gamename} level: {level} damage: {damage} ")

health = health - 20 
print (f"My health is now {health}")

# Oefening 7
# Ga verder met je character van de vorige oefening. Voeg nu een nieuw variabel "weapon" toe.
# Geef het wapen een naam, verhoog de damage van je character en verhoog het level met 1
# Print daarna de nieuwe waardes uit 

weapon = "Greatsword"
weaponDamage = 35
damage += weaponDamage
level += 1 
print(f"I equiped my {weapon}, and now my damage is {damage}  ")
print(f"I also leveled up my level is now {level}")

# Oefening 8
# Maak een programma dat een profiel van een gamer laat zien
# Maak minimaal de volgende variabelen: name, age, favouriteGame, hoursPlayed, level, score
# Print al deze informatie netjes uit
# Verhoog daarna de score van het profiel met 250 en print de nieuwe waarde
# Bonus! Voeg zelf 3 nieuwe variabelen toe

name = "Yusuf"
age = 17
favouritegame = "elden ring"
hoursplayed = 300
level = 200 
score = 5000 

score += 250

print(f"My new score is {score}")