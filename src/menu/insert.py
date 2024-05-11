import colorama
from utils.clear import clear

from data.avl import avl


def insert_word():
    """Memasukkan kata dan arti ke dalam AVL Dictionary."""
    clear()
    new_word = [input("Input kata: "), input("Input arti: ")]
    avl.insert(*new_word)
    print(f"\n{colorama.Fore.RED}Berhasil diinput!{colorama.Fore.RESET}")
