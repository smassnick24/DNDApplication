import requests


class CharacterSheet(object):
    def __init__(self):
        self.url = "https://media.wizards.com/2016/dnd/downloads/5E_CharacterSheet_Fillable.pdf"
        self.character_pdf = None

    def get(self, filename: str) -> None:
        """
        function that retreives the character sheet from the url
        then saves it in the current directory
        :return: None
        """
        request = requests.get(self.url, allow_redirects=True)
        with open(f'{filename}.pdf', 'wb') as file:
            file.write(request.content)
        self.character_pdf = filename + ".pdf"

    def write(self) -> None:
        """
        function that writes to the character sheet
        :return: None
        """
        pass

    def get_data(self) -> int or str or list:
        """
        function that retrieves data from the character sheet
        :return: int, str, list
        """
        pass
