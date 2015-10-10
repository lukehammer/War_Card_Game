__author__ = 'luke'

import unittest

from cards import Card

class Card_Tests(unittest.TestCase):
    def setUp(self):
        self.king_of_clubs = Card("king","clubs")
        self.two_of_hearts = Card(2,"hearts")


    def test_value(self):
        self.assertEqual(self.two_of_hearts.rank, 2)

    def test_value2(self):
        self.assertEqual(self.king_of_clubs.rank, 13)

    def test_does_not_equal(self):
        self.assertNotEqual(self.king_of_clubs,self.two_of_hearts)

    def test_does_not_equal_values(self):
        self.assertNotEqual(self.king_of_clubs.rank,self.two_of_hearts.rank)



if __name__ == '__main__':
    unittest.main()