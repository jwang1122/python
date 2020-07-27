#sort list
cars = ['Ford', 'BMW', 'Volvo','Cammary']
print(cars)
cars.sort()
print(cars)  #cars list modified

cars.sort(reverse=True)
print(cars)

cars.sort(key=lambda s: len(s))
print(cars)

cars.sort(key=lambda s: len(s), reverse=True)
print(cars)

# sort dictionary
def myFunc(e):
  return e['year']
  
cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc, reverse=True)
print(cars)