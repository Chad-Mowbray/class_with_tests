# LiteraryDevices


class LiteraryDevices:
    def __init__(self, text):
        self.text = text
        self.list_words = self.turn_text_into_list_words()

    def has_palindrome(self):  # returns Bool
        bool_lst = [self._test_word_is_palindrome(w) for w in self.list_words]
        return any(bool_lst)

    def turn_text_into_list_words(self):
        return self.text.split(" ")

    @staticmethod
    def _test_word_is_palindrome(word):  # returns Bool
        # palindrome logic
        if len(word) <= 1:
            return True
        elif word[0] == word[-1]:
            return LiteraryDevices._test_word_is_palindrome(word[1:-1])
        else:
            return False

    def same_first_and_last(self):  # returns Bool
        lst_words = self.list_words
        if lst_words[0] == lst_words[-1]:
            return True
        else:
            return False


txt = "I fell into a racecar"
ld = LiteraryDevices(txt)
