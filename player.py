import json
import os

class Player:
    SAVE_DIR = "saves"

    def __init__(self, name: str):
        self.name = name
        self.busy = False
        self.__inventory = {}
        self.__skill_mining = {"xp": 0, "level": 1}

        self._load_from_file()

    def _get_save_path(self) -> str:
        os.makedirs(self.SAVE_DIR, exist_ok=True)
        return os.path.join(self.SAVE_DIR, f"{self.name}.json")
    
    def _load_from_file(self):
        save_path = self._get_save_path()
        if os.path.exists(save_path):
            with open(save_path, "r") as f:
                data = json.load(f)
                self.__inventory = data["inventory"]
                self.__skill_mining = data["skill_mining"]

    def save_to_file(self):
        save_path = self._get_save_path()
        data = {
            "inventory": self.__inventory,
            "skill_mining": self.__skill_mining
        }
        with open(save_path, "w") as f:
            json.dump(data, f, indent=2)

    def get_mining_xp(self) -> int:
        return self.__skill_mining["xp"]
        
    def get_mining_level(self) -> int:
        return self.__skill_mining["level"]
    
    @staticmethod
    def _xp_to_level(xp: int) -> int:
        base_xp_per_level = 10
        current_level = 1

        while xp > 0:
            xp_to_lose = base_xp_per_level + current_level
            if xp - xp_to_lose >= 0:
                current_level += 1
            xp -= xp_to_lose

        return current_level
    
    def add_xp_mining(self, xp: int):
        total_xp = self.get_mining_xp() + xp
        self.__skill_mining["xp"] = total_xp
        


        self.__skill_mining["level"] = self._xp_to_level(total_xp)

    def add_item(self, item: str):
        if item in self.__inventory:
            self.__inventory[item] += 1
        else:
            self.__inventory[item] = 1

    def list_inventory(self):
        for item in self.__inventory:
            print(f"{item}: {self.__inventory[item]}")
