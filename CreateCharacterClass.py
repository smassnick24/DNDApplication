from PyPDFForm import PyPDFForm
import json


class CharacterCreator(object):
    def __init__(self):
        self.template = "template/DnD_5E_CharacterSheet_FormFillable.pdf"
        self.output = "character_sheets/Default.pdf"

