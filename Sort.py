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
        self.time = 0
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

    def _sort(self, items):
        # your code here

        return sorted_items

    def _merge(self, left, right):
        # your code here

        return merged

    def _time(self, items):
        # your code here

        return self.time