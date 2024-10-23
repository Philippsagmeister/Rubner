import random
from collections import Counter

# Definiere eine Karte als ein Objekt mit Zahlenwert (rank) und Farbe (suit)
class Card:
    def __init__(self, rank, suit):
        # Rank steht für den Zahlenwert der Karte (2, 3, ..., 14, wobei 14 = Ace)
        self.rank = rank
        # Suit steht für die Kartenfarbe (z.B. Hearts, Diamonds, Clubs, Spades)
        self.suit = suit

    # Definiere, wie eine Karte als String dargestellt werden soll, z.B. '10 of Hearts'
    def __repr__(self):
        return f"{self.rank} of {self.suit}"

# Funktion, um die Farben der Handkarten als Liste zurückzugeben
def get_suits(hand):
    # Erstelle eine Liste, die die Farben (suits) der Karten in der Hand enthält
    return [card.suit for card in hand]

# Funktion, um die Zahlenwerte der Handkarten als Liste zurückzugeben
def get_ranks(hand):
    # Erstelle eine Liste, die die Zahlenwerte (ranks) der Karten in der Hand enthält
    return [card.rank for card in hand]

# Prüft, ob eine Hand einen Royal Flush hat (höchste Pokerhand)
def is_royal_flush(hand):
    # Ein Royal Flush ist ein Straight Flush mit einem Ass (14)
    return is_straight_flush(hand) and 14 in get_ranks(hand)

# Prüft, ob eine Hand einen Straight Flush hat (Straße und Flush kombiniert)
def is_straight_flush(hand):
    # Ein Straight Flush ist gegeben, wenn die Hand sowohl ein Flush als auch eine Straße ist
    return is_flush(hand) and is_straight(hand)

# Prüft, ob eine Hand Four of a Kind (vier gleiche Kartenwerte) hat
def is_four_of_a_kind(hand):
    # Zähle die Häufigkeit der einzelnen Kartenwerte in der Hand
    rank_counts = Counter(get_ranks(hand))
    # Prüfe, ob einer der Kartenwerte genau viermal vorkommt
    return 4 in rank_counts.values()

# Prüft, ob eine Hand ein Full House (drei gleiche und zwei gleiche Kartenwerte) hat
def is_full_house(hand):
    # Zähle die Häufigkeit der einzelnen Kartenwerte in der Hand
    rank_counts = Counter(get_ranks(hand))
    # Prüfe, ob die Karten ein Full House bilden, indem du auf genau einen Drilling und ein Paar prüfst
    return set(rank_counts.values()) == {3, 2}

# Prüft, ob eine Hand einen Flush (alle Karten haben dieselbe Farbe) hat
def is_flush(hand):
    # Prüfe, ob alle Karten dieselbe Farbe (suit) haben
    suits = get_suits(hand)
    return len(set(suits)) == 1  # Set entfernt Duplikate, daher sollte die Länge 1 sein

# Prüft, ob eine Hand eine Straße (fünf aufeinanderfolgende Kartenwerte) hat
def is_straight(hand):
    # Hole die Kartenwerte und sortiere sie
    ranks = get_ranks(hand)
    rank_values = sorted(ranks)
    # Prüfe, ob die Werte eine aufeinanderfolgende Sequenz von fünf Zahlen bilden
    return rank_values == list(range(min(rank_values), min(rank_values) + 5))

# Prüft, ob eine Hand Three of a Kind (drei gleiche Kartenwerte) hat
def is_three_of_a_kind(hand):
    # Zähle die Häufigkeit der Kartenwerte
    rank_counts = Counter(get_ranks(hand))
    # Prüfe, ob einer der Werte dreimal vorkommt
    return 3 in rank_counts.values()

# Prüft, ob eine Hand Two Pair (zwei verschiedene Paare) hat
def is_two_pair(hand):
    # Zähle die Häufigkeit der Kartenwerte
    rank_counts = Counter(get_ranks(hand))
    # Prüfe, ob genau zwei Kartenwerte jeweils zweimal vorkommen
    return len([count for count in rank_counts.values() if count == 2]) == 2

