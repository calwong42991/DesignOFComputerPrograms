my_set = set(['Set: ', 'one', 'two', 'three', 'two'])
my_frozenSet = frozenset({'Frozen: ', 'one', 'two', 'three', 'two'})
my_set.add('did this add?') 

'''ERROR 'frozenset' object has no attribute 'add' 
my_frozenSet.add('did this add?') '''

print('Pop:    ', my_set.pop())
print('remove: ', my_set.remove('one'))
# remove only if it is there
print('discard:', my_set.discard('five'))


print('Set:    ', my_set)
print('Frozen: ', my_frozenSet)
print('Length: ', len(my_set))

#print('clear:  ', my_set.clear())