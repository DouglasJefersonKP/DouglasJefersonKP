import random

# Simplified Truco game for two players
# Deck with values 1-7, J, Q, K (Truco uses a 40 card deck)
values = ['4', '5', '6', '7', 'Q', 'J', 'K', 'A', '2', '3']
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

def create_deck():
    """Create a deck of 40 cards."""
    return [f"{v} of {s}" for v in values for s in suits]

def card_rank(card):
    """Return the rank index of the card for comparison."""
    value = card.split()[0]
    return values.index(value)

def deal_cards(deck):
    """Deal three cards to each player."""
    random.shuffle(deck)
    return [deck[:3], deck[3:6]], deck[6:]

def choose_card(hand):
    """Player chooses a card from their hand."""
    while True:
        print("\nSua mão:")
        for idx, card in enumerate(hand):
            print(f"{idx + 1} - {card}")
        choice = input("Escolha uma carta (1-3): ")
        if choice.isdigit() and 1 <= int(choice) <= len(hand):
            return hand.pop(int(choice) - 1)
        print("Escolha inválida. Tente novamente.")

def play_round(player_hand, cpu_hand):
    """Play a single round (trick)."""
    player_card = choose_card(player_hand)
    cpu_card = random.choice(cpu_hand)
    cpu_hand.remove(cpu_card)
    print(f"\nVocê jogou {player_card}")
    print(f"CPU jogou {cpu_card}")
    if card_rank(player_card) > card_rank(cpu_card):
        print("Você ganhou a rodada!")
        return 1
    elif card_rank(player_card) < card_rank(cpu_card):
        print("CPU ganhou a rodada!")
        return -1
    else:
        print("Empate na rodada!")
        return 0

def main():
    deck = create_deck()
    hands, _ = deal_cards(deck)
    player_hand, cpu_hand = hands
    player_score = cpu_score = 0
    round_number = 1
    while player_score < 2 and cpu_score < 2 and player_hand:
        print(f"\n-- Rodada {round_number} --")
        result = play_round(player_hand, cpu_hand)
        if result == 1:
            player_score += 1
        elif result == -1:
            cpu_score += 1
        round_number += 1
    if player_score > cpu_score:
        print("\nParabéns! Você venceu o jogo de Truco!")
    elif cpu_score > player_score:
        print("\nA CPU venceu o jogo de Truco!")
    else:
        print("\nJogo empatado!")

if __name__ == "__main__":
    main()
