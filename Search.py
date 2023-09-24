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
        self._time = time.perf_counter()
        self._search(item)
        self._time = time.perf_counter() - self._time
        return self._time


"""Module with the implementation of the Linear Search algorithm."""

class LinSearch(Search):
    """Class that represents a Linear Search implementation."""

    def _search(self, item):
        for i in self.get_items():
            if i == item:
                return True
        return False


"""Module with the implementation of the Binary Search algorithm."""

class BinSearch(Search):
    """Class that represents a Binary Search implementation."""

    def _search(self, item):
        _items = self.get_items()
        left, right = 0, len(_items)-1
        while True:
            if(left > right):
                break
            else:
                mid = (left + right) //2
                if(_items[mid] == item):
                    return True
                else:
                    if(_items[mid] < item):
                        left = mid + 1
                    else:
                        right = mid - 1
        return False