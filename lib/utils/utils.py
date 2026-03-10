def display_menu():
    print("=== Medieval Game ===")
    print("1. Jouer")
    print("2. Afficher le classement")
    print("3. Quitter")

def get_choices(max_options):
    while True:
        choice = input("Ton choix: ")
        # si le choix est compris entre 1 est l'option max
        if choice.isdigit() and 1 <= int(choice) <= max_options:
            return int(choice)
        print(f"Choix invalide ! Veuillez entrer un nombre entre 1 et {max_options}.")

def display_characters(characters_list):
    for i, char in enumerate(characters_list, 1):
        print(f"{i}. {char['name']} (ATK:{char['atk']} DEF:{char['def']} PV:{char['pv']})")

def display_team(team):
    if len(team) == 0:
        print("Equipe vide.")
    else:
        print("\n=== Ton équipe ===")
        for i, char in enumerate(team, 1):
            print(f"{i}. {char.name} (ATK:{char.atk} DEF:{char.defense} PV:{char.pv})")
   

def display_available_characters(char_list, team):
    team_names = [char.name for char in team]
    available = []
    for char in char_list:
        if char["name"] not in team_names:
            available.append(char)

        
    for i, char in enumerate(available, 1):
        print(f"{i}. {char['name']} (ATK:{char['atk']} DEF:{char['def']} PV:{char['pv']})")
    
    return available



