import colorama
from datetime import datetime
from utils.clear import clear

from data.avl import avl


def insert_word():
    """Memasukkan kata dan arti ke dalam AVL Dictionary."""
    clear()
    new_word = [input("Input kata: "), input("Input arti: ")]

    start_time = datetime.now()
    avl.insert(*new_word)
    end_time = datetime.now()

    delta = (end_time - start_time).total_seconds() * 1000

    print(f"\n{colorama.Fore.RED}Berhasil diinput!{colorama.Fore.RESET}")

    print(f"Kecepatan insert: {delta}ms{colorama.Fore.RESET}")
