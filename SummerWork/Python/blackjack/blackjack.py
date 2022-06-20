def blackjack(player_cards: list, dealer_cards: list):

    for cards in [player_cards, dealer_cards]:
        if 1 in cards and sum(cards) + 10 <= 21:
            cards.append(10)

    player_score = sum(player_cards)
    dealer_score = sum(dealer_cards)

    return dealer_score < player_score <= 21 or player_score <= 21 < dealer_score