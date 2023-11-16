import requests


class DatabaseLookup:
    def __init__(self):
        self.base_url = "https://www.dnd5eapi.co/api/"
        self.modes = {0: "spells", 1: "classes", 2: "subclasses", 3: "monsters"}

    @staticmethod
    def _validate(string: str):
        temp = list(string)
        for i in range(len(temp)):
            if temp[i] == ' ':
                temp[i] = "-"
        return "".join(temp)

    def query(self, mode: int, user_query: str) -> dict:
        param = self._validate(user_query)
        query_mode = self.modes[mode]
        query_url = self.base_url + query_mode + "/" + param
        response = requests.get(query_url)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")




if __name__ == "__main__":
    test = DatabaseLookup()
    print(test.query(mode=0, user_query="fireball"))
