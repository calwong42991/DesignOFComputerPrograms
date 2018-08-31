import random 

def deal(numHands, n=5, deck = [r+s for r in '23456789TJQKA' for s in 'SHDC']):
  "Shuffle the deck and deal out num_hands n-card hands"
  random.shuffle(deck)
  return [deck[n*i:n*(i+1)] for i in range(numHands)]

print(deal(2))
