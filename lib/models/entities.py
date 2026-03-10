class Character:

    def __init__(self, name, atk, defense, pv, atout, ultime):
        self.name = name
        self.atk = atk
        self.defense = defense
        self.pv = pv
        self.atout = atout
        self.ultime = ultime
        self.tour = 0

    def is_alive(self):
        return self.pv > 0

    def attack(self, target):
        self.tour += 1
        damage = max(1, self.atk - target.defense)
        skill_used = None
    
        if self.tour % self.ultime["cooldown"] == 0:
            damage = self.apply_effect(self.ultime, damage, target)
            skill_used = self.ultime["name"]
        elif self.tour % self.atout["cooldown"] == 0:
            damage = self.apply_effect(self.atout, damage, target)
            skill_used = self.atout["name"]

        target.pv -= damage
        return damage, skill_used

    def apply_effect(self, skill, damage, target):
        effet = skill["effet"]
        valeur = skill["valeur"]

        if effet == "atk_boost":
            damage += valeur
        if effet == "def_boost":
            self.defense += valeur
        if effet == "heal":
            self.pv += valeur
        if effet == "double_hit":
            damage *= 2

        return damage

class Monster(Character):
    pass
    

