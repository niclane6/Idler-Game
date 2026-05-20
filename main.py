import player
import activities

def main():
    
    ##### TESTING #####

    print("Running main.py")

    test_player = player.Player("test")

    activities.go_mining(test_player, 10)

    test_player.save_to_file()

    test_player.list_inventory()

    print(test_player.get_mining_level())

if __name__ == "__main__":
    main()