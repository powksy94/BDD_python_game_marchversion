import random
from .models.entities import Character, Monster
from .models.db_collections import monsters, players
from .utils.utils import display_team, get_choices, display_available_characters

def create_team(display_characters):
    char_list = list(display_characters)
    team = []

    while len(team) < 3:
        display_team(team)
        print(f"=== Choisir un personnage ({len(team)}/3) ===")
        available = display_available_characters(char_list, team)
        choice = get_choices(len(available))
        char_data = available[choice - 1]

        player = Character(
            char_data["name"],
            char_data["atk"],
            char_data["def"],
            char_data["pv"],
            char_data["atout"],
            char_data["ultime"],
        )
        team.append(player)

    print("Equipe complète !")
    display_team(team)
    return team

def play(player_name, team):

    score = 0
    kills = {}
    for char in team:
        kills[char.name] = 0
    max_rounds = 10

    while any(char.is_alive() for char in team) and score < max_rounds:
        monster_data = random.choice(list(monsters.find()))
        enemy = Monster(
            monster_data['name'],
            monster_data["atk"],
            monster_data['def'],
            monster_data['pv'],
            monster_data['atout'],
            monster_data['ultime'],
        )

        current = None
        for char in team:
            if char.is_alive():
                current = char 
                break
        print (f"\nCombat : {current.name} VS {enemy.name}")

        while current.is_alive() and enemy.is_alive():
            dmg, skill = current.attack(enemy)
            print(f" {current.name} inflige {dmg} dégâts à {enemy.name}")
            if skill:
                print(f" + {current.name} utilise [{skill}] !")
            if not enemy.is_alive():
                score += 1
                kills[current.name] += 1
                print(f"{enemy.name} est vaincu ! (Score = {score})")

            dmg, skill = enemy.attack(current)
            print(f" {enemy.name} inflige {dmg} dégâts à {current.name}")
            if skill:
                print(f" + {enemy.name} utilise [{skill}] !")
            if not current.is_alive():
                print(f"{current.name} est tombé dans les ténèbres !")
                break

    print(f"\n Game Over ! {player_name}, ton score: {score} monstres vaincus !")
    for name, count in kills.items():
        print(f" - {name} - {count} monstres vaincus !")

    players.insert_one({"name": player_name, "score": score, "kills": kills})

def display_ranking():
    print("\n=== Classement ===")
    ranking = players.find().sort("score", -1)
    for i , player in enumerate(ranking, 1):
        print(f"{i}. {player['name']} - {player['score']} monstres vaincus")
        if "kills" in player:
            for char_name, count in player["kills"].items():
                print(f"        - {char_name} : {count} monstres vaincus")
