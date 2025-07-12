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

def example_f_string():
    logging.info('--- Executing example_string_multiplication ---')

    some_value = 42
    logging.info(f'Sample string: {some_value}')

    name = 'Man of Steel'
    age = 22
    pi = 3.14159

    multi_line_info = f"""
    Justice League:
        Name: {name.upper()}
        Age: {age}
        Pi (approximately): {pi: .4f})
    """
    logging.info(multi_line_info)

    logging.info('----------------------------------------------')

