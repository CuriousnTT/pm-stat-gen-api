from typing import List, Type

def get_list_of_objects_by_template(template: Type, *values: List) -> List:
    """
    Generate a list of dictionaries based on a template and values.

    Args:
        template (Type): A dataclass Type with key names.
        *values (List): Lists containing the values to be inserted into the keys.
        NB! The function assumes that all lists passed to *values have the same length, and also assumes that the number of lists equals the keys in the template!

    Returns:
        List: A list of objects where each object maps values from the different lists to keys in the template based on their index.
    """
    list_of_objects = []
    for value_set in zip(*values):
        object_from_values = template(*value_set)
        list_of_objects.append(object_from_values)
    return list_of_objects
