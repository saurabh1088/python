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
    def __init__(self, maximum):
        self.count = 0
        self.maximum = maximum

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.maximum:
            self.count += 1
            return self.count
        else:
            raise StopIteration
