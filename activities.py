from player import Player

import random

def condense_item_pool_to_level(dict: dict[str, int], level: int) -> list:
    new_items = []
    for d in dict:
        if dict[d] <= level:
            new_items.append(d)
    return new_items


def go_mining(player: Player, hours: int):

    print("Starting activity: mining")
    
    # Dict to keep track of the level requirements for each item
    basic_items = {
        "stone": 1,
        "coal": 1,
        "copper": 5,
        "iron": 10,
    }

    gems = {
        "pebblegem": 1,
        "glowstone": 10,
        "ruby": 20,
        "moon quartz": 30,
        "sapphire": 40,
        "opal": 50,
        "topaz": 60,
        "void crystal": 70,
        "diamond": 80,
        "starheart": 90
    }

    mining_level = player.get_mining_level()

    pool = condense_item_pool_to_level(basic_items, mining_level)
    rare_pool = condense_item_pool_to_level(gems, mining_level)

    for i in range(0, hours):

        if random.randint(1, 10) == 10:
            player.add_item(random.choice(rare_pool))
        else:
            player.add_item(random.choice(pool))

        player.add_xp(1)

        if player.get_mining_level() != mining_level:
            mining_level = player.get_mining_level()
            pool = condense_item_pool_to_level(basic_items, mining_level)
            rare_pool = condense_item_pool_to_level(gems, mining_level)