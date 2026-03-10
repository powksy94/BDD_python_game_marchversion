from .db_init import get_db
from ..data import CHARACTERS, MONSTERS

db = get_db()

characters = db["characters"]
battles = db["battles"]
players = db["players"]
monsters = db["monsters"]

def seed_db():
    characters.drop()
    battles.drop()
    players.drop()
    monsters.drop()
    characters.insert_many(CHARACTERS)
    monsters.insert_many(MONSTERS)
