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
    object = concepts.SampleClassDeclaration()
    concepts.example_create_object_for_sample_class_with_instance_properties()
    concepts.example_create_object_for_sample_class_with_type_properties()

if __name__ == '__main__':
    main()
    