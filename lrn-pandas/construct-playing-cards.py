# Hearts, Spades, Clubs, Diamonds
suits = ['H', 'S', 'C', 'D']
card_val = (range(1, 11) + [10] * 3) * 4
base_names = ['A'] + range(2, 11) + ['J', 'K', 'Q'] 
cards = []
for suit in ['H', 'S', 'C', 'D']:
	cards.extend(str(num) + suit for num in base_names)

deck = Series(card_val, index=cards)


def draw(deck, n=5):
	return deck.take(np.random.permutation(len(deck))[:n])


get_suit = lambda card: card[-1] # last letter is suit
deck.groupby(get_suit).apply(draw, n=2)
# or
deck.groupby(get_suit, group_keys=False).apply(draw, n=2)