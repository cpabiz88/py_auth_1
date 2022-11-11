import os
import registration as reg
import userlogin as login
import hashlib

COLON_ERROR = "The name must not contain a colon character! Press Enter to restart!"
LOGIN_ERROR = "Warning! The login must not be less than " \
              "3 characters and more than 20 characters! Press Enter to restart!"
PASSWORD_ERROR = "Warning! The password must not be less than 4 characters and more than" \
                 " 32 characters! Press Enter to restart!"
REGISTERED_ERROR = "Warning! This login is already registered! Try choose another one! Press Enter to restart!"


def md5(password):
    md = hashlib.md5()
    md.update(password.encode('utf-8'))
    return md.hexdigest()


def is_login_registered(reg_login):
    try:
        with open("users.db", "r", encoding="utf-8") as file:
            data = file.read()
    except FileNotFoundError:
        try:
            with open("users.db", "w+", encoding="utf-8") as file:
                file.close()
        except IOError:
            restart_menu("Unknown IO error")
        finally:
            return False
    else:
        file.close()
        if reg_login + "::" in data:
            return True


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def restart_menu(text):
    input(text)
    clear_console()
    print_menu()


def print_menu():
    clear_console()
    answer = input("Select an action:\n\n"
                   "r) Register\n"
                   "l) Login\n"
                   "e) Exit\n\n"
                   "Enter 'r', 'l' or 'e' to select menu item: ")

    if answer == "r":
        clear_console()
        reg.user_registration()
        return
    elif answer == "l":
        login.user_login()
        return
    elif answer == "e":
        return
    else:
        print_menu()
