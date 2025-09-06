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
# --- Main Functionality ---
def main():
    logging.info("Application started")
    try:
        # Simulate some operations
        logging.debug("Performing operation 1")
        # operation_1()
        logging.debug("Operation 1 completed")

        logging.debug("Performing operation 2")
        # operation_2()
        logging.debug("Operation 2 completed")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        logging.info("Application finished")


if __name__ == "__main__":
    main()

