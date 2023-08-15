def insertionSort(nList):
  for i in range(0, len(nList) - 1): # Loop through list (starts at 1 so loop does not check negative indexes)
    movementTracker = i; # Set a movement tracker variable to the current index. This variable will track what index in the list values need to be swapped to
    while nList[movementTracker + 1] < nList[movementTracker] and movementTracker >= 0: # Keep running until the tracker value is in its correct place or the check reaches the beginning of the list
      nList[movementTracker], nList[movementTracker + 1] = nList[movementTracker + 1], nList[movementTracker]; # Swap the two values
      movementTracker -= 1; # Subtract one to the tracker variable so the values in the list can swap further towards the beginning of the list
  return nList; # Return the sorted list
