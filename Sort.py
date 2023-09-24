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
        self._time = time.perf_counter()
        self._sort(self.get_items())
        self._time = time.perf_counter() - self._time
        return self.time


"""Module with the implementation of the BubbleSort algorithm."""

class BubbleSort(Sort):
    """Class that represents a BubbleSort implementation."""

    def _sort(self):
        _items = self.get_items().copy()
        for i in range(len(_items)):
            for j in range(len(_items)-i-1):
                if _items[j] > _items[j+1]:
                    _items[j],_items[j+1] = _items[j+1],_items[j]
        return _items

"""Module with the implementation of the MergeSort algorithm."""

class MergeSort(Sort):
    """Class that represents a MergeSort implementation."""

    def _sort(self):
        _items = self.get_items().copy()
        size = 1
        while True:
            if(size >= len(_items)):
                break
            else:
                for i in range(0,len(_items),size*2):
                    left = _items[i : i+size]
                    right = _items[i+size : i+size*2]
                    merged = self._merge(left,right)
                    _items[i : i+len(merged)] = merged
                size = size*2
        return _items

    def _merge(self, left, right):
        merged = []
        i,j = 0,0
        while i < len(left) and j < len(right):
            if(left[i] < right[j]):
                merged.append(left[i])
                i+=1
            else:
                merged.append(right[j])
                j+=1
        if(i!=len(left)):
            merged.extend(left[i:])
        if(j!=len(right)):
            merged.extend(right[j:])
        return merged