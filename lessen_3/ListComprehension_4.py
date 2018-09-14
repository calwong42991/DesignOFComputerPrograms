# list of tuples

ta_data = [
  ('Peter', 'USA', 'CS262'),
  ('Andy', 'USA', 'CS212'),
  ('Sarah', 'England', 'CS101'),
  ('Job', 'USA', 'CS387'),
  ('Sean', 'USA', 'CS253'),
  ('Calvin', 'USA', 'CS353'),
]

ta_300 = [name + ' lives in ' + country + ' and is the TA for ' + course for name, country, course in ta_data if course.find('CS3') != -1]

for row in ta_300:
  print(row)