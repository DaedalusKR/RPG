from Entity import *
from UI import *
import json

def start_game(GameExists):

    if GameExists == 0:
        print("Starting a New Game....")
        new_game_window = New_Player_Window()


        setup_new_player()
    elif GameExists == 1:
        new_player = load_saved_player()

    #print("---- Battle Starting----")

    battle_success = start_fight(new_player)

def setup_new_player():
    new_player = Player()
    new_player.name = input("What is your character's name?:   ")
    new_player.class_id = selectPlayerClass()
    new_player.playerClassName, new_player.playerMaxHP, new_player.playerMaxMP = playerClass(new_player.class_id,
                                                                                             new_player.playerMaxHP,
                                                                                             new_player.playerMaxMP)
    new_player.playerAttackPackage = setAttackPackage(new_player.class_id)
    new_player.playerSaveData = {"pName": new_player.name, "pHp": new_player.playerMaxHP, "pMp": new_player.playerMaxMP,
                                 "pClassId": new_player.class_id, "pClass": new_player.playerClassName,
                                 "pPackage": new_player.playerAttackPackage }
    showInConsole(new_player)

    print("Save character: ", new_player.playerName, "? - Y/N")
    confirmSave = input()
    if confirmSave == "Y" or confirmSave == "y":
        savegame(new_player.playerSaveData)

def build_enemies(battle_enemies_array):
    battle_enemies_array=[]
    for i in range(4):
        i = (Enemy())
        battle_enemies_array.append(i)
    return battle_enemies_array

def start_fight(new_player):
    enemies_to_gen = 2
    loops = 0
    enemies_array = []
    print("\nYou're being attacked by: \n")

    for i in range(enemies_to_gen):
        i = Enemy()
        i.enemy_id = loops
        loops += 1
        enemies_array.append(i)
        print(str(loops) + ": ", i.enemy_type_name, " -- ", "HP:", i.enemy_hp)

        if loops == enemies_to_gen:
            print("")

    new_player.hp = new_player.playerMaxHP

    while enemies_alive(enemies_array):
        number_of_enemies = len(enemies_array)
        print("\nSelect a skill and the enemy to attack:")

        for i in range(len(new_player.playerAttackPackage)):
            print(str(int(i+1))+":" , new_player.playerAttackPackage[i])

        print("\nSelect Skill:")
        skill_to_use = int(input())-1
        print("\nSelect Enemy ")
        enemy_to_hit = int(input())-1

        enemies_array = hit_enemy(enemy_to_hit, enemies_array, new_player.playerAttackPackage[skill_to_use])
        print("Used", new_player.playerAttackPackage[skill_to_use], "against", enemies_array[enemy_to_hit].enemy_type_name)
        print(enemies_array[enemy_to_hit].enemy_type_name, "has", enemies_array[enemy_to_hit].enemy_hp, "left.")

def hit_enemy(enemy_to_hit, enemies_array, skill_to_use):
    enemies_array[enemy_to_hit].enemy_hp = enemies_array[enemy_to_hit].enemy_hp - damage_amount(skill_to_use)
    return enemies_array

def damage_amount(skill_to_use):

    damage_to_enemy = 0
    if skill_to_use == "Attack":
        damage_to_enemy = 20
    elif skill_to_use == "Fire":
        damage_to_enemy = 35
    elif skill_to_use == "Lightning":
        damage_to_enemy = 35
    elif skill_to_use == "Blizzard":
        damage_to_enemy = 35
    elif skill_to_use == "Water":
        damage_to_enemy = 35
    else:
        damage_to_enemy = 0

    return damage_to_enemy

def showInConsole(new_player):
    print("------------------------------------------")
    print("Stats:")
    print("------------------------------------------")
    print("Name:   ", new_player.name)
    print("Class   ", new_player.playerClassName)
    print("------------------------------------------")
    print("HP: ", new_player.playerMaxHP)
    print("MP: ", new_player.playerMaxMP)
    print("------------------------------------------")
    print("Available Skills:    ")

    for skill in new_player.playerAttackPackage:
        print("    ", skill)

def enemies_alive(enemies_array):

    number_of_alive_enemies = 0
    for i in enemies_array:
        if enemies_array[i.enemy_id].enemy_hp > 0:
            number_of_alive_enemies += 1

    if number_of_alive_enemies > 0:
        return True
    else:
        return False

def savegame(saveObject):
    with open("saveData.txt", "w") as outfile:
        json.dump(saveObject, outfile)
    outfile.close()
    print("File Data Saved")

def load_saved_player():

    with open("saveData.txt", "r") as infile:
        loaded_data = json.load(infile)
        print(loaded_data.keys())
        infile.close()

    new_player = Player()
    new_player.name = loaded_data["pName"]
    new_player.class_id = loaded_data["pClassId"]
    new_player.playerClassName = loaded_data["pClass"]
    new_player.playerMaxHP = loaded_data["pHp"]
    new_player.playerMaxMP = loaded_data["pMp"]
    new_player.playerAttackPackage = loaded_data["pPackage"]
    new_player.playerSaveData = {"pName": new_player.name, "pHp": new_player.playerMaxHP, "pMp": new_player.playerMaxMP, "pClassId": new_player.class_id, "pClass": new_player.playerClassName, "pPackage": new_player.playerAttackPackage}

    showInConsole(new_player)
    print("loaded from saved file")
    return new_player

def setAttackPackage(classId):
    skillsPackage = []
    if classId == 1:
        skillsPackage = ["Attack", "Block", "Dodge", "Items"]
    elif classId == 2:
        skillsPackage = ["Attack", "Fire", "Lightning", "Blizzard", "Water"]
    elif classId == 3:
        skillsPackage = ["Attack", "Cure", "Life", "Esuna"]

    return skillsPackage

def selectPlayerClass():
    print("Pick Your Your Class:\n"
          "1. Warrior\n"
          "2. Mage\n"
          "3. Healer\n")

    playerclassid = int(input())
    return int(playerclassid)

def playerClass(playerclassid, hp, mp):

    if playerclassid < 4:
        if playerclassid == 1:
            playerclass = "Warrior"
            hp = 250
            mp = 20
            print(hp)
            print(mp)
            print("----")
            print(playerclass)
            return playerclass, hp, mp

        elif playerclassid == 2:
            playerclass = "Mage"
            hp = 150
            mp = 75
            return playerclass, hp, mp

        elif playerclassid == 3:
            playerclass = "Healer"
            hp = 100
            mp = 100
            return playerclass, hp, mp
    else:
        print(playerclassid, " isn't an option, try again")
        selectPlayerClass()

#def create_new_player():


doesSaveExist = 0
start_game(doesSaveExist)


