import unittest
import test_runner as tr
import xmlrunner


class TestAutomation(unittest.TestCase):

    def setUp(self):
        print("setup")

    def test1(self):
        tr.print_message("hello world 1")
        assert False

    def test2(self):
        tr.print_message("hello world 2")
        assert False

    def test3(self):
        tr.print_message("hello world 3")
        assert True


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))


