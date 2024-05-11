import colorama
from utils.clear import clear

from data.avl import avl


def delete_word():
    """Menghapus kata dari AVL Dictionary."""
    clear()
    avl.delete(input("Input kata: "))
    print(f"\n{colorama.Fore.RED}Berhasil dihapus!{colorama.Fore.RESET}")
