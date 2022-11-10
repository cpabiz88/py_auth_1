import utils


def user_registration():
    reg_login = input("Enter your login: ")

    if len(reg_login) < 3 or len(reg_login) > 20:
        utils.restart_menu(utils.LOGIN_ERROR)
        return

    if ":" in reg_login:
        utils.restart_menu(utils.COLON_ERROR)
        return

    if utils.is_login_registered(reg_login):
        utils.restart_menu(utils.REGISTERED_ERROR)
        return

    reg_password = input("Enter your password: ")

    if len(reg_password) < 4 or len(reg_password) > 32:
        utils.restart_menu(utils.PASSWORD_ERROR)
        return

    with open('users.db', 'a+', encoding="utf-8") as file:
        result = file.write(reg_login + "::" + utils.md5(reg_password) + "\n")
        file.close()
        if result > 0:
            utils.restart_menu(f"User {reg_login} register successful! Press Enter to continue...")
        else:
            utils.restart_menu(f"User {reg_login} register failed! Press Enter to continue...")
