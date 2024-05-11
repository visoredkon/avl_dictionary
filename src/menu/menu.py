import colorama


def display_menu():
    """Menampilkan menu utama AVL Dictionary."""
    print(colorama.Fore.GREEN + "\n*\tAVL Dictionary\t*")
    print("")
    print("*\tInsert\t [1]\t*")
    print("*\tDelete\t [2]\t*")
    print("*\tSearch\t [3]\t*")
    print(
        "*\t"
        + colorama.Fore.RESET
        + colorama.Fore.LIGHTMAGENTA_EX
        + "Exit\t [0]"
        + colorama.Fore.RESET
        + colorama.Fore.BLUE
        + "\t*"
    )
    print("" + colorama.Fore.RESET)
