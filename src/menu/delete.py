import colorama
from datetime import datetime
from utils.clear import clear

from data.avl import avl


def delete_word():
    """Menghapus kata dari AVL Dictionary."""
    clear()

    start_time = datetime.now()
    avl.delete(input("Input kata: "))
    end_time = datetime.now()

    delta = (end_time - start_time).total_seconds() * 1000

    print(f"\n{colorama.Fore.RED}Berhasil dihapus!{colorama.Fore.RESET}")

    print(f"Kecepatan delete: {delta}ms{colorama.Fore.RESET}")
