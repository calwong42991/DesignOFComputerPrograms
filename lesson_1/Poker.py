'''
User Instructions
modify the poker() function to return the best hand according to the hand_rank() function. 
'''

def poker(hands):
  return max(hands, key=hand_rank)

def hand_rank(hand):
  "Return a value indicating the ranking of a hand."

def test():
  "Test cases for the functions in poker program."
  sf = '6C 7C 8C 0C TC'.split()
  fk = '9D 9H 9S 9C 7D'.split()
  fh = 'TD TC TH 7C 7D'.split()
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