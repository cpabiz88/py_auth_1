import utils


def user_login():
    user_name = input("login: ").strip()

    if len(user_name) < 3 or len(user_name) > 20:
        return utils.LENGTH_ERROR

    elif ":" in user_name:
        return utils.COLON_ERROR

    elif not utils.is_login_registered(user_name):
        return utils.USER_NOT_FOUND_ERROR

    else:
        with open("users.db", "r") as file:
            lines = file.readlines()
            file.close()

        for line in lines:
            if line.find(user_name + "::") != -1:
                reference_password = line.split("::")[1][:-1]
                entered_password = input("Password: ")

                if utils.md5(entered_password) == reference_password:
                    return True
                else:
                    return utils.PASSWORD_INCORRECT
