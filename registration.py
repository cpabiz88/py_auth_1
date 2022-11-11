import utils


def user_registration():
    reg_login = input("Registration login: ").strip()

    if len(reg_login) < 3 or len(reg_login) > 20:
        return utils.LENGTH_ERROR

    elif ":" in reg_login:
        return utils.COLON_ERROR

    elif utils.is_login_registered(reg_login):
        return utils.USER_EXISTS_ERROR

    else:
        reg_password = input("Registration password: ")

        if len(reg_password) < 4 or len(reg_password) > 32:
            utils.restart_menu(utils.PASSWORD_ERROR)
            return

        try:
            result = -1
            with open('users.db', 'a+', encoding="utf-8") as file:
                result = file.write(reg_login + "::" + utils.md5(reg_password) + "\n")
                file.close()
        except IOError:
            print("Error! Some IO error while writing file users.db! Readonly file?")
        finally:
            return True if result > 0 else False
