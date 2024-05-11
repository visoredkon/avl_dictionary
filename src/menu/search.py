import colorama

# from time import time
from datetime import datetime
from utils.clear import clear

from data.avl import avl


def search_word():
    """Mencari arti kata dalam AVL Dictionary."""
    clear()
    start_time = datetime.now()
    search_word = avl.search(input("Input kata: "))
    end_time = datetime.now()

    if search_word:
        print(
            f'\n{colorama.Fore.BLUE}Arti kata {search_word.key} adalah "{search_word.value}"'
        )
        print(
            f"Kecepatan pencarian: {(end_time - start_time).total_seconds() * 1000}ms{colorama.Fore.RESET}"
        )
    else:
        print(f"\n{colorama.Fore.RED}Kata tidak ditemukan!{colorama.Fore.RESET}")
