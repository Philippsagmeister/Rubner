import random
from collections import Counter

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank} of {self.suit}"


def get_suits(hand):
    return [card.suit for card in hand]


def get_ranks(hand):
    return [card.rank for card in hand]


def is_royal_flush(hand):
    return is_straight_flush(hand) and 14 in get_ranks(hand)


def is_straight_flush(hand):
    return is_flush(hand) and is_straight(hand)


def is_four_of_a_kind(hand):
    rank_counts = Counter(get_ranks(hand))
    return 4 in rank_counts.values()


def is_full_house(hand):
    rank_counts = Counter(get_ranks(hand))
    return set(rank_counts.values()) == {3, 2}


def is_flush(hand):
    suits = get_suits(hand)
    return len(set(suits)) == 1


def is_straight(hand):
    ranks = get_ranks(hand)
    rank_values = sorted(ranks)
    return rank_values == list(range(min(rank_values), min(rank_values) + 5))


def is_three_of_a_kind(hand):
    rank_counts = Counter(get_ranks(hand))
    return 3 in rank_counts.values()


def is_two_pair(hand):
    rank_counts = Counter(get_ranks(hand))
    return len([count for count in rank_counts.values() if count == 2]) == 2


def is_pair(hand):
    rank_counts = Counter(get_ranks(hand))
    return 2 in rank_counts.values()


def is_high_card(hand):
    return True


def check_hand(hand):
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


def generate_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = list(range(2, 15))
    return [Card(rank, suit) for rank in ranks for suit in suits]


def draw_hand(deck, hand_size=5):
    return random.sample(deck, hand_size)


def simulate_poker_hands(deck, num_simulations):
    stats = Counter()
    for _ in range(num_simulations):
        hand = draw_hand(deck)
        try:
            result = check_hand(hand)
            for combination, hit in result.items():
                if hit:
                    stats[combination] += 1
                    break
        except ValueError as e:
            print(f"Fehler bei der Handprüfung: {e}")
    return stats


def calculate_percentages(stats, total_hands):
    return {combination: (count / total_hands) * 100 for combination, count in stats.items()}


def run_simulation():
    num_simulations = int(input("Enter the number of simulations: "))
    deck = generate_deck()
    stats = simulate_poker_hands(deck, num_simulations)
    percentages = calculate_percentages(stats, num_simulations)

    for combination, percentage in percentages.items():
        print(f"{combination}: {percentage:.2f}%")


def main():
    run_simulation()


if __name__ == "__main__":
    main()
