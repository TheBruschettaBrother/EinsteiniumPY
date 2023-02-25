def get_element_info(element_name):
    # Dictionary containing information about each element
    elements = {
        "hydrogen": {
            "symbol": "H",
            "atomic number": 1,
            "atomic mass": 1.008,
            "group": 1,
            "period": 1,
            "category": "nonmetal"
        },
        "helium": {
            "symbol": "He",
            "atomic number": 2,
            "atomic mass": 4.003,
            "group": 18,
            "period": 1,
            "category": "noble gas"
        },
        "lithium": {
            "symbol": "Li",
            "atomic number": 3,
            "atomic mass": 6.941,
            "group": 1,
            "period": 2,
            "category": "alkali metal"
        },
        # add more elements here...
    }

    # Convert the input to lowercase for easier comparison
    element_name = element_name.lower()

    # Check if the element exists in the dictionary
    if element_name in elements:
        # Return the information about the element
        return elements[element_name]
    else:
        # If the element doesn't exist in the dictionary, return None
        return None
