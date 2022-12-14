def flatten(x):
  """flatten(sequence) -> list"""

  result = []
  for el in x:
    # alternatively:
    # if isinstance(el, (list, tuple)):
    if (type(el) == list) or (type(el) == tuple):
      result.extend(flatten(el))
    else:
      result.append(el)
  return result
  
print(flatten([(1,2), "Python", ["a",[1,7]], 1, 1.3]))
