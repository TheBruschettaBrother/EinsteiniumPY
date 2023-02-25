# EinsteiniumPY
Python Library for pulling basic Scientific Info

#Usage
```
import periodic_table
element_name = "hydrogen"
element_info = periodic_table.get_element_info(element_name)
if element_info:
    print(f"Symbol: {element_info['symbol']}")
    print(f"Atomic number: {element_info['atomic number']}")
    print(f"Atomic mass: {element_info['atomic mass']}")
    print(f"Group: {element_info['group']}")
    print(f"Period: {element_info['period']}")
    print(f"Category: {element_info['category']}")
else:
    print("Element not found.")
```
#Installation
```put the ```
