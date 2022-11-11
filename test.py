import unittest
import utils
import registration as reg
import userlogin as log


class RegisterLoginTests(unittest.TestCase):
    def test_is_user_registered(self):
        utils.clear_console()
        print("Test 1. 'is_user_registered'. Enter registered name (which in database!)\n")
        name = input("Enter registered name: ")
        answer = utils.is_login_registered(name)
        self.assertEqual(answer, True)

    def test_user_login(self):
        print("Test 2. 'user_login'. Enter registered name (which in database!)")
        answer = log.user_login()
        self.assertEqual(answer, True)

    def test_user_registration(self):
        print("Test 3. 'user_registration'. Enter name to register (which not in database!)")
        answer = reg.user_registration()
        self.assertEqual(answer, True)


if __name__ == '__main__':
    unittest.main()
