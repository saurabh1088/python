import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

def example_string_multiplication():
    logging.info('--- Executing example_string_multiplication ---')
    sample_string = 'Hello!'
    logging.info(f'Sample string: {sample_string}')
    logging.info(f'Value of sample string multiplying by 3 : {sample_string*3}')
    logging.info('----------------------------------------------')