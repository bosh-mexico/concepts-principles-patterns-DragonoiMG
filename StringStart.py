from typing import Callable, Any

def character_matches_at_position(text: str, target_char: str, position: int, case_sensitive: bool = True) -> bool:
    """Check if character at position matches target character."""
    if not text or len(text) <= position:
        return False
    
    if case_sensitive:
        return text[position] == target_char
    else:
        return text[position].lower() == target_char.lower()


def filter_items(source: list, predicate: Callable[[Any], bool]) -> list:
    if not source:
        return []

    filtered_items = []

    for item in source:
        if predicate(item):
            filtered_items.append(item)

    return filtered_items


if __name__ == "__main__":
    list_of_names = ["Bosch", "Mexico", "Mango", "Mark", "Blr", "Clean code"]
    print(filter_items(list_of_names, lambda name: character_matches_at_position(name, 'M', 0, case_sensitive=True)))
