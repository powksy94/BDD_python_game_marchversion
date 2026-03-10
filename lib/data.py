CHARACTERS = [
    {"name": "Guerrier",   "atk": 15, "def": 10, "pv": 100, "atout": {"name": "Bouclier", "effet": "def_boost", "valeur": 5, "cooldown": 2}, "ultime": {"name": "Rage", "effet": "atk_boost", "valeur": 10, "cooldown": 5}},
    {"name": "Mage",       "atk": 20, "def": 5,  "pv": 80, "atout": {"name": "Barrière magique", "effet": "def_boost", "valeur": 3, "cooldown": 2}, "ultime": {"name": "Météore", "effet": "atk_boost", "valeur": 15, "cooldown": 4}},
    {"name": "Archer",     "atk": 18, "def": 7,  "pv": 90, "atout": {"name": "Flèche rapide", "effet": "double_hit", "valeur": 0, "cooldown": 3}, "ultime": {"name": "Pluie de flèches", "effet": "atk_boost", "valeur": 12, "cooldown": 5}},
    {"name": "Voleur",     "atk": 22, "def": 8,  "pv": 85, "atout": {"name": "Esquive", "effet": "def_boost", "valeur": 4, "cooldown": 2}, "ultime": {"name": "Fatality", "effet": "atk_boost", "valeur": 14, "cooldown": 4}},
    {"name": "Paladin",    "atk": 14, "def": 12, "pv": 110, "atout": {"name": "Soin", "effet": "heal", "valeur": 20, "cooldown": 3}, "ultime": {"name": "Lumière divine", "effet": "heal", "valeur": 40, "cooldown": 5}},
    {"name": "Sorcier",    "atk": 25, "def": 3,  "pv": 70, "atout": {"name": "Drain", "effet": "heal", "valeur": 10, "cooldown": 2}, "ultime": {"name": "Apocalypse", "effet": "atk_boost", "valeur": 20, "cooldown": 5}},
    {"name": "Chevalier",  "atk": 17, "def": 15, "pv": 120, "atout": {"name": "Parade", "effet": "def_boost", "valeur": 6, "cooldown": 2}, "ultime": {"name": "Charge", "effet": "atk_boost", "valeur": 12, "cooldown": 4}},
    {"name": "Moine",      "atk": 19, "def": 9,  "pv": 95, "atout": {"name": "Méditation", "effet": "heal", "valeur": 15, "cooldown": 3}, "ultime": {"name": "Ki", "effet": "atk_boost", "valeur": 10, "cooldown": 4}},
    {"name": "Berserker",  "atk": 23, "def": 6,  "pv": 105, "atout": {"name": "Fureur", "effet": "atk_boost", "valeur": 5, "cooldown": 2}, "ultime": {"name": "Déchainement", "effet": "double_hit", "valeur": 0, "cooldown": 4}},
    {"name": "Chasseur",   "atk": 16, "def": 11, "pv": 100, "atout": {"name": "Piège", "effet": "def_boost", "valeur": 4, "cooldown": 2}, "ultime": {"name": "Tir précis", "effet": "atk_boost", "valeur": 11, "cooldown": 4}},
]

MONSTERS = [
    {"name": "Gobelin",    "atk": 10, "def": 5,  "pv": 50,  "atout": {"name": "Ruse", "effet": "atk_boost", "valeur": 3, "cooldown": 2}, "ultime": {"name": "Embuscade", "effet": "double_hit", "valeur": 0, "cooldown": 4}},
    {"name": "Orc",        "atk": 20, "def": 8,  "pv": 120, "atout": {"name": "Cri de guerre", "effet": "atk_boost", "valeur": 5, "cooldown": 3}, "ultime": {"name": "Écrasement", "effet": "atk_boost", "valeur": 12, "cooldown": 5}},
    {"name": "Dragon",     "atk": 35, "def": 20, "pv": 300, "atout": {"name": "Écailles", "effet": "def_boost", "valeur": 8, "cooldown": 2}, "ultime": {"name": "Souffle de feu", "effet": "atk_boost", "valeur": 20, "cooldown": 5}},
    {"name": "Zombie",     "atk": 12, "def": 6,  "pv": 70,  "atout": {"name": "Infection", "effet": "atk_boost", "valeur": 3, "cooldown": 2}, "ultime": {"name": "Horde", "effet": "double_hit", "valeur": 0, "cooldown": 4}},
    {"name": "Troll",      "atk": 25, "def": 15, "pv": 200, "atout": {"name": "Régénération", "effet": "heal", "valeur": 20, "cooldown": 3}, "ultime": {"name": "Massue", "effet": "atk_boost", "valeur": 15, "cooldown": 5}},
    {"name": "Spectre",    "atk": 18, "def": 10, "pv": 100, "atout": {"name": "Intangible", "effet": "def_boost", "valeur": 5, "cooldown": 2}, "ultime": {"name": "Possession", "effet": "atk_boost", "valeur": 10, "cooldown": 4}},
    {"name": "Golem",      "atk": 30, "def": 25, "pv": 250, "atout": {"name": "Blindage", "effet": "def_boost", "valeur": 10, "cooldown": 2}, "ultime": {"name": "Séisme", "effet": "atk_boost", "valeur": 18, "cooldown": 5}},
    {"name": "Vampire",    "atk": 22, "def": 12, "pv": 150, "atout": {"name": "Morsure", "effet": "heal", "valeur": 15, "cooldown": 2}, "ultime": {"name": "Sang noir", "effet": "atk_boost", "valeur": 14, "cooldown": 4}},
    {"name": "Loup-garou", "atk": 28, "def": 18, "pv": 180, "atout": {"name": "Hurlement", "effet": "atk_boost", "valeur": 5, "cooldown": 3}, "ultime": {"name": "Transformation", "effet": "atk_boost", "valeur": 16, "cooldown": 5}},
    {"name": "Squelette",  "atk": 15, "def": 7,  "pv": 90,  "atout": {"name": "Os dur", "effet": "def_boost", "valeur": 3, "cooldown": 2}, "ultime": {"name": "Armée des morts", "effet": "double_hit", "valeur": 0, "cooldown": 4}},
]