# Dynamic arrays

- Store pointer(memory address) to dynamically allocated array
- Replace old with newly allocated array if needed
- Some space is wasted

### What is needed to use dynamic arrays

Store:

- arr: dynamically allocated array
- capacity: maximum size of arr
- size: number of current elements in the arr

### Method

- get(i):
  - Return element at location i
- set(i, val):
  - Set val at i location
- PushBack(val):
  - add val to the end of array
- Remove(i):
  - Remove element at i
- size():
  - return the size of array

### Runtime

| method        | runtime            |
|---------------|--------------------|
| get(i)        | O(1)               |
| set(i, val)   | O(1)               |
| PushBack(val) | O(n) (mostly O(1)) |
| remove(i)     | O(n)               |
| size()        | O(1)               |

## Details of methods

### get(i)

```c
if i < 0 or i >= arr[size]:
 error: index out of range
return arr[i]
```

### set(i, val)

```c
if i < 0 or i >= arr[size]:
 error: index out of range
arr[i] = val
```

### PushBack(val)

```c
if size == capacity:
 allocate new_arr[capacity * 2]
 for i from 0 to size - 1:
  new_arr[i] <- arr[i]
 free arr
 arr <- new_arr
arr[size] = val
size <- size + 1
```

### remove(i)

```c
if i < 0 or i >= arr[size]:
 error: index out of range
for j from i to size - 2:
 arr[j] <- arr[j + 1]
size <- size - 1
```
