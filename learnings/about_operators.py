import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

# ** (Exponentiation): Raises the left operand to the power of the right.
def example_exponentiation():
    logging.info('--- Executing example_exponentiation ---')
    logging.info(f'2 to the power of 16 is : {2**16}')
    logging.info('----------------------------------------------')