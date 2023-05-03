from PyPDF2 import PdfReader, PdfWriter


def fill_form():
    char_name = input("What is your Character's Name?: ")
    race = input("What is your Character's Race?: ")
    alignment = input("What is your Character's Alignment?: ")
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
                stat_mods.append("+" + str(modifier))
            else:
                storage = 10 - stat
                modifier = (storage // 2) * -1
                stat_mods.append("-" + str(modifier))

    filled_fields = {
        "CharacterName": char_name,
        "Race ": race,
        "Alignment": alignment,
        "Initiative": int(initiative),
        "HPMax": int(max_hp),
        "STR": stats[0],
        "STRmod": stat_mods[0],
        "DEX": stats[1],
        "DEXmod ": stat_mods[1],
        "CON": stats[2],
        "CONmod": stat_mods[2],
        "INT": stats[3],
        "INTmod": stat_mods[3],
        "WIS": stats[4],
        "WISmod": stat_mods[4],
        "CHA": stats[5],
        "CHamod": stat_mods[5]
    }

    with open("Character-Sheet.pdf", "rb") as pdf:
        page_container = []

        reader = PdfReader(pdf)
        writer = PdfWriter()
        fields = reader.get_fields()

        page_one = reader.pages[0]
        writer.add_page(page_one)

        # print(fields)

        for pages in reader.pages:
            page_container.append(pages.extract_text())

    fields.update(filled_fields)
    writer.update_page_form_field_values(writer.pages[0], fields)

    with open("Character-Sheet.pdf", "wb") as output:
        writer.write(output)


fill_form()
