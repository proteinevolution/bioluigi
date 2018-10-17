import unittest
from unittest.mock import patch
from luigibio.parameter import FileParameter, FileExistence


class FileParameterTests(unittest.TestCase):

    def check_consistency(self, param: FileParameter, existence: FileExistence):
        self.assertIs(param.existence, existence)
        for e in FileExistence:
            if e is not existence:
                self.assertIsNot(param.existence, e)

    def get_file_param(self, existence: FileExistence):
        param = FileParameter(existence)
        self.check_consistency(param, existence)
        return param

    @staticmethod
    def parse(param: FileParameter):
        param.parse("foo")

    def parse_something_with_value_error(self, param: FileParameter):
        with self.assertRaises(ValueError):
            FileParameterTests.parse(param)

    #######################################################
    # Tests that will FileParameter let raise a Value Error
    #######################################################

    @patch('luigibio.parameter.isfile', return_value=True)
    @patch('luigibio.parameter.islink', return_value=True)
    def test_links_are_not_allowed_1(self, islink, isfile):
        self.parse_something_with_value_error(
            self.get_file_param(FileExistence.EXISTING))

    @patch('luigibio.parameter.isfile', return_value=True)
    @patch('luigibio.parameter.islink', return_value=True)
    def test_links_are_not_allowed_2(self, islink, isfile):
        self.parse_something_with_value_error(
            self.get_file_param(FileExistence.NON_EXISTING))

    @patch('luigibio.parameter.isfile', return_value=False)
    def test_file_must_exist(self, isfile):
        self.parse_something_with_value_error(
            self.get_file_param(FileExistence.EXISTING))

    @patch('luigibio.parameter.exists', return_value=True)
    def test_file_must_not_exist(self, exists):
        self.parse_something_with_value_error(
            self.get_file_param(FileExistence.NON_EXISTING))

    #######################################################
    # Tests that do not let raise a Value Error
    #######################################################

    @patch('luigibio.parameter.isfile', return_value=True)
    def test_file_exits(self, isfile):
        param = self.get_file_param(FileExistence.EXISTING)
        FileParameterTests.parse(param)

    @patch('luigibio.parameter.exists', return_value=False)
    def test_file_does_not_exist(self, exists):
        param = self.get_file_param(FileExistence.NON_EXISTING)
        FileParameterTests.parse(param)


if __name__ == '__main__':
    unittest.main()
