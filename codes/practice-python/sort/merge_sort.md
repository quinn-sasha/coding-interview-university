# Merge sort

```py
# divide process
mergesort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    l = mergesort(arr[0:n//2])
    r = mergesort(arr[n//2:n])
    return merge(l, r)
```

## how merge works

```py
# input: sorted arrays C and D(length n / 2)
# output: sorted array B(lenght n)
i = 1
j = 1
for k = 1 to n do
    if C[i] < D[j]:
        B[k] = C[i]
        i += 1
    else:
        B[k] = D[j]
        j += 1
```
