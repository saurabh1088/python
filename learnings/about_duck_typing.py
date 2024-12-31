import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

class Duck:
    def quack(self):
        logging.info('I am a Duck and I do quack, quack')

    def fly(self):
        logging.info('I am a Duck and I fly flap, flap')


class Person:
    def quack(self):
        logging.info('I am person but still I am quacking like a duck')

    def fly(self):
        logging.info('I am flapping my arms')


def example_duck_typing():
    duck = Duck()
    person = Person()
    make_it_quack_and_fly(duck)
    make_it_quack_and_fly(person)

def make_it_quack_and_fly(object):
    object.quack()
    object.fly()

if __name__ == '__main__':
    example_duck_typing()

