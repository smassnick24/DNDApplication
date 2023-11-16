import requests


class DatabaseLookup:
    def __init__(self):
        self.base_url = "https://www.dnd5eapi.co/api/"
        self.modes = {0: "spells", 1: "classes", 2: "subclasses", 3: "monsters"}

    def validate(self, string: str):
        temp = list(string)
        for i in range(len(temp)):
            if temp[i] == ' ':
                temp[i] = "-"
        return "".join(temp)

    def query(self, mode: int, user_query: str) -> dict:
        param = self.validate(user_query)
        query_mode = self.modes[mode]
        query_url = self.base_url + query_mode + "/" + param
        response = requests.get(query_url)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")



# reference functuons for class development
def get_spell_info(spell_name: str):
    # modify spell name to work with dnd5eapi formatting, ex) acid arrow = acid-arrow
    temp = list(spell_name)
    for i in range(len(temp)):
        if temp[i] == ' ':
            temp[i] = "-"
    spell = "".join(temp)

    base_url = "https://www.dnd5eapi.co/api/spells"  # set base url
    spell_url: str = f"{base_url}/{spell}"  # specific spell url
    response = requests.get(spell_url)  # make GET request

    if response.status_code == 200:  # checking for successful request
        return response.json()
    else:
        print(f"Error: {response.status_code}")


def get_class_info(class_name: str):
    base_url = "https://www.dnd5eapi.co/api/classes"


def get_subclass_info(subclass_name: str):
    base_url = "https://www.dnd5eapi.co/api/subclasses"


def get_monster_info(monster: str):
    base_url = "https://www.dnd5eapi.co/api/monsters"


def ti_input() -> str:
    spell = input("Enter spell name: ")
    return spell


if __name__ == "__main__":
    print(get_spell_info("fireball"))
