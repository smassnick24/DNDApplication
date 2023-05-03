from PyPDF2 import PdfReader, PdfWriter

with open("Character-Sheet.pdf", "rb") as pdf:
    page_container = []

    reader = PdfReader(pdf)
    fields = reader.get_form_text_fields()

    # print(fields)

    for pages in reader.pages:
        page_container.append(pages.extract_text())

        # print(page_container)


def fill_form():
    char_name = input("What is your Character's Name?: ")
    race = input("What is your Character's Race?: ")
    alignment = input("What is your Character's Race?: ")
    initiative = input("Initiative: ")
    max_hp = input("Maximum HP: ")
    stats = [input("Strength: "), input("Dexterity: "), input("Constitution: "),
             input("Intelligence: "), input("Wisdom: "), input("Charisma: ")]
    stat_mods = []

    # calculating stat modifiers
    for i, stat in enumerate(stats):
        if not stat.isdigit():  # if stat as a string isn't a digit
            stats[i] = 10
            stat_mods.append(0)
        else:  # stat is a digit
            stat = int(stat)
            stats[i] = stat
            if stat == 10:
                stat_mods.append(0)
            elif stat > 10:
                storage = stat - 10
                modifier = storage // 2
                stat_mods.append(modifier)
            else:
                storage = 10 - stat
                modifier = (storage // 2) * -1
                stat_mods.append(modifier)
