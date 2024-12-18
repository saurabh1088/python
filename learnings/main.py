import concepts
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

def main():
    logging.info('This is entry point')
    concepts.example_dynamic_typing_in_python()
    concepts.example_initialise_sample_class()
    concepts.example_create_object_for_sample_class_with_instance_properties()
    concepts.example_create_object_for_sample_class_with_type_properties()
    concepts.example_using_singleton_created_with_init()
    concepts.example_reference_counting()
    concepts.example_object_reference_removal_using_del()
    concepts.example_using_class_and_subclass_showing_inheritance()

if __name__ == '__main__':
    main()
    