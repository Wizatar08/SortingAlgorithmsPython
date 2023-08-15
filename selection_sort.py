def selectionSort(nList):
  for i in range(len(nList)): # Loop through list using a main sorting index variable
    lowInd = i; # Set a new index, which will be the index of the lowest number
    for j in range(i, len(nList)): # Loop through the part of the list above the main sorting index, using a current index relative to the entire list
      if nList[j] < nList[lowInd]: # If the current index's list value is less than current lowest index's list value
        lowInd = j; # Set the lowest number index to the current index looped through
    nList[i], nList[lowInd] = nList[lowInd], nList[i]; # Swap the main sorting index's list value with the lowest index's list value
  return nList; # Return the sorted list
