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
