import time
from abc import ABC, abstractmethod

"""Module with the base implementation of a Search class."""

class Search(ABC):
    """Abstract base class for searching."""

    def __init__(self, items):
        self._items = items

    @abstractmethod
    def _search(self, item):
        """Returns True if item is contained in elements
        in the `_items` property else False.
        Returns:
            Boolean: True/False
        """
        pass

    def get_items(self):
        return self._items

    def _time(self, item):
        # Returns time taken for searching the item in the list
        self._time = time.perf_counter()
        self._search(item)
        self._time = time.perf_counter() - self._time
        return self._time


"""Module with the implementation of the Linear Search algorithm."""

class LinSearch(Search):
    """Class that represents a Linear Search implementation."""

    def _search(self, item):
        # Searches item in the list by iterating over list by one item after the other 
        for i in self.get_items():
            if i == item:
                # Returns True when Item found
                return True
        # If item not found returns False
        return False


"""Module with the implementation of the Binary Search algorithm."""

class BinSearch(Search):
    """Class that represents a Binary Search implementation."""

    def _search(self, item):
        # Searches the item in list(which is sorted)
        _items = self.get_items()
        left, right = 0, len(_items)-1
        while True:
            if(left > right):
                # Breaking the loop when left index becomes greater than right
                break
            else:
                # Calculating middle element index in our search space
                mid = (left + right) //2
                if(_items[mid] == item):
                    # Returns True if element Found
                    return True
                else:
                    if(_items[mid] < item):
                        # If item is greater than middle element, search space changes to second half of current search space
                        left = mid + 1
                    else:
                        # If item is less than middle element, search space changes to first half of current search space
                        right = mid - 1
        return False