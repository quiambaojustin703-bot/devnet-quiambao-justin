import random
import requests

pokemon_list = ["ditto", "pikachu", "charizard", "bulbasaur", "squirtle"]
chosen_name = random.choice(pokemon_list)

url = f"https://pokeapi.co/api/v2/pokemon/{chosen_name}"
response = requests.get(url)

if response.status_code == 200:
    pokemon = response.json()
    
    height = pokemon.get("height")
    weight = pokemon.get("weight")
    abilities = [item["ability"]["name"] for item in pokemon.get("abilities", [])]

    print("WHO'S THAT POKEMON!?")
    print("")
    print(f"Height: {height}")
    print(f"Weight: {weight}")
    print(f"Abilities: {', '.join(abilities)}")
    print("")

    attempts = 3
    while attempts > 0:
        guess = input(f"Enter your guess ({attempts} left): ").strip()
        
        if guess.lower() == chosen_name.lower():
            print("You got it right!")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print("Wrong! Try again.\n")
            else:
                print(f"\nGame over! It was {chosen_name}.")
else:
    print("Failed to fetch.")
