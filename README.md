# EinsteiniumPY
Python Library for pulling basic Scientific Info
!\[my badge\](https://badgen.net/github/release/TheBruschettaBrother/EinsteiniumPY)
# Usage

## Exsample 1
```
import Einsteinium as einsteinium
element_name = "hydrogen"
element_info = einsteinium.periodic_table_get(element_name)
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
**Exsample 1's Output**
```
Symbol: H
Atomic number: 1
Atomic mass: 1.008
Group: 1
Period: 1
Category: nonmetal
```

# Installation
Put the ```Einsteinium.py``` file into your scripts folder and Import the File as a library with
```import Einsteinium as einsteinium```

If You need help importing files as libraries use [how-to-import-a-library-in-python](https://codeberryschool.com/blog/en/how-to-import-a-library-in-python/) by [codeberryschool.com](codeberryschool.com)

# Functionality
as of now we have the .periodic_table_get function that can fetch about a certain element

## .periodic_table_get

The .periodic_table_get function can fetch the data about a element such as the, symbol(Eg."H"), atomic number(Eg. 1),atomic mass(Eg. 1.008),group(Eg. 1),period(1),category(Eg. nonmetal). 


We are working on adding all the elements of the elements to our index but for now we only have
- hydrogen
- lithium
- helium
