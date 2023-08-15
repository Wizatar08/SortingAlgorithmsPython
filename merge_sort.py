def mergeSort(nList):
  if len(nList) == 1: # If the list is 1 in size, return the list
    return nList;
  midpoint = len(nList) // 2 # Calculate midpoint of the list
  return merge(mergeSort(nList[:midpoint]), mergeSort(nList[midpoint:])) # Merge sort by splitting the list repeatedly  in half using recursion of the mergeSort function and putting it through the helper function.

# HELPER FUNCTION FOR RECURSION
def merge(list1, list2):
  newList = []; # Create a new list
  while len(list1) > 0 and len(list2) > 0: # While both these lists have something inside of them
    # Keep comparing the first value of the first list with the first value of the second list. The smaller number will go into the third list and removed from its initial list. Keep doing this until one list is completely empty.
    if list1[0] < list2[0]:
      newList.append(list1.pop(0));
    else:
      newList.append(list2.pop(0));
  newList += list1 + list2;
  return newList; # Return that list
