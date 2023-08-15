def cocktailSort(numList): # USE FOR LOOPS
  # Create a lot of variables
  checkListMin = 0; # checkListMin and checkListMax: specifies the minimum index (wall) that should be checked (anything before that is already sorted) and the maximum index (wall) that should be checked (anything after that is already sorted)
  checkListMax = len(numList) - 1;
  dir = 1; # Direction of sorting, 1 to go forward, -1 to go backward
  i = 0; # Index of checking
  swapped = False; # Specifies if there is a swap from one instance of checking from checkListMin-->checkListMax or checkListMax-->checkListMin
  while True: # Loop until broken
    if checkListMin == checkListMax: # Check if the entire list has been looped through (if it gets to the point where the min wall is equal to the max wall, the entire list is already sorted)
      break; # Break out of the loop
    elif (dir == 1 and i == checkListMax - 1) or (dir == -1 and i == checkListMin): # If the checking index gets to the maximum or ninimum value
      if dir == 1: # Move the maximum down if it reaches the uppermost portion of the list
        checkListMax -= 1;
      else: # Move the minimum up if it reaches the lowermost portion of the list
        checkListMin += 1;
      dir *= -1; # Switch the direction
      if not swapped: # If there was no swaps in this iteration, break the loop
        break;
      swapped = False; # Set the swap check variable back to false
    if numList[i] > numList[i + 1] and i >= 0: # If element i is greater than the next element (i + 1) and if i is greater than or equal to 0 (the second condition is meant to remove issues where i becomes a negative number for very small lists)
      numList[i], numList[i + 1] = numList[i + 1], numList[i]; # Swap the two elements
      swapped = True; # Say that there was a swap
    i += dir; # Move the checking index
  return numList; # Return the sorted list
