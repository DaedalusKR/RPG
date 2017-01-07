class Entity():
    def __init__(self):
        self.hp = 0
        self.mp = 0

class Player(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.playerName = ""
        self.playerMaxHP = 0
        self.playerHP = 0
        self.playerMaxMP = 0
        self.playerMP = 0
        self.playerClassID = 0
        self.playerClassName = ""
        self.playerAttackPackage = ""
        self.playerSaveData = {}

class Enemy(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.enemy_hp = 250
        self.enemy_mp = 50
        self.enemy_class_id = 1
        self.enemy_type_name = "Soldier"
        self.enemy_id = 0



