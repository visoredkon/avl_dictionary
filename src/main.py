from utils.clear import clear

from menu.menu import display_menu
from menu.insert import insert_word
from menu.delete import delete_word
from menu.search import search_word

clear()

while True:
    display_menu()
    menu = input("Select menu : ")

    match menu:
        case "1":
            insert_word()
        case "2":
            delete_word()
        case "3":
            search_word()
        case "0":
            break
