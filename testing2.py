from PyPDFForm import PyPDFForm
import os

PATH_TO_FILLABLE = "template/DnD_5E_CharacterSheet_FormFillable.pdf"

PATH_TO_OUTPUT = "character_sheets/Filled.pdf"

filled_fields = {
    "CharacterName": "Sam",
    "STR": "24",
    "Age": "25",
}

with open(PATH_TO_OUTPUT, 'wb') as output:
    output.write(PyPDFForm(PATH_TO_FILLABLE).fill(filled_fields).read())