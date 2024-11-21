import unittest

from Pokergame import generate_deck, Card, is_flush, is_straight, is_pair


class TestPokerMethods(unittest.TestCase):
    def setUp(self):
        # Wird vor jedem Test ausgeführt. Erzeugt ein Deck mit 52 Karten.
        self.deck = generate_deck()

    def test_generate_deck(self):
        # Testet, ob das generierte Deck genau 52 Karten enthält.
        self.assertEqual(len(self.deck), 52)

    def test_is_flush(self):
        # Erstellt eine Hand, bei der alle Karten die gleiche Farbe (suit) haben.
        hand = [
            Card(2, 'Hearts'),
            Card(3, 'Hearts'),
            Card(4, 'Hearts'),
            Card(5, 'Hearts'),
            Card(6, 'Hearts')
        ]
        # Überprüft, ob die Funktion is_flush() korrekt erkennt, dass es sich um einen Flush handelt.
        self.assertTrue(is_flush(hand))

    def test_is_straight(self):
        # Erstellt eine Hand mit fünf aufeinanderfolgenden Kartenwerten (rank).
        hand = [
            Card(2, 'Hearts'),
            Card(3, 'Diamonds'),
            Card(4, 'Clubs'),
            Card(5, 'Spades'),
            Card(6, 'Hearts')
        ]
        # Überprüft, ob die Funktion is_straight() korrekt erkennt, dass es sich um eine Straße handelt.
        self.assertTrue(is_straight(hand))

    def test_is_pair(self):
        # Erstellt eine Hand mit genau einem Paar (zwei Karten mit dem gleichen Wert).
        hand = [
            Card(2, 'Hearts'),
            Card(2, 'Diamonds'),
            Card(4, 'Clubs'),
            Card(5, 'Spades'),
            Card(6, 'Hearts')
        ]
        # Überprüft, ob die Funktion is_pair() korrekt erkennt, dass die Hand ein Paar enthält.
        self.assertTrue(is_pair(hand))


# Führt die Tests aus, wenn die Datei direkt ausgeführt wird.
if __name__ == "__main__":
    unittest.main()
