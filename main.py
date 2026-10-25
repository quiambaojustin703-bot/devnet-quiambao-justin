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

    print("WHO'S THAT POKEMON!? - main.py:17")
    print("")
    print(f"Height: {height} - main.py:19")
    print(f"Weight: {weight} - main.py:20")
    print(f"Abilities: {', '.join(abilities)} - main.py:21")
    print("")

    attempts = 3
    while attempts > 0:
        guess = input(f"Enter your guess ({attempts} left): ").strip()
        
        if guess.lower() == chosen_name.lower():
            print("You got it right! - main.py:29")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print("Wrong! Try again.\n - main.py:34")
            else:
                print(f"\nGame over! It was {chosen_name}. - main.py:36")
else:
    print("Failed to fetch. - main.py:38")