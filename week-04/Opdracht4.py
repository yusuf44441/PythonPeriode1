# Opdracht - Weapon Selector
#
# Je gaat een programma maken waarin een speler een wapen kan kiezen.
# Ieder wapen heeft zijn eigen damage en een speciale eigenschap.
#
# Stap 1 - Variabelen
# Maak de volgende variabelen aan:
# - Een variabele voor de naam van de speler
# - Een variabele voor het gekozen wapen
# - Een variabele voor de damage van het wapen
#
# Geef de speler zelf een naam en kies alvast een wapen.
#
# LET OP:
# Gebruik voor alle variabelen de juiste Python naming conventions!
# Bijvoorbeeld: player_name in plaats van playerName.

player_name = "Yusuf"
selected_weapon = "sword"
player_damage = 20

# Stap 2 - Match Case
# Gebruik een match case om te controleren welk wapen de speler heeft.
#
# De speler kan kiezen uit de volgende wapens:
#
# Sword:
# - Doet 20 damage
# - Print "Je gebruikt een zwaard!"
#
# Bow:
# - Doet 15 damage
# - Print "Je gebruikt een boog!"
#
# Staff:
# - Doet 25 damage
# - Print "Je gebruikt een magische staf!"
#
# Axe:
# - Doet 30 damage
# - Print "Je gebruikt een bijl!"
#
# Zorg ervoor dat de damage variabele de juiste waarde krijgt.
#
# Als de speler een onbekend wapen heeft gekozen:
# - Zet de damage op 0
# - Print "Onbekend wapen!"
#
# TIP:
# Gebruik case _ voor een onbekende waarde.

match selected_weapon:
    case "Sword":
        player_damage = 20
        print("Je gebruikt een zwaard!")
    case "Bow":
        player_damage = 15
    case "bow":
        player_damage = 15    

# Stap 3 - Resultaat printen
# Print na de match case de volgende informatie:
#
# Speler: Steve
# Wapen: Sword
# Damage: 20
#
# Zorg ervoor dat de informatie uit je variabelen komt.

print("speler:", player_name)
print("wapen:", selected_weapon)
print("damage:", player_damage)

# Stap 4 - Comments
# Voeg minimaal 3 eigen comments toe aan je programma.
#
# Leg met deze comments uit:
# - Wat een bepaald stuk code doet
# - Waarom je een match case gebruikt
# - Wat er gebeurt als het wapen niet bestaat
#
# Schrijf duidelijke comments die iemand anders helpen
# om jouw code te begrijpen.

# Deze code bepaalt welk wapen de speler heeft gekozen en toont informatie erbij
# Een match case wordt gebruikt om vershillende wapens te controleren en de juiste damage te laten zien
# Als een wapen niet bestaat wordt er een bericht getoond dat het wapen onbekend is

# Stap 5 - Naming Conventions
# Controleer of je code voldoet aan de Python naming conventions.
#
# - Gebruik snake_case voor variabelen
# - Gebruik duidelijke Engelse namen
# - Begin variabelen met een kleine letter
# - Gebruik geen spaties in variabelenamen
#
# FOUT: playerDamage = 20
# GOED: player_damage = 20
#
# FOUT: x = "Sword"
# GOED: selected_weapon = "Sword"\



# BONUS 1
# Voeg zelf minimaal 2 nieuwe wapens toe aan je match case.
# Bedenk voor ieder wapen een eigen damage en beschrijving.

match selected_weapon:
    case "bow":
        player_damage = 15
    case "axe":
        player_damage = 30

# BONUS 2
# Maak een variabele enemy_health met de waarde 100.
# Laat de speler 3 keer aanvallen met zijn gekozen wapen.
#
# Gebruik hiervoor een for-loop.
#
# Print na iedere aanval hoeveel health de vijand nog heeft.
# Zorg ervoor dat de health niet onder de 0 komt.

enemy_health = 100
for attack in range(5):
    enemy_health -= player_damage
    if enemy_health < 0:
        enemy_health = 0

    print("De vijand heeft nog", enemy_health, "health over.")

# BONUS 3
# Gebruik een while-loop om de vijand aan te vallen
# totdat de vijand geen health meer heeft.
#
# Print daarna "Vijand verslagen!"

while enemy_health > 0:
    enemy_health -= player_damage

    if enemy_health < 0:
        enemy_health = 0

    print("De vijand heeft nog", enemy_health, "health over.")

print("Vijand verslagen!")

    