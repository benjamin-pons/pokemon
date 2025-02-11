class Pokemon :
    def __init__(self, nom, hp, atk, defense, lvl = 5) :
        self.nom = nom
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.lvl = lvl
        self.sprite_front = f"./images/sprite/{self.nom}-face.png"
        self.sprite_back = f"./images/sprite/{self.nom}-back.png"
        self.alive = True
    
    def lower_hp(self, damage) :
        """Inflicts damage to the pokemon, if hp reaches 0 KO's the pokemon"""
        if damage >= self.hp :
            self.hp = 0
            self.alive = False
        else :
            self.hp -= damage
    
    def get_hp(self) :
        return self.hp

pokemon1 = Pokemon("absol", 50, 30, 20)
print(f"PV de Absol : {pokemon1.get_hp()}")
pokemon1.lower_hp(30)
print(f"PV de Absol : {pokemon1.get_hp()}")
pokemon1.lower_hp(30)
print(f"PV de Absol : {pokemon1.get_hp()}")