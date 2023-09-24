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

    def _time(self):
        self.time = 0
        return self.time


"""Module with the implementation of the Linear Search algorithm."""

class LinSearch(Search):
    """Class that represents a Linear Search implementation."""

    def _search(self, item):
        n=len(self._items)
        for i in range(n):
            if self._items[i] == item:
                return True
        return False

    def _time(self, item):
        start_time =time.time()
        self._search(self, item)
        end_time =time.time()
        timetaken= end_time - start_time
        return timetaken


"""Module with the implementation of the Binary Search algorithm."""

class BinSearch(Search):
    """Class that represents a Binary Search implementation."""

    def _search(self, items):
        # your code here

        return False


    def _time(self, items):
        # your code here

        return self.time