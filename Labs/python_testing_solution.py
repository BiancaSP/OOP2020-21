# a solution for lab on testing
# author: B. Schoen-Phelan
# date: 04-12-2020

# imports
import unittest
from Labs.python_testing import TypesAndStrings

# testing class
class TestMyStrings(unittest.TestCase):

    # set up all necessary variables used during the test
    def setUp(self):
        self.ts = TypesAndStrings()
        self.value = ["HALLO", 123]

    def test_last(self):
        result = self.ts.last_char(self.value[0])
        self.assertEqual(result, self.value[0][-1])
        self.assertNotEqual(result, self.value[0][-2])

    @unittest.expectedFailure
    def test_last_expect_failure(self):
        result = self.ts.last_char(self.value[0])
        self.assertEqual(result, self.value[0][0])

    def test_replacing_a(self):
        result = self.ts.replace_all_a(self.value[0].lower())
        self.assertNotIn(result, 'a')

    # this one fails initially.
    # need to change the original code to make it pass.
    def test_lower(self):
        result = self.ts.all_lower(self.value[0])
        self.assertEqual(result, self.value[0].lower())

    def test_first_char_correct(self):
        result = self.ts.first_char(self.value[0])
        self.assertTrue(result, self.value[0][0])

    @unittest.expectedFailure
    def test_first_char_incorrect(self):
        result = self.ts.first_char(self.value[0])
        self.assertFalse(result, self.value[0][1])

    # test that an assertion is thrown
    def test_assertion_no_str(self):
        with self.assertRaises(TypeError):
            self.ts.first_char(self.value[1])


if __name__ == "__main__":
    unittest.main()