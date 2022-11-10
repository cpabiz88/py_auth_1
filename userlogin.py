import utils


def user_login():
    utils.clear_console()
    user_name = input("Enter your login: ")

    if len(user_name) < 3 or len(user_name) > 20:
        utils.restart_menu(utils.LOGIN_ERROR)
        return

    if ":" in user_name:
        utils.restart_menu(utils.COLON_ERROR)
        return

    if not utils.is_login_registered(user_name):
        utils.restart_menu(f"Error! {user_name} user not found! Press Enter to restart!")
    else:
        with open("users.db", "r") as file:
            lines = file.readlines()
            file.close()
            for line in lines:
                if line.find(user_name + "::") != -1:
                    reference_password = line.split("::")[1][:-1]

            entered_password = input(f"Enter {user_name} password: ")
            if utils.md5(entered_password) == reference_password:
                utils.restart_menu("Login successful! Press Enter to restart!")
            else:
                utils.restart_menu("Wrong password!")
