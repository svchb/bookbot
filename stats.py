from collections import Counter
from typing import Dict

def count_words(text):
    return len(text.split(" "))

def char_counts(text: str) -> Dict[str, int]:
    """Return a dictionary mapping each character in *text* (converted to lowercase)
    to the number of times it appears.
    Symbols, punctuation, spaces, and newlines are all included.
    """
    # Convert text to lowercase once to avoid duplicate keys
    lowered = text.lower()
    return dict(Counter(lowered))

def char_dics(char_counts: Dict[str, int]) -> Dict[str, int]:
    char_list = []
    for key in char_counts.keys():
        char_list += [{"char": key, "num": char_counts[key]}]

    return char_list
