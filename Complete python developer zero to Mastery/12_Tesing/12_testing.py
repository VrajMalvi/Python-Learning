# pylint , pyflakes, pep 8
# only for devs not to send to customers

import unittest
import main


class TestMain(unittest.TestCase):
    # we add it start of defination
    def setUp(self):      # one of the default method
        print('about to test function')  # runs before each function

    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'vh'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)
        # here valueError is class and result is instance and fun gives ans in bool so we use assertTrue method of many assert methods

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    def test_do_stuff4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

        # in all above main.do_stuff main is file name and after that is name of def in main file

    # one of the default method at the end
    def tearDown(self):
        print('cleaning up')  # this method run at the end of every function


if __name__ == '__main__':
    unittest.main()
# here main is the file from which all operation are running not the main file
# here  this file is work as main file

# type python -m unittest -v in bash for more detailed information
