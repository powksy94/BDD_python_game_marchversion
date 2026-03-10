from .models.db_collections import characters, seed_db
from .utils.utils import display_menu, get_choices, get_valid_name
from .game import create_team, play, display_ranking

seed_db()

while True:
    display_menu()
    choice = get_choices(3)
    if choice == 1:
        get_valid_name()
        team = create_team(characters.find())
        play(player_name, team)
    elif choice == 2:
        display_ranking()
    elif choice == 3:
        print("Au revoir !")
        break
