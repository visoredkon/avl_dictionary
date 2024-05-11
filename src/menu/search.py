import colorama
from time import time
from utils.clear import clear

from data.avl import avl


def search_word():
    """Mencari arti kata dalam AVL Dictionary."""
    clear()
    start = time()
    search_word = avl.search(input("Input kata: "))
    end = time()

    if search_word:
        print(
            f'\n{colorama.Fore.BLUE}Arti kata {search_word.key} adalah "{search_word.value}"'
        )
        print(f"Kecepatan pencarian: {end-start} {colorama.Fore.RESET}")
    else:
        print(f"\n{colorama.Fore.RED}Kata tidak ditemukan!{colorama.Fore.RESET}")
