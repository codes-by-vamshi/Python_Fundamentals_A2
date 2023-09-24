# Python_Fundamentals_A2

# Contributions
### 1. Devesh - Bubble Sort
### 2. Vamshi - Merge Sort
### 3. Ann - Linear Search
### 4. Vishakha - Binary Search

# How to use Search Module

## Linear Search
import Search

searchObj = Search.LinSearch([1,2,3,4])

print(searchObj._search(2))

### to get time for search
print(searchObj._time(2))

## Binary Search
import Search

searchObj = Search.LinSearch([1,2,3,4])

print(searchObj._search(2))

### to get time for search
print(searchObj._time(2))

# How to use Sort Class

## Bubble Sort
import Sort

sortObj = Sort.BubbleSort([3,4,2,1])

print(sortObj._sort())

### to get time for sort
print(sortObj._time())

## Merge Sort
import Sort

sortObj = Sort.MergeSort([3,4,2,1])

print(sortObj._sort())

### to get time for sort
print(sortObj._time())