# Prüft, ob eine Hand ein Pair (zwei gleiche Kartenwerte) hat
def is_pair(hand):
    # Zähle die Häufigkeit der Kartenwerte
    rank_counts = Counter(get_ranks(hand))
    # Prüfe, ob einer der Werte zweimal vorkommt
    return 2 in rank_counts.values()

# Funktion, die prüft, ob die Hand keine spezielle Kombination hat (High Card)
def is_high_card(hand):
    # Diese Funktion gibt immer True zurück, wenn keine andere Kombination gefunden wurde
    return True

# Testet eine Hand auf alle möglichen Pokerkombinationen und gibt die Ergebnisse zurück
def check_hand(hand):
    # Speichert die Testergebnisse für jede mögliche Kombination in einem Dictionary
    hand_results = {
        "Royal Flush": is_royal_flush(hand),
        "Straight Flush": is_straight_flush(hand),
        "Four of a Kind": is_four_of_a_kind(hand),
        "Full House": is_full_house(hand),
        "Flush": is_flush(hand),
        "Straight": is_straight(hand),
        "Three of a Kind": is_three_of_a_kind(hand),
        "Two Pair": is_two_pair(hand),
        "Pair": is_pair(hand),
        "High Card": is_high_card(hand)
    }
    return hand_results

# Funktion, die ein vollständiges Deck mit 52 Karten generiert
def generate_deck():
    # Definiere die Farben (Hearts, Diamonds, Clubs, Spades)
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    # Definiere die Kartenwerte von 2 bis 14 (wobei 14 = Ass)
    ranks = list(range(2, 15))
    # Erstelle eine Liste von Karten, eine für jede Kombination von Wert und Farbe
    deck = [Card(rank, suit) for rank in ranks for suit in suits]
    return deck

# Funktion, die eine zufällige Hand aus dem Deck zieht
def draw_hand(deck, hand_size=5):
    # Wähle zufällig eine Hand von `hand_size` Karten aus dem Deck
    return random.sample(deck, hand_size)

# Funktion, die eine bestimmte Anzahl von Pokerhänden simuliert und die Ergebnisse zählt
def simulate_poker_hands(num_simulations):
    # Ein Counter-Objekt wird verwendet, um die Anzahl der Treffer für jede Kombination zu zählen
    stats = Counter()
    # Erstelle ein neues Deck
    deck = generate_deck()

    # Wiederhole die Simulation für die gegebene Anzahl von Simulationen
    for _ in range(num_simulations):
        # Ziehe eine zufällige Hand aus dem Deck
        hand = draw_hand(deck)
        # Überprüfe die Hand auf mögliche Pokerkombinationen
        result = check_hand(hand)
        # Zähle die erste Kombination, die gefunden wird (von Royal Flush bis High Card)
        for combination, hit in result.items():
            if hit:
                stats[combination] += 1  # Inkrementiere den Zähler für die Kombination
                break  # Stoppe, sobald eine Kombination gefunden wurde

    return stats

# Funktion, die die Prozentsätze der verschiedenen Kombinationen berechnet
def calculate_percentages(stats, total_hands):
    # Berechne den Prozentsatz jeder Kombination basierend auf der Anzahl der Simulationen
    percentages = {combination: (count / total_hands) * 100 for combination, count in stats.items()}
    return percentages

# Hauptfunktion zur Durchführung der Simulation
def run_simulation(num_simulations=1000000):
    # Simuliere die gegebene Anzahl von Pokerhänden
    stats = simulate_poker_hands(num_simulations)
    # Berechne die Prozentsätze der verschiedenen Kombinationen
    percentages = calculate_percentages(stats, num_simulations)

    # Gib die Ergebnisse der Simulation aus
    for combination, percentage in percentages.items():
        print(f"{combination}: {percentage:.6f}%")

# Führe die Simulation von 1.000.000 Pokerhänden aus
run_simulation()
