

def _matrix(index, column_range):
  matrix =  [[0 for x in range(column_range +1)] for y in range(len(index)+1)]
  for i in range(column_range +1):
    matrix[0][i] =i
  return matrix

m1 = _matrix([15,10,5,1], 10)