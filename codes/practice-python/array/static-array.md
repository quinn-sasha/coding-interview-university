# Feature of array

- constant time access: read and write element
- how memory address is calculated
  - (starting_point) + element_size * (i - first_index)

## Multidimensional array

 1. skip rows that doesn't have target element
    - (target_row - start_row)
 2. skip columns
    - (target_column - start_column)

A. start + element_size * ((target_row - start_row) + (target_column - start_column))

## Array runtime

- read and write element: O(1)

|           | add  | remove |
| --------- | ---- | ------ |
| beggining | O(n) | O(n)   |
| end       | O(1) | O(1)   |
| middle    | O(n) | O(n)   |
