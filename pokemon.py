class Pokemon :
    def __init__(self, name, base_hp, atk, defense, lvl, type1, type2 = "Single") :
        self.name = name
        self.atk = atk
        self.defense = defense
        self.type1 = type1
        self.type2 = type2
        self.lvl = lvl
        self.max_hp = (2*base_hp*self.lvl)//100 + self.lvl + 10
        self.__hp = self.max_hp
        self.sprite_front = f"./assets/images/sprites/front/{self.name.lower()}_front.png"
        self.sprite_back = f"./assets/images/sprites/back/{self.name.lower()}_back.png"
        self.alive = True
    
    def lower_hp(self, damage) :
        """Inflicts damage to the pokemon, if hp reaches 0 KO's the pokemon"""
        if damage >= self.__hp :
            self.__hp = 0
            self.alive = False
        else :
            self.__hp -= damage
    
    def get_hp(self) :
        return self.__hp
    
    def get_type(self) :
        return (self.type1, self.type2)
    
    def get_atk(self) :
        return self.atk
    
    def get_def(self) :
        return self.defense

    def get_effectiveness(self, target) : 
        type_atk = self.get_type()[0]
        type1_def = target.get_type()[0]
        type2_def = target.get_type()[1]
        
        efficiency = type_matchups[type1_def][type_atk] * type_matchups[type2_def][type_atk]
        return efficiency
    
    def attack(self, target) :
        base = (2*self.lvl +2)*(self.atk/target.get_def() * 20)
        efficiency = self.get_effectiveness(target)
        damage = (base//50 + 2) * efficiency
        target.lower_hp(damage)
        print(f"{target.name} took {damage} damage")
    
    def print_hp(self) :
        print(f"{self.name} : {self.get_hp()} HP")
    
    def print_info(self) :
        print(f"{self.name} : LVL {self.lvl}")
        if self.type2 != "Single" :
            print(f"Types : {self.type1}, {self.type2}")
        else :
            print(f"Type : {self.type1}")
        print(f"ATK : {self.atk} \nDEF : {self.defense} \nHP : {self.__hp}")

    
# Source : https://github.com/AbnormalNormality/Pokemon-Type-Matchups/blob/main/original%20function.py
type_matchups = {
        "Normal": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 1,
                   "Fighting": 2, "Poison": 1, "Ground": 1, "Flying": 1, "Psychic": 1, "Bug": 1,
                   "Rock": 1, "Ghost": 0, "Dragon": 1, "Dark": 1, "Steel": 1, "Fairy": 1},

        "Fire": {"Normal": 1, "Fire": 0.5, "Water": 2, "Electric": 1, "Grass": 0.5, "Ice": 0.5,
                 "Fighting": 1, "Poison": 1, "Ground": 2, "Flying": 1, "Psychic": 1, "Bug": 0.5,
                 "Rock": 2, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 0.5, "Fairy": 0.5},

        "Water": {"Normal": 1, "Fire": 0.5, "Water": 0.5, "Electric": 2, "Grass": 2, "Ice": 0.5,
                  "Fighting": 1, "Poison": 1, "Ground": 2, "Flying": 1, "Psychic": 1, "Bug": 1,
                  "Rock": 2, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 0.5, "Fairy": 1},

        "Electric": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 0.5, "Grass": 1, "Ice": 1,
                     "Fighting": 1, "Poison": 1, "Ground": 2, "Flying": 0.5, "Psychic": 1, "Bug": 1,
                     "Rock": 1, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 0.5, "Fairy": 1},

        "Grass": {"Normal": 1, "Fire": 2, "Water": 0.5, "Electric": 0.5, "Grass": 0.5, "Ice": 2,
                  "Fighting": 1, "Poison": 2, "Ground": 0.5, "Flying": 2, "Psychic": 1, "Bug": 2,
                  "Rock": 1, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 1, "Fairy": 1},

        "Ice": {"Normal": 1, "Fire": 2, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 0.5,
                "Fighting": 2, "Poison": 1, "Ground": 1, "Flying": 1, "Psychic": 1, "Bug": 1,
                "Rock": 2, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 2, "Fairy": 1},

        "Fighting": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 1,
                     "Fighting": 1, "Poison": 1, "Ground": 1, "Flying": 2, "Psychic": 2, "Bug": 0.5,
                     "Rock": 0.5, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 1, "Fairy": 2},

        "Poison": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 1,
                   "Fighting": 0.5, "Poison": 0.5, "Ground": 2, "Flying": 1, "Psychic": 2, "Bug": 0.5,
                   "Rock": 1, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 1, "Fairy": 0.5},

        "Ground": {"Normal": 1, "Fire": 1, "Water": 2, "Electric": 0, "Grass": 2, "Ice": 2,
                   "Fighting": 1, "Poison": 0.5, "Ground": 1, "Flying": 1, "Psychic": 1, "Bug": 1,
                   "Rock": 0.5, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 1, "Fairy": 1},

        "Flying": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 2, "Grass": 0.5, "Ice": 2,
                   "Fighting": 0.5, "Poison": 1, "Ground": 0, "Flying": 1, "Psychic": 1, "Bug": 1,
                   "Rock": 2, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 1, "Fairy": 1},

        "Psychic": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 1,
                    "Fighting": 0.5, "Poison": 1, "Ground": 1, "Flying": 1, "Psychic": 0.5, "Bug": 2,
                    "Rock": 1, "Ghost": 2, "Dragon": 1, "Dark": 2, "Steel": 1, "Fairy": 1},

        "Bug": {"Normal": 1, "Fire": 2, "Water": 1, "Electric": 1, "Grass": 0.5, "Ice": 1,
                "Fighting": 0.5, "Poison": 1, "Ground": 0.5, "Flying": 2, "Psychic": 1, "Bug": 1,
                "Rock": 2, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 1, "Fairy": 1},

        "Rock": {"Normal": 0.5, "Fire": 0.5, "Water": 2, "Electric": 1, "Grass": 2, "Ice": 1,
                 "Fighting": 2, "Poison": 0.5, "Ground": 2, "Flying": 0.5, "Psychic": 1, "Bug": 1,
                 "Rock": 1, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 1, "Fairy": 1},

        "Ghost": {"Normal": 0, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 1,
                  "Fighting": 0, "Poison": 0.5, "Ground": 1, "Flying": 1, "Psychic": 1, "Bug": 0.5,
                  "Rock": 1, "Ghost": 2, "Dragon": 1, "Dark": 2, "Steel": 1, "Fairy": 1},

        "Dragon": {"Normal": 1, "Fire": 0.5, "Water": 0.5, "Electric": 0.5, "Grass": 0.5, "Ice": 2,
                   "Fighting": 1, "Poison": 1, "Ground": 1, "Flying": 1, "Psychic": 1, "Bug": 1,
                   "Rock": 1, "Ghost": 1, "Dragon": 2, "Dark": 1, "Steel": 1, "Fairy": 2},

        "Dark": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 1,
                 "Fighting": 2, "Poison": 1, "Ground": 1, "Flying": 1, "Psychic": 0, "Bug": 2,
                 "Rock": 1, "Ghost": 0.5, "Dragon": 1, "Dark": 0.5, "Steel": 1, "Fairy": 2},

        "Steel": {"Normal": 0.5, "Fire": 2, "Water": 1, "Electric": 1, "Grass": 0.5, "Ice": 0.5,
                  "Fighting": 2, "Poison": 0, "Ground": 2, "Flying": 0.5, "Psychic": 0.5, "Bug": 0.5,
                  "Rock": 0.5, "Ghost": 1, "Dragon": 0.5, "Dark": 1, "Steel": 0.5, "Fairy": 0.5},

        "Fairy": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 1,
                  "Fighting": 0.5, "Poison": 2, "Ground": 1, "Flying": 1, "Psychic": 1, "Bug": 0.5,
                  "Rock": 1, "Ghost": 1, "Dragon": 0, "Dark": 0.5, "Steel": 2, "Fairy": 1},

        "Single": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 1,
                  "Fighting": 1, "Poison": 1, "Ground": 1, "Flying": 1, "Psychic": 1, "Bug": 1,
                  "Rock": 1, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 1, "Fairy": 1}
    }