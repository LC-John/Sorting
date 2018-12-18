# Sorting

A sorting algorithm a day, keeps bugs away.

## Bubble Sort

```C
for (int i = 0; i < arr.length; i++)
    for (int j = i+1; j < arr.length; j++)
        if (compare(arr[i], arr[j]) < 0)
        {
            arr[i] = arr[i] ^ arr[j];
            arr[j] = arr[i] ^ arr[j];
            arr[i] = arr[i] ^ arr[j];
        }
```

![bubble](./images/BubbleSort.gif)