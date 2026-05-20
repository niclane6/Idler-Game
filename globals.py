game_items = {
    "rocks": {
        "stone": 1,
        "coal": 1,
        "copper": 5,
        "iron": 10,
    },

    "gems": {
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
}

def condense_item_pool_to_level(dict: dict[str, int], level: int) -> list:
    new_items = []
    for d in dict:
        if dict[d] <= level:
            new_items.append(d)
    return new_items
