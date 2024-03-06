
print("")
print("                                  ,'\\")
print("    _.----.        ____         ,'  _\   ___    ___     ____")
print("_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.")
print("\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |")
print(" \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |")
print("   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |")
print("    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |")
print("     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |")
print("      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |")
print("       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |")
print("        \_.-'       |__|    `-._ |              '-.|     '-.| |   |")
print("                                `'                            '-._|")
print("")
print("Pokemon Battle")
print("")

import json
import random

# read Pokemon file into dictionary
pokemons_file = open('pokemons.json') # opening JSON file
pokemons = json.load(pokemons_file) # returns JSON object as a dictionary
pokemons_file.close() # Closing file

#print(pokemons[0])
pokemon_comparison=pokemons.copy()
def sort_pokemon(pokemon_comparison):
    return int(pokemon_comparison["total"])
while True:
    print("1. Show pokemon by index")
    print("2. Top 10 strongest pokemons (by total)")
    print("3. Top 10 weakest pokemons (by total)")
    print("4. Battle of 2 pokemons")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        search=int(input("Enter pokemon number "))
        print(pokemons[search-1])
        # https://www.w3schools.com/python/python_dictionaries_access.asp
        pass
    elif choice == '2':
        pokemon_comparison.sort(key=sort_pokemon, reverse=True)
        print(pokemon_comparison[0:10])
        # https://www.w3schools.com/python/python_lists_sort.asp
        pass
    elif choice == '3':
        pokemon_comparison.sort(key=sort_pokemon)
        print(pokemon_comparison[:10])
        # https://www.w3schools.com/python/python_lists_sort.asp
        pass
    elif choice == '4':
        print("Pokemon battle!")
        player_pokemon=int(input("Choose your pokemon!(enter your pokemon number) "))-1
        print("You have chosen", pokemons[player_pokemon]['name'])
        pc_pokemon=random.randint(0,49)
        print("PC has chosen", pokemons[pc_pokemon]['name'])
        player_health=pokemons[player_pokemon]['health']
        pc_health=pokemons[pc_pokemon]['health']
        print("Pokemon battle started!")
        if (random.randint(1,2)==1):
            print("Player attacks first")
            turn="player"
        else:
            print("PC attacks first")
            turn="pc"
        while ():
            print("abc")
        # Battle
        # 
        # https://www.w3schools.com/python/ref_random_choice.asp - random choice
        # Computer choosing one random Pokemon from list
        # Player choosing by entering Pokemon index
        # Damage is calculated by: (attack of Pokemon 2) - (defense of Pokemon 1) + (random from 5 to 20), and vice-versa
        # Player reaching 0 health (total) - lost
        pass

    elif choice == '5':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 5")

    print("==========================")


