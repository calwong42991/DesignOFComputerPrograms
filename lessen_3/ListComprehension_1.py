udacity_tas = ['peter', 'andy', 'sarah', 'gundega']

# initiate list
bad_uppercase_tas = []

# iterate through list
for i in range(len(udacity_tas)):
  # set to upper then append to new list
  bad_uppercase_tas.append(udacity_tas[i].upper())

# print(bad_uppercase_tas)

# better way
udacity_tas = [name.upper() for name in udacity_tas]

print(udacity_tas)