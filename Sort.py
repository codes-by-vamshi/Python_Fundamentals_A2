import time
from abc import ABC, abstractmethod

"""Module with the base implementation of a Sort class."""

class Sort(ABC):
    """Abstract base class for sorting."""

    def __init__(self, items):
        self._items = items

    @abstractmethod
    def _sort(self):
        """Returns the sorted version of the elements contained
        in the `_items` property.
        Returns:
            List: The sorted elements.
        """
        pass

    def get_items(self):
        return self._items

    def _time(self):
        # Returns time taken for sorting the list
        self._time = time.perf_counter()
        self._sort()
        self._time = time.perf_counter() - self._time
        return self._time


"""Module with the implementation of the BubbleSort algorithm."""

class BubbleSort(Sort):
    """Class that represents a BubbleSort implementation."""

    def _sort(self):
        # Making a copy of list to sort
        _items = self.get_items().copy()
        # Iterating over list, comparing adjacent elements and swapping them if necessary
        for i in range(len(_items)):
            for j in range(len(_items)-i-1):
                if _items[j] > _items[j+1]:
                    # Swapping the elements if they are out of order
                    _items[j],_items[j+1] = _items[j+1],_items[j]
        # Return the sorted list
        return _items

"""Module with the implementation of the MergeSort algorithm."""

class MergeSort(Sort):
    """Class that represents a MergeSort implementation."""

    def _sort(self):
        # Making a copy of list to sort
        _items = self.get_items().copy()
        # Initializing the size of sub array
        size = 1
        while True:
            if(size >= len(_items)):
                break
            else:
                for i in range(0,len(_items),size*2):
                    # Dividing the array into two sub arrays
                    left = _items[i : i+size]
                    right = _items[i+size : i+size*2]
                    # Merging the sub arrays
                    merged = self._merge(left,right)
                    # Updating the main array with merged subarrays
                    _items[i : i+len(merged)] = merged
                # Doubling the size of subarray for next iteration
                size = size*2
        # Return sorted list
        return _items

    def _merge(self, left, right):
        merged = []
        i,j = 0,0
        # Merging two subarrays in sorted order
        while i < len(left) and j < len(right):
            if(left[i] < right[j]):
                merged.append(left[i])
                i+=1
            else:
                merged.append(right[j])
                j+=1
        # Adding any remaining elements from the subarray if any  
        if(i!=len(left)):
            merged.extend(left[i:])
        if(j!=len(right)):
            merged.extend(right[j:])
        # Returning the merged subarray
        return merged