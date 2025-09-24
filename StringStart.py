def check_names_start_char(names: list, start_char) -> list : 
    if not names:
        return []
    
    selected_strings = []
    
    for name in names:
        if name[0].lower() == start_char.lower():
            selected_strings.append(name)

    return selected_strings


if __name__ == "__main__":
    list_of_names = ["Bosch", "Mexico", "Mango", "Mark", "Blr", "Clean code"]
    print(check_names_start_char(list_of_names, "m"))
