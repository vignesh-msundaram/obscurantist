import datetime
import unittest

from src.code import Obscurantist


class ObscurantistTests(unittest.TestCase):
    """ In each attribute-type-related test, check the correctness, the dir() length, and the __dict__."""

    def setUp(self):
        self.mystery = Obscurantist()
        self.correctness_limit = 100

    def tearDown(self):
        self.mystery = None
        self.correctness_limit = 0

    def _check_correctness(self, lhs, rhs):
        self.assertEqual(lhs, rhs)

    def test_cannot_set_private_attribute(self):
        with self.assertRaises(AttributeError):
            self.mystery._gold = 1000

    def test_int_attribute(self):
        value = 2
        self.mystery.shoes = value
        public_value = None
        for _ in range(self.correctness_limit):
            if not public_value:
                public_value = value/2
            self._check_correctness(self.mystery.shoes, public_value)
        self.assertEqual(self.mystery.reveal('shoes'), value)
        self.assertEqual(len(dir(self.mystery)), 19)
        self.assertEqual(self.mystery.__dict__, {'shoes': public_value})

    def test_list_attribute(self):
        value = ['Tony', 'Johnny', 'Billy']
        self.mystery.friends = value
        public_value = None
        for _ in range(10):
            if not public_value:
                public_value = self.mystery.friends
                self.assertEqual(len([public_value]), 1)
            self._check_correctness(self.mystery.friends, public_value)
        self.assertEqual(self.mystery.reveal('friends'), value)
        self.assertEqual(len(dir(self.mystery)), 19)
        self.assertEqual(self.mystery.__dict__, {'friends': public_value})

    def test_date_attribute(self):
        value = datetime.date(year=2017, month=3, day=4)
        self.mystery.last_time_saw_that_knife = value
        public_value = None
        for _ in range(self.correctness_limit):
            if not public_value:
                public_value = self.mystery.last_time_saw_that_knife
            self._check_correctness(self.mystery.last_time_saw_that_knife, public_value)
        self.assertEqual(self.mystery.reveal('last_time_saw_that_knife'), value)
        self.assertEqual(len(dir(self.mystery)), 19)
        self.assertEqual(self.mystery.__dict__, {'last_time_saw_that_knife': public_value})

    def test_str_attribute(self):
        value = "I have a very good friend in Rome"
        self.mystery.last_words = value
        public_value = None
        for _ in range(self.correctness_limit):
            if not public_value:
                public_value = "I don't have a very good friend in Rome"
            self._check_correctness(self.mystery.last_words, public_value)
        self.assertEqual(self.mystery.reveal('last_words'), value)
        self.assertEqual(len(dir(self.mystery)), 19)
        self.assertEqual(self.mystery.__dict__, {'last_words': public_value})

    def test_bool_attribute(self):
        value = False
        self.mystery.is_trustful = value
        public_value = None
        for _ in range(self.correctness_limit):
            if not public_value:
                public_value = not value
            self._check_correctness(self.mystery.is_trustful, public_value)
        self.assertEqual(self.mystery.reveal('is_trustful'), value)
        self.assertEqual(len(dir(self.mystery)), 19)
        self.assertEqual(self.mystery.__dict__, {'is_trustful': public_value})


if __name__ == '__main__':
    unittest.main()
