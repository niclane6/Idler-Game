class Player:
    def __init__(self, name: str):
        self.name = name

        self.busy = False

        self.__inventory = {}

        self.__skill_mining = {"xp": 0, "level": 1}

    def get_mining_xp(self) -> int:
        return self.__skill_mining["xp"]
        
    def get_mining_level(self) -> int:
        return self.__skill_mining["level"]
    
    def add_xp(self, xp: int):
        total_xp = self.get_mining_xp() + xp
        self.__skill_mining["xp"] = total_xp

        base_xp_per_level = 10
        current_level = 1

        while total_xp > 0:
            xp_to_lose = base_xp_per_level + current_level
            if total_xp - xp_to_lose >= 0:
                current_level += 1
            total_xp -= xp_to_lose

        self.__skill_mining["level"] = current_level

    def add_item(self, item: str):
        if item in self.__inventory:
            self.__inventory[item] += 1
        else:
            self.__inventory[item] = 1

    def list_inventory(self):
        for item in self.__inventory:
            print(f"{item}: {self.__inventory[item]}")
