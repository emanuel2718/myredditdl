import unittest
import myredditdl.config_handler as config_handler


class TestConfigHandler(unittest.TestCase):
    def test_string(self):
        a = 1
        b = 2
        self.assertEqual(a+b, 3)


if __name__ == '__main__':
    unittest.main()
