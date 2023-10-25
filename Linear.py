def linear_search(array, element):
  """Searches for an element in a given array using linear search.

  Args:
    array: A list of elements.
    element: The element to search for.

  Returns:
    The index of the element in the array if found, or -1 if not found.
  """

  for i in range(len(array)):
    if array[i] == element:
      return i
  return -1


# Example usage:

array = [1, 3, 5, 7, 9]
element = 7

index = linear_search(array, element)

if index != -1:
  print("The element {} is found at index {}.".format(element, index))
else:
  print("The element {} is not found in the array.".format(element))
