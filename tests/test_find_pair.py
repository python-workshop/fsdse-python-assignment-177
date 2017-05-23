from unittest import TestCase


class TestFind_pair(TestCase):

    def test_find_pair(self):
        try:
            from build import find_pair
        except ImportError:
            self.assertFalse("no function found")

        self.assertRaises(TypeError, find_pair, None)
        self.assertRaises(ValueError, find_pair, -1)
        self.assertEqual(find_pair(0), [])
        self.assertEqual(find_pair(1), ['()'])
        self.assertEqual(find_pair(2), ['(())',
                                                '()()'])
        self.assertEqual(find_pair(3), ['((()))',
                                                '(()())',
                                                '(())()',
                                                '()(())',
                                                '()()()'])
