import about_generators
import concepts
import logging
import about_none
import about_pointers
import about_iterators

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

def about_pointers_method_calls():
    about_pointers.example_pointer_behaviour_over_int_types()
    about_pointers.example_pointer_behaviour_over_string_types()
    about_pointers.example_pointer_behaviour_over_dict_types()
    about_pointers.example_pointer_behaviour_over_list_types()
    about_pointers.example_pointers_check_reference_equality()

def about_none_method_calls():
    about_none.type_of_none()
    about_none.singleton_nature_of_none()
    about_none.result_type_of_functions_without_any_return()
    about_none.usage_as_variable_initialisation()
    about_none.usage_as_in_boolean_context()

def concepts_method_calls():
    concepts.example_dynamic_typing_in_python()
    concepts.example_initialise_sample_class()
    concepts.example_create_object_for_sample_class_with_instance_properties()
    concepts.example_create_object_for_sample_class_with_type_properties()
    concepts.example_using_singleton_created_with_init()
    concepts.example_reference_counting()
    concepts.example_object_reference_removal_using_del()
    concepts.example_using_class_and_subclass_showing_inheritance()
    concepts.example_showing_python_as_interpreted_language()

def about_iterators_method_calls():
    about_iterators.example_iterator_behaviour()
    about_iterators.example_iterator_behaviour_for_custom_counter_iterator()
    about_iterators.example_iterator_behaviour_going_beyond_limit()

def about_generators_method_calls():
    about_generators.example_simple_generator()
    about_generators.example_generator_behaviour()

def main():
    logging.info('This is entry point')
    # about_pointers_method_calls()
    # about_none_method_calls()
    # concepts_method_calls()
    # about_iterators_method_calls()
    # about_generators_method_calls()

if __name__ == '__main__':
    main()
    

