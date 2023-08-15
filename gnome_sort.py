def gnomeSort(nList):
  # Create a bunch of variables
  i = 1; # Checking index
  while i < len(nList): # While the checking index has not reached the end of the list
    if nList[i - 1] > nList[i] and i > 0: # If the current number based on the checking index is greater than the next number
      nList[i - 1], nList[i] = nList[i], nList[i - 1]; # Swap the two elements
      i -= 1;
    else: # If the two checked numbers are in order, move the checking index forward
      i += 1;
  return nList; # Return the sorted list
