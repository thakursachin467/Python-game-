from random import randint
game_running = True
game_results = []


def calc_monster_attack():
    return randint(monster["attack_min"],
                   monster["attack_max"])


def game_end(name):
    print(f'{name} won the game!')


while game_running:
    new_round = True
    counter = 0
    player = {
        "name": "sachin",
        "attack": 10,
        "heal": 15,
        "health": 100
    }
    monster = {
        "name": "dark lord",
        "attack_min": 10,
        "attack_max": 20,
        "health": 100
    }
    print("---"*8)
    print("Enter Player name")
    player["name"] = input()
    print("---"*8)
    print(player["name"] + ' has ' + str(player["health"]) + ' health ')
    print(monster["name"] + ' has ' + str(monster["health"]) + ' health ')
    print("---"*8)
    while new_round:
        counter += 1
        player_won = False
        monster_won = False
        print("---"*8)
        print("Please select an action")
        print("1) attack")
        print("2) heal")
        print("3) Show results")
        print("4) Exit game")
        print("---"*8)
        player_choice = input()

        if player_choice == "1":
            monster["health"] -= player["attack"]
            if monster["health"] <= 0:
                player_won = True
            else:
                monster_attack = calc_monster_attack()
                player["health"] -= monster_attack
                if player["health"] <= 0:
                    monster_won = True
        elif player_choice == "2":
            monster_attack = calc_monster_attack()
            player["health"] += player["heal"]
            player["health"] -= monster_attack
            if player["health"] <= 0:
                monster_won = True
        elif player_choice == "3":
            for count in game_results:
                print(count)
        elif player_choice == "4":
            game_running = False
            new_round = False
        else:
            print("wrong input")

        if player_won == False and monster_won == False:
            print("---"*8)
            print(player["name"] + ' has ' + str(player["health"]) + ' left ')
            print(monster["name"] + ' has ' +
                  str(monster["health"]) + ' left ')
            print("---"*8)
        elif player_won:
            game_end(player["name"])
            round_result = {
                "name": player["name"],
                "health": player["health"],
                "roundes": counter
            }
            game_results.append(round_result)
            new_round = False
        elif monster_won:
            game_end(monster["name"])
            round_result = {
                "name": monster["name"],
                "health": monster["health"],
                "roundes": counter
            }
            game_results.append(round_result)
            new_round = False
