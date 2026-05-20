from player import Player

import globals

import random

def go_mining(player: Player, hours: int):

    print("Starting activity: mining")

    mining_level = player.get_mining_level()

    pool = globals.condense_item_pool_to_level(globals.game_items["rocks"], mining_level)
    rare_pool = globals.condense_item_pool_to_level(globals.game_items["gems"], mining_level)

    for i in range(0, hours):

        if random.randint(1, 10) == 10:
            player.add_item(random.choice(rare_pool))
        else:
            player.add_item(random.choice(pool))

        player.add_xp(1)

        if player.get_mining_level() != mining_level:
            mining_level = player.get_mining_level()
            pool = globals.condense_item_pool_to_level(globals.game_items["rocks"], mining_level)
            rare_pool = globals.condense_item_pool_to_level(globals.game_items["gems"], mining_level)