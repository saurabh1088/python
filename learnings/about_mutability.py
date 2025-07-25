import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

def example_immutable_type_int():
    logging.info('--- Executing example_immutable_type_int ---')
    x = 10
    logging.info(f"x value: {x}")
    logging.info(f"x identity: {id(x)}")
    logging.info(f'Assigning x to new variable y')
    y = x
    logging.info(f"y value: {y}")
    logging.info(f"y identity: {id(x)}")
    if id(x) == id(y):
        if x == y:
            logging.info("x and y are having equal identity and value")
    logging.info('----------------------------------------------')

