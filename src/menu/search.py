import colorama

from datetime import datetime
from utils.clear import clear

from data.avl import avl


def search_word():
    """Mencari arti kata dalam AVL Dictionary."""
    clear()
    start_time = datetime.now()
    search_word = avl.search(input("Input kata: "))
    end_time = datetime.now()

    delta = (end_time - start_time).total_seconds() * 1000

    if search_word:
        print(
            f'\n{colorama.Fore.BLUE}Arti kata {search_word.key} adalah "{search_word.value}"'
        )
    else:
        print(f"\n{colorama.Fore.RED}Kata tidak ditemukan!{colorama.Fore.RESET}")

    print(f"Kecepatan pencarian: {delta}ms{colorama.Fore.RESET}")
