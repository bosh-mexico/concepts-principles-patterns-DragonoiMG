from typing import List, Callable

def check_character(target_char: str, position: int, case_sensitive: bool = True) -> Callable[[str], bool]:
    def predicate(text: str) -> bool:
        if not text:
            return False
        
        if case_sensitive:
            return text[position] == target_char
        else:
            return text[position].lower() == target_char.lower()
    
    return predicate

def filter_strings(source: list, predicate) -> list:
    if not source:
        return []

    filtered_items = []

    for item in source:
        if predicate(item):
            filtered_items.append(item)

    return filtered_items


if __name__ == "__main__":
    list_of_names = ["Bosch", "Mexico", "Mango", "Mark", "Blr", "Clean code"]
    print(filter_strings(list_of_names, check_character('m', position=0, case_sensitive=False)))
