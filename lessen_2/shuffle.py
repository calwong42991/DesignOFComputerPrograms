def shuffle(deck):
  N = len(deck)
  for i in range(N - 1):
    swap(deck, i, random.randrange(i, N))
def swap(deck, i, j):
  print ('swap', i, j)
  deck[i], deck[j] = deck[j], deck[i]