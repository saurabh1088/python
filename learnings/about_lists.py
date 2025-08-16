import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

# --------------------------------------------------------------------------------
# --- Example functions ---

def example_lists_simple_concepts():
    logging.info('--- Executing example_lists_simple_concepts ---')
    logging.info('Creating a simple list')
    simple_list_numbers = [1, 2, 3]
    simple_list_strings = ['Batman', 'Superman', 'Wonder Woman']
    simple_list_mixed_types = [1, 1.0, 'Iron Man', 200, simple_list_numbers]
    logging.info(f'simple_list_numbers = {simple_list_numbers}')
    logging.info(f'simple_list_strings = {simple_list_strings}')
    logging.info(f'simple_list_mixed_types = {simple_list_mixed_types}')
    logging.info('----------------------------------------------')


# --------------------------------------------------------------------------------
# --- Entry point ---

def main():
    logging.info('This is entry point for lists examples')
    example_lists_simple_concepts()


if __name__ == '__main__':
    main()

