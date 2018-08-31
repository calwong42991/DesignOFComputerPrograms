'''
User Instructions
modify the poker() function to return the best hand according to the hand_rank() function. 
'''

def poker(hands):
  return max(hands, key=hand_rank)

def card_ranks(cards):
  "Return a list of the ranks, sorted with higher first"
  ranks = ['--23456789TJQKA'.index(r) for r,s in cards]
  ranks.sort(reverse = True)
  return ranks

def hand_rank(hand):
  "Return a value indicating the ranking of a hand."
  ranks = card_ranks(hand)
  if straight(ranks) and flush(hand):
    return (8, max(ranks))
  elif kind(4, ranks):
    return (7, kind(4, ranks), kind(1, ranks))
  elif kind(3, ranks) and kind(2, ranks):
    return (6, kind(3, ranks), kind(2, ranks))
  elif flush(hand):
    return (5, ranks)
  elif straight(ranks):
    return (4, max(ranks))
  elif kind(3, ranks):
    return (3, kind(3, ranks), ranks)
  elif two_pair(ranks):
    return (2, two_pair(ranks), ranks)
  elif kind(2, ranks):
    return (1, kind(2, ranks), ranks)
  else: 
    return (0, ranks)

def test():
  "Test cases for the functions in poker program."
  sf = '6C 7C 8C 0C TC'.split()
  fk = '9D 9H 9S 9C 7D'.split()
  fh = 'TD TC TH 7C 7D'.split()
  assert straight([9, 8, 7, 6, 5]) == True
  assert straight([9, 8, 8, 6, 5]) == False
  assert flush(sf) == True
  assert flush(fk) == False
  assert card_ranks(sf) == [10, 9, 8, 7, 6]
  assert card_ranks(sf) == [9, 9, 9, 9, 7]
  assert card_ranks(sf) == [10, 10, 10, 7, 7]
  assert poker([sf, fk, fh]) == sf
  assert poker([fk, fh]) == fk
  assert poker([fh, fh]) == fh
  assert poker([sf]) == sf
  assert poker([sf] + 99*[fh]) == sf
  assert hand_rank(sf) == (8, 10)
  assert hand_rank(fk) == (7, 9, 7)
  assert hand_rank(fh) == (6, 10, 7)
  return 'tests pass'