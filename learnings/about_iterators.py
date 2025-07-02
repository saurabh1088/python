import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

def example_iterator_behaviour():
    justice_league_tuple = ("Batman", "Superman", "Wonder Woman", "Flash", "Aquaman")
    iterator = iter(justice_league_tuple)
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))

def example_iterator_behaviour_for_custom_counter_iterator():
    counter = Counter(5)
    iterator = iter(counter)
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))


class Counter:
    """
    An iterator that counts from 1 up to a specified maximum value.

    This class implements the iterator protocol by defining the `__iter__` and `__next__` methods.
    Each call to `next()` returns the next number in the sequence, starting from 1 up to `maximum`.

    Attributes:
        count (int): The current count, initialized to 0.
        maximum (int): The upper limit of the count (inclusive).
    """

    def __init__(self, maximum):
        """
        Initializes the Counter with a maximum value.

        Args:
            maximum (int): The maximum value the counter will count up to.
        """
        self.count = 0
        self.maximum = maximum

    def __iter__(self):
        """
        Returns the iterator object itself.

        Returns:
            Counter: The iterator instance.
        """
        return self

    def __next__(self):
        """
        Returns the next number in the sequence.

        Increments the internal counter by 1 and returns the new value.
        Raises StopIteration when the count exceeds the maximum value.

        Returns:
            int: The next number in the counting sequence.

        Raises:
            StopIteration: When the counter exceeds the maximum value.
        """
        if self.count < self.maximum:
            self.count += 1
            return self.count
        else:
            raise StopIteration

        