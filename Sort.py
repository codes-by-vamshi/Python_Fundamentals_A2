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

    def _sort(self, items):
        # your code here

        return items


"""Module with the implementation of the MergeSort algorithm."""

class MergeSort(Sort):
    """Class that represents a MergeSort implementation."""

    def _sort(self, items):
        # your code here

        return sorted_items

    def _merge(self, left, right):
        # your code here

        return merged