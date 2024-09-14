# Two pointers

- search pairs in a sorted array
- One points smallest item (arr[0]) and other points biggest item (arr[length - 1])

## Flow

Let i and j are smallest and biggest index.

- if arr[i] + arr[j] < target, move i pointer right
- if arr[i] + arr[j] > target, move j pointer left

## Example

```py
def isPairsum(a: list[int], n: int, target: int) -> bool:
 """Return True if sum of pair elements is equal to target.

 a: arr
 n: lenght of a
 """
 i, j = 0, n - 1
 while i != j:
  if sum(a[i], a[j]) == target:
   return True
  elif sum(a[i], a[j]) < target:
   i += 1
  else:
   j -= 1
 return False
```
