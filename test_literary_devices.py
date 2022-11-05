import unittest
from devices import LiteraryDevices


class TestLiteraryDevices(unittest.TestCase):
    def test_initializes_correctly(self):
        ld = LiteraryDevices("hi")
        expected = "hi"
        actual = ld.text
        self.assertEqual(expected, actual)

    def test_palindrome_logic(self):
        actual = LiteraryDevices._test_word_is_palindrome("racecar")
        expected = True
        self.assertEqual(actual, expected)

    def test_has_palindrome_works_false(self):
        ld = LiteraryDevices("hi")
        actual = ld.has_palindrome()
        self.assertFalse(actual)
        self.assertIs(actual, False)

    def test_has_palindrome_works_true(self):
        ld = LiteraryDevices("racecar")
        actual = ld.has_palindrome()
        self.assertTrue(actual)

    def test_same_first_last(self):
        ld = LiteraryDevices("racecar is a racecar")
        actual = ld.same_first_and_last()
        self.assertTrue(actual)


if __name__ == "__main__":
    unittest.main()
