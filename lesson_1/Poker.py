'''
User Instructions
modify the poker() function to return the best hand according to the hand_rank() function. 
'''

def poker(hands):
  return max(hands, key=hand_rank)

def hand_rank(hand):
  "Return a value indicating the ranking of a hand."
