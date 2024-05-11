import colorama


def display_menu():
    """Menampilkan menu utama AVL Dictionary."""
    print(colorama.Fore.GREEN + "\n📖 AVL Dictionary 📖")
    print("")
    print("Insert\t [1]")
    print("Delete\t [2]")
    print(f"Search\t [3]{colorama.Fore.RESET}")
    print(f"{colorama.Fore.RED}Exit\t [0]{colorama.Fore.RESET}\n")
