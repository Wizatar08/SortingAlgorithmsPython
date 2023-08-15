def bubbleSort(nList):
  for i in range(len(nList)): # Create a wall. This will serve to prevent comparing numbers that have already been sorted at the end of the list
    swapped = False; # Track if anything was swapped during this loop
    for j in range(len(nList) - i - 1): # 'For' loop that will use indexes that will compare two values in specific positions
      if nList[j] > nList[j + 1]: # Get the number which the index corresponds to in the list and the next one, and compare their values
        nList[j], nList[j + 1] = nList[j + 1], nList[j]; # If they need to, swap places
        swapped = True; # Remember that there was a swap
    if not swapped: # If there were no swaps, break the loop
      break;
  return nList; # Return the sorted list
