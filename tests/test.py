import unittest


def is_login_registered(reg_login):
    try:
        with open("../users.db", "r", encoding="utf-8") as file:
            data = file.read()
    except FileNotFoundError:
        try:
            with open("../users.db", "w+", encoding="utf-8") as file:
                file.close()
        except IOError:
            restart_menu("Unknown IO error")
        finally:
            return False
    else:
        file.close()
        if reg_login + "::" in data:
            return True


class RegisterLoginTests(unittest.TestCase):
    def test_is_user_registered(self):
        answer = is_login_registered("john")
        self.assertEqual(answer, True)


if __name__ == '__main__':
    unittest.main()
