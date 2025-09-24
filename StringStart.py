from typing import Callable, Any

def is_number_prime(number: int):
    """Iterate (0, number) to see if number can be divided exactly by any number in the range"""
    if number < 2:
        return False
    
    for num in range(2, number):
        if number % num == 0:
            return False
    
    return True

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

    list_of_numbers = [1, 2, 3, 5, 7, 8, 11, 21, 29, 31, 35, 46, 47, 50]
    # First 100 prime numbers:
    # 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
    print(filter_items(list_of_numbers, lambda number: is_number_prime(number)))