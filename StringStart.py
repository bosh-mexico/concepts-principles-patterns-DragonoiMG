from typing import List, Callable

def starts_with_character(target_char: str, case_sensitive: bool = True) -> Callable[[str], bool]:
    def predicate(text: str) -> bool:
        if not text:
            return False
        
        if case_sensitive:
            return text[0] == target_char
        else:
            return text[0].lower() == target_char.lower()
    
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
    print(filter_strings(list_of_names, starts_with_character('m', case_sensitive=False)))
