import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

# Simple class with no properties
class SampleClassDeclaration:

    def __init__(self):
        logging.info('Initialising class SampleClassDeclaration...')
        pass

class SampleClassWithInstanceProperties:

    def __init__(self, property):
        logging.info('Initialising class SampleClassWithInstanceProperties...')
        self.property = property

    def __str__(self):
        return f"This SampleClassWithInstanceProperties instance property's value is {self.property}\n- Type of property is {type(self.property)}"

class SampleClassWithTypeProperties:

    typeProperty = "value_for_type_property"

    def __init__(self):
        pass

def example_dynamic_typing_in_python():
    x = 10
    logging.info(f"x is {x} and type of x is {type(x)}")
    
    x = 1.5
    logging.info(f"x is {x} and type of x is {type(x)}")

    x = "string"
    logging.info(f"x is {x} and type of x is {type(x)}")

def example_create_object_for_sample_class_with_instance_properties():
    objectOne = SampleClassWithInstanceProperties(property="string")
    objectTwo = SampleClassWithInstanceProperties(property=100)
    logging.info(objectOne)
    logging.info(objectTwo)

def example_create_object_for_sample_class_with_type_properties():
    objectOne = SampleClassWithTypeProperties()
    objectTwo = SampleClassWithTypeProperties()
    objectThree = SampleClassWithTypeProperties()

    logging.info("Initial value for type property across multiple instances")
    logging.info(f"Object 1 : {objectOne.typeProperty}")
    logging.info(f"Object 2 : {objectOne.typeProperty}")
    logging.info(f"Object 3 : {objectOne.typeProperty}")

    logging.info("Updating type property value using objectOne...")
    logging.info("Update finished, printing values again...")
    objectOne.typeProperty = "updated_type_proprty_value"

    logging.info(f"Object 1 : {objectOne.typeProperty}")
    logging.info(f"Object 2 : {objectOne.typeProperty}")
    logging.info(f"Object 3 : {objectOne.typeProperty}")
