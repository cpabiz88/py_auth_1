import unittest
import utils
import registration


class RegisterLoginTests(unittest.TestCase):
    def test_is_user_registered(self):
        answer = utils.is_login_registered("john")
        self.assertEqual(answer, True)

    def test_user_registration(self):
        answer = registration.user_registration()
        self.assertEqual(answer, True)


if __name__ == '__main__':
    unittest.main()
